"""
Lightweight Data Quality Framework

A framework for implementing data quality expectations, tracking failures,
and explaining what breaks and why it matters.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Callable, Tuple
from dataclasses import dataclass, field
from enum import Enum
import json
import sqlite3
from pathlib import Path


class ExpectationType(Enum):
    """Types of data quality expectations"""
    NOT_NULL = "not_null"
    UNIQUE = "unique"
    IN_RANGE = "in_range"
    MATCHES_PATTERN = "matches_pattern"
    CUSTOM = "custom"
    REFERENTIAL_INTEGRITY = "referential_integrity"
    COMPLETENESS = "completeness"
    ACCURACY = "accuracy"
    CONSISTENCY = "consistency"
    TIMELINESS = "timeliness"


class Severity(Enum):
    """Severity levels for data quality issues"""
    CRITICAL = "critical"  # Blocks downstream processes
    HIGH = "high"  # Significant impact on analytics/reports
    MEDIUM = "medium"  # Moderate impact
    LOW = "low"  # Minor impact


@dataclass
class Expectation:
    """Represents a data quality expectation"""
    name: str
    expectation_type: ExpectationType
    table_name: str
    column_name: Optional[str] = None
    description: str = ""
    severity: Severity = Severity.MEDIUM
    downstream_impact: str = ""
    validation_func: Optional[Callable] = None
    parameters: Dict[str, Any] = field(default_factory=dict)
    
    def validate(self, data: Any) -> Tuple[bool, Optional[str]]:
        """
        Validate data against this expectation.
        Returns (is_valid, error_message)
        """
        if self.validation_func:
            try:
                result = self.validation_func(data)
                if isinstance(result, tuple):
                    return result
                return (result, None if result else f"Validation failed for {self.name}")
            except Exception as e:
                return (False, f"Validation error: {str(e)}")
        
        # Default validations based on type
        if self.expectation_type == ExpectationType.NOT_NULL:
            is_valid = data is not None and (not isinstance(data, str) or data.strip() != "")
            return (is_valid, None if is_valid else f"{self.column_name} is null or empty")
        
        return (True, None)


@dataclass
class ExpectationResult:
    """Result of running an expectation"""
    expectation: Expectation
    passed: bool
    error_message: Optional[str] = None
    affected_rows: int = 0
    sample_failures: List[Any] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for storage"""
        return {
            "expectation_name": self.expectation.name,
            "expectation_type": self.expectation.expectation_type.value,
            "table_name": self.expectation.table_name,
            "column_name": self.expectation.column_name,
            "passed": self.passed,
            "error_message": self.error_message,
            "affected_rows": self.affected_rows,
            "severity": self.expectation.severity.value,
            "downstream_impact": self.expectation.downstream_impact,
            "timestamp": self.timestamp.isoformat(),
            "sample_failures": str(self.sample_failures[:5])  # Store first 5
        }


