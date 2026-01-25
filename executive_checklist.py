"""
Executive Metric Readiness Checklist

A checklist to ensure data quality metrics are ready for executive reporting.
"""

from dataclasses import dataclass
from typing import List, Dict
from enum import Enum


class ChecklistStatus(Enum):
    """Status of checklist items"""
    PASS = "pass"
    FAIL = "fail"
    WARNING = "warning"
    NOT_APPLICABLE = "n/a"


@dataclass
class ChecklistItem:
    """A single checklist item"""
    category: str
    item: str
    description: str
    status: ChecklistStatus
    notes: str = ""


class ExecutiveMetricReadinessChecklist:
    """Checklist for ensuring metrics are ready for executive consumption"""
    
    def __init__(self):
        self.items: List[ChecklistItem] = []
        self._initialize_checklist()
    
    def _initialize_checklist(self):
        """Initialize the standard checklist items"""
        checklist_data = [
            # Data Quality Foundation
            ("Data Quality Foundation", 
             "Data completeness > 95%",
             "At least 95% of expected records are present and non-null",
             ChecklistStatus.PASS),
            
            ("Data Quality Foundation",
             "Data freshness < 24 hours",
             "Data is updated within 24 hours of source system changes",
             ChecklistStatus.PASS),
            
            ("Data Quality Foundation",
             "No critical data quality failures in last 7 days",
             "No severity-critical expectations have failed in the past week",
             ChecklistStatus.PASS),
            
            # Metric Accuracy
            ("Metric Accuracy",
             "Metric definitions documented",
             "Clear documentation of how metrics are calculated",
             ChecklistStatus.PASS),
            
            ("Metric Accuracy",
             "Historical baseline established",
             "Historical data available to establish normal ranges",
             ChecklistStatus.PASS),
            
            ("Metric Accuracy",
             "Validation rules implemented",
             "Automated checks ensure metric calculations are correct",
             ChecklistStatus.PASS),
            
            # Business Context
            ("Business Context",
             "Downstream impact documented",
             "Clear understanding of how data issues affect business decisions",
             ChecklistStatus.PASS),
            
            ("Business Context",
             "Owner assigned",
             "Data steward or team responsible for metric quality",
             ChecklistStatus.PASS),
            
            ("Business Context",
             "Alert thresholds defined",
             "Clear thresholds for when to escalate issues",
             ChecklistStatus.PASS),
            
            # Reliability
            ("Reliability",
             "Monitoring in place",
             "Automated monitoring tracks metric health continuously",
             ChecklistStatus.PASS),
            
            ("Reliability",
             "Failure tracking implemented",
             "System tracks and trends failures over time",
             ChecklistStatus.PASS),
            
            ("Reliability",
             "Recovery procedures documented",
             "Clear procedures for responding to data quality issues",
             ChecklistStatus.PASS),
            
            # Executive Readiness
            ("Executive Readiness",
             "Trend analysis available",
             "Can show trends over time, not just point-in-time status",
             ChecklistStatus.PASS),
            
            ("Executive Readiness",
             "Impact quantification",
             "Can quantify business impact of data quality issues",
             ChecklistStatus.PASS),
            
            ("Executive Readiness",
             "Actionable insights",
             "Reports include recommendations, not just problems",
             ChecklistStatus.PASS),
        ]
        
        for category, item, description, status in checklist_data:
            self.items.append(ChecklistItem(
                category=category,
                item=item,
                description=description,
                status=status
            ))
    
    def evaluate(self, framework_results: Dict) -> List[ChecklistItem]:
        """Evaluate checklist based on framework results"""
        # Update checklist based on actual framework state
        for item in self.items:
            if "Data completeness" in item.item:
                # Check if completeness expectations exist
                item.status = ChecklistStatus.PASS if framework_results.get("has_completeness_checks") else ChecklistStatus.FAIL
            
            elif "Data freshness" in item.item:
                # Check if timeliness expectations exist
                item.status = ChecklistStatus.PASS if framework_results.get("has_timeliness_checks") else ChecklistStatus.WARNING
            
            elif "No critical data quality failures" in item.item:
                critical_failures = framework_results.get("critical_failures_7d", 0)
                item.status = ChecklistStatus.PASS if critical_failures == 0 else ChecklistStatus.FAIL
                item.notes = f"{critical_failures} critical failures in last 7 days"
            
            elif "Failure tracking implemented" in item.item:
                item.status = ChecklistStatus.PASS if framework_results.get("has_tracking") else ChecklistStatus.FAIL
            
            elif "Trend analysis available" in item.item:
                item.status = ChecklistStatus.PASS if framework_results.get("has_trends") else ChecklistStatus.FAIL
        
        return self.items
    
    def get_summary(self) -> Dict:
        """Get summary of checklist status"""
        by_category = {}
        for item in self.items:
            if item.category not in by_category:
                by_category[item.category] = {"pass": 0, "fail": 0, "warning": 0, "n/a": 0}
            
            status_key = item.status.value
            by_category[item.category][status_key] = by_category[item.category].get(status_key, 0) + 1
        
        total_items = len(self.items)
        passed = sum(1 for item in self.items if item.status == ChecklistStatus.PASS)
        failed = sum(1 for item in self.items if item.status == ChecklistStatus.FAIL)
        warnings = sum(1 for item in self.items if item.status == ChecklistStatus.WARNING)
        
        readiness_score = (passed / total_items) * 100 if total_items > 0 else 0
        
        return {
            "readiness_score": readiness_score,
            "total_items": total_items,
            "passed": passed,
            "failed": failed,
            "warnings": warnings,
            "by_category": by_category,
            "is_ready": readiness_score >= 80 and failed == 0
        }
    
    def print_report(self):
        """Print a formatted checklist report"""
        summary = self.get_summary()
        
        print("=" * 80)
        print("EXECUTIVE METRIC READINESS CHECKLIST")
        print("=" * 80)
        print(f"\nOverall Readiness Score: {summary['readiness_score']:.1f}%")
        print(f"Status: {'✓ READY' if summary['is_ready'] else '✗ NOT READY'}")
        print(f"\nBreakdown: {summary['passed']} Pass | {summary['failed']} Fail | {summary['warnings']} Warning")
        
        current_category = None
        for item in self.items:
            if item.category != current_category:
                current_category = item.category
                print(f"\n{'─' * 80}")
                print(f"{current_category.upper()}")
                print(f"{'─' * 80}")
            
            status_symbol = {
                ChecklistStatus.PASS: "✓",
                ChecklistStatus.FAIL: "✗",
                ChecklistStatus.WARNING: "⚠",
                ChecklistStatus.NOT_APPLICABLE: "○"
            }.get(item.status, "?")
            
            print(f"  {status_symbol} {item.item}")
            if item.notes:
                print(f"    Note: {item.notes}")
        
        print("\n" + "=" * 80)