class DataQualityFramework:
    """Main framework for data quality monitoring"""
    
    def __init__(self, db_path: str = "data_quality.db"):
        """Initialize the framework with a database for tracking"""
        self.db_path = db_path
        self.expectations: Dict[str, Expectation] = {}
        self._init_database()
    
    def _init_database(self):
        """Initialize SQLite database for tracking failures"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expectation_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expectation_name TEXT NOT NULL,
                expectation_type TEXT NOT NULL,
                table_name TEXT NOT NULL,
                column_name TEXT,
                passed INTEGER NOT NULL,
                error_message TEXT,
                affected_rows INTEGER DEFAULT 0,
                severity TEXT NOT NULL,
                downstream_impact TEXT,
                timestamp TEXT NOT NULL,
                sample_failures TEXT
            )
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_timestamp 
            ON expectation_results(timestamp)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_expectation_name 
            ON expectation_results(expectation_name)
        """)
        
        conn.commit()
        conn.close()
    
    def add_expectation(self, expectation: Expectation):
        """Register a data quality expectation"""
        self.expectations[expectation.name] = expectation
    
    def run_expectation(self, expectation_name: str, data: Any) -> ExpectationResult:
        """Run a single expectation against data"""
        if expectation_name not in self.expectations:
            raise ValueError(f"Expectation '{expectation_name}' not found")
        
        expectation = self.expectations[expectation_name]
        passed, error_message = expectation.validate(data)
        
        result = ExpectationResult(
            expectation=expectation,
            passed=passed,
            error_message=error_message,
            affected_rows=1 if not passed else 0
        )
        
        self._store_result(result)
        return result
    
    def run_all_expectations(self, data_provider: Callable[[str], Any]) -> List[ExpectationResult]:
        """Run all registered expectations"""
        results = []
        for name, expectation in self.expectations.items():
            try:
                data = data_provider(expectation.table_name)
                result = self.run_expectation(name, data)
                results.append(result)
            except Exception as e:
                result = ExpectationResult(
                    expectation=expectation,
                    passed=False,
                    error_message=f"Error running expectation: {str(e)}"
                )
                self._store_result(result)
                results.append(result)
        
        return results
    
    def _store_result(self, result: ExpectationResult):
        """Store expectation result in database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        result_dict = result.to_dict()
        cursor.execute("""
            INSERT INTO expectation_results 
            (expectation_name, expectation_type, table_name, column_name,
             passed, error_message, affected_rows, severity, downstream_impact,
             timestamp, sample_failures)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            result_dict["expectation_name"],
            result_dict["expectation_type"],
            result_dict["table_name"],
            result_dict["column_name"],
            1 if result_dict["passed"] else 0,
            result_dict["error_message"],
            result_dict["affected_rows"],
            result_dict["severity"],
            result_dict["downstream_impact"],
            result_dict["timestamp"],
            result_dict["sample_failures"]
        ))
        
        conn.commit()
        conn.close()
    
    def get_failure_history(self, expectation_name: Optional[str] = None, 
                           days: int = 30) -> List[Dict]:
        """Get failure history for expectations"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()
        
        if expectation_name:
            cursor.execute("""
                SELECT * FROM expectation_results
                WHERE expectation_name = ? 
                AND passed = 0
                AND timestamp >= ?
                ORDER BY timestamp DESC
            """, (expectation_name, cutoff_date))
        else:
            cursor.execute("""
                SELECT * FROM expectation_results
                WHERE passed = 0
                AND timestamp >= ?
                ORDER BY timestamp DESC
            """, (cutoff_date,))
        
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return results
    
    def get_failure_trends(self, expectation_name: str, days: int = 30) -> Dict:
        """Get failure trends over time for an expectation"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()
        
        cursor.execute("""
            SELECT 
                DATE(timestamp) as date,
                COUNT(*) as total_runs,
                SUM(CASE WHEN passed = 0 THEN 1 ELSE 0 END) as failures,
                SUM(affected_rows) as total_affected_rows
            FROM expectation_results
            WHERE expectation_name = ?
            AND timestamp >= ?
            GROUP BY DATE(timestamp)
            ORDER BY date DESC
        """, (expectation_name, cutoff_date))
        
        trends = []
        for row in cursor.fetchall():
            trends.append({
                "date": row[0],
                "total_runs": row[1],
                "failures": row[2],
                "total_affected_rows": row[3],
                "failure_rate": row[2] / row[1] if row[1] > 0 else 0
            })
        
        conn.close()
        return {"expectation_name": expectation_name, "trends": trends}
    
    def generate_explanation(self, expectation_name: str) -> Dict:
        """Generate explanation of what broke and why it matters"""
        failure_history = self.get_failure_history(expectation_name, days=7)
        trends = self.get_failure_trends(expectation_name, days=30)
        
        if not failure_history:
            return {
                "status": "healthy",
                "message": f"Expectation '{expectation_name}' has no recent failures"
            }
        
        expectation = self.expectations.get(expectation_name)
        if not expectation:
            return {"status": "error", "message": "Expectation not found"}
        
        recent_failures = len([f for f in failure_history 
                              if datetime.fromisoformat(f["timestamp"]) > 
                              datetime.now() - timedelta(days=1)])
        
        total_affected = sum(f.get("affected_rows", 0) for f in failure_history)
        
        explanation = {
            "expectation_name": expectation_name,
            "expectation_type": expectation.expectation_type.value,
            "table": expectation.table_name,
            "column": expectation.column_name,
            "severity": expectation.severity.value,
            "status": "failing",
            "what_broke": expectation.description or f"Data quality check failed for {expectation_name}",
            "why_it_matters": expectation.downstream_impact or self._generate_default_impact(expectation),
            "recent_failures_24h": recent_failures,
            "total_affected_rows_7d": total_affected,
            "failure_trend": self._analyze_trend(trends.get("trends", [])),
            "recommendation": self._generate_recommendation(expectation, trends)
        }
        
        return explanation
    
    def _generate_default_impact(self, expectation: Expectation) -> str:
        """Generate default downstream impact explanation"""
        impacts = {
            ExpectationType.NOT_NULL: f"Missing {expectation.column_name} values will cause errors in downstream analytics and reporting",
            ExpectationType.UNIQUE: f"Duplicate values in {expectation.column_name} will lead to incorrect aggregations and join issues",
            ExpectationType.IN_RANGE: f"Out-of-range values in {expectation.column_name} will produce invalid calculations and misleading insights",
            ExpectationType.MATCHES_PATTERN: f"Invalid format in {expectation.column_name} will break data parsing and integration processes",
        }
        return impacts.get(expectation.expectation_type, 
                          f"Data quality issues in {expectation.table_name} may impact downstream analytics and business decisions")
    
    def _analyze_trend(self, trends: List[Dict]) -> str:
        """Analyze failure trend"""
        if not trends or len(trends) < 2:
            return "insufficient_data"
        
        recent_failure_rate = trends[0].get("failure_rate", 0)
        older_failure_rate = trends[-1].get("failure_rate", 0)
        
        if recent_failure_rate > older_failure_rate * 1.2:
            return "worsening"
        elif recent_failure_rate < older_failure_rate * 0.8:
            return "improving"
        else:
            return "stable"
    
    def _generate_recommendation(self, expectation: Expectation, trends: Dict) -> str:
        """Generate recommendation based on expectation and trends"""
        trend_analysis = self._analyze_trend(trends.get("trends", []))
        
        if trend_analysis == "worsening":
            return f"Urgent: {expectation.severity.value.upper()} severity issue is getting worse. Investigate data source immediately."
        elif expectation.severity == Severity.CRITICAL:
            return f"Critical: This issue blocks downstream processes. Fix immediately."
        else:
            return f"Monitor: Review data source and validation logic. Consider data pipeline improvements."
