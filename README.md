# Data Quality & Reliability Monitoring Framework

A lightweight, production-ready data quality framework that implements expectations/tests, tracks failures over time, and explains what breaks and why it matters.

## Features

### Core Capabilities

- **Expectation System**: Define and implement data quality expectations (not null, unique, range checks, custom validations, etc.)
- **Failure Tracking**: Persistent tracking of data quality failures over time with SQLite backend
- **Trend Analysis**: Analyze failure patterns and trends to identify deteriorating data quality
- **Impact Explanation**: Automatically explains what broke and why it matters to business stakeholders
- **Executive Readiness**: Checklist to ensure metrics are ready for executive reporting
- **Downstream Impact Examples**: Real-world scenarios showing how data issues cascade through systems

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Basic Usage

```python
from data_quality_framework import (
    DataQualityFramework, Expectation, ExpectationType, Severity
)

# Initialize framework
framework = DataQualityFramework()

# Add an expectation
framework.add_expectation(Expectation(
    name="customer_id_not_null",
    expectation_type=ExpectationType.NOT_NULL,
    table_name="transactions",
    column_name="customer_id",
    description="Customer ID must be present for all transactions",
    severity=Severity.CRITICAL,
    downstream_impact="Missing customer IDs prevent revenue attribution and CLV calculations"
))

# Run validation
result = framework.run_expectation("customer_id_not_null", customer_id_value)

# Get explanation of what broke
explanation = framework.generate_explanation("customer_id_not_null")
print(explanation)
```

## Framework Components

### 1. Data Quality Framework (`data_quality_framework.py`)

The core framework that:
- Manages data quality expectations
- Validates data against expectations
- Tracks failures in a SQLite database
- Provides trend analysis
- Generates explanations

**Key Classes:**
- `DataQualityFramework`: Main framework class
- `Expectation`: Represents a data quality check
- `ExpectationResult`: Result of running an expectation
- `ExpectationType`: Types of expectations (NOT_NULL, UNIQUE, IN_RANGE, etc.)
- `Severity`: Impact levels (CRITICAL, HIGH, MEDIUM, LOW)

### 2. Executive Metric Readiness Checklist (`executive_checklist.py`)

A comprehensive checklist ensuring data quality metrics are ready for executive consumption:

- **Data Quality Foundation**: Completeness, freshness, critical failures
- **Metric Accuracy**: Documentation, baselines, validation rules
- **Business Context**: Impact documentation, ownership, alert thresholds
- **Reliability**: Monitoring, tracking, recovery procedures
- **Executive Readiness**: Trend analysis, impact quantification, actionable insights

**Usage:**
```python
from executive_checklist import ExecutiveMetricReadinessChecklist

checklist = ExecutiveMetricReadinessChecklist()
checklist.evaluate(framework_results)
checklist.print_report()
```

### 3. Downstream Impact Examples (`downstream_impact_examples.py`)

Real-world scenarios demonstrating how data quality issues cascade through systems:

- E-commerce revenue reporting failures
- Financial reporting inaccuracies
- Real-time inventory management issues
- Healthcare analytics errors
- Customer data integration problems
- Multi-system data warehouse integrity issues

Each example includes:
- Data issue description
- Immediate impact
- Downstream effects
- Business cost quantification
- Affected systems
- Prevention strategies

**Usage:**
```python
from downstream_impact_examples import DownstreamImpactExamples

examples = DownstreamImpactExamples()
examples.print_all_examples()
```

## Example Scenarios

### Scenario 1: Missing Customer Data

**Issue**: Customer ID field contains 15% null values

**Impact**:
- Revenue reports cannot attribute sales to customers
- CLV calculations are inaccurate
- Marketing cannot identify high-value customers
- Customer support cannot link tickets to purchases

**Business Cost**: $50K/month in lost marketing efficiency

**Solution**: Implement NOT_NULL expectation with automatic alerts

### Scenario 2: Stale Inventory Data

**Issue**: Inventory levels not updated for 48 hours

**Impact**:
- Customers order out-of-stock items
- Supply chain makes incorrect decisions
- Sales team promises unavailable products
- Customer satisfaction drops

**Business Cost**: $200K in lost sales and operational inefficiency

**Solution**: Implement TIMELINESS expectation with SLA monitoring

## API Reference

### DataQualityFramework

#### Methods

- `add_expectation(expectation: Expectation)`: Register a data quality expectation
- `run_expectation(name: str, data: Any) -> ExpectationResult`: Run a single expectation
- `run_all_expectations(data_provider: Callable) -> List[ExpectationResult]`: Run all expectations
- `get_failure_history(expectation_name: Optional[str], days: int) -> List[Dict]`: Get failure history
- `get_failure_trends(expectation_name: str, days: int) -> Dict`: Get failure trends over time
- `generate_explanation(expectation_name: str) -> Dict`: Generate explanation of what broke

### Expectation Types

- `NOT_NULL`: Ensures values are not null or empty
- `UNIQUE`: Ensures values are unique
- `IN_RANGE`: Ensures values are within a specified range
- `MATCHES_PATTERN`: Ensures values match a regex pattern
- `CUSTOM`: Custom validation function
- `REFERENTIAL_INTEGRITY`: Ensures foreign key relationships
- `COMPLETENESS`: Ensures data completeness thresholds
- `ACCURACY`: Validates data accuracy
- `CONSISTENCY`: Ensures data consistency
- `TIMELINESS`: Validates data freshness

## Running Examples

See `example_usage.py` for a complete demonstration:

```bash
python example_usage.py
```

This will:
1. Create sample expectations
2. Run validations against sample data
3. Generate explanations
4. Show failure tracking
5. Display executive checklist
6. Show downstream impact examples

## Database Schema

The framework uses SQLite to track expectation results:

```sql
CREATE TABLE expectation_results (
    id INTEGER PRIMARY KEY,
    expectation_name TEXT NOT NULL,
    expectation_type TEXT NOT NULL,
    table_name TEXT NOT NULL,
    column_name TEXT,
    passed INTEGER NOT NULL,
    error_message TEXT,
    affected_rows INTEGER,
    severity TEXT NOT NULL,
    downstream_impact TEXT,
    timestamp TEXT NOT NULL,
    sample_failures TEXT
)
```

## Best Practices

1. **Define Clear Expectations**: Each expectation should have a clear description and business justification
2. **Set Appropriate Severity**: Use CRITICAL for blocking issues, HIGH for significant impact
3. **Document Downstream Impact**: Always include how failures affect business operations
4. **Monitor Trends**: Regularly review failure trends to catch deteriorating data quality early
5. **Use Executive Checklist**: Ensure metrics meet readiness criteria before executive reporting
6. **Quantify Business Impact**: Include cost estimates in downstream impact descriptions

## Use Cases

- **Data Pipeline Monitoring**: Validate data quality at each stage of ETL pipelines
- **Analytics Dashboard Validation**: Ensure metrics are accurate before executive reporting
- **Data Warehouse Quality**: Maintain data quality standards in data warehouses
- **Real-time Data Validation**: Validate streaming data before it reaches downstream systems
- **Compliance Monitoring**: Ensure data meets regulatory requirements

## Architecture

The framework is designed to be:
- **Lightweight**: Minimal dependencies, easy to integrate
- **Extensible**: Easy to add custom expectation types
- **Persistent**: Tracks history for trend analysis
- **Business-Focused**: Explains impact in business terms
- **Production-Ready**: Includes error handling and logging

## Contributing

This is a resume project demonstrating data quality engineering capabilities. Key highlights:

- Implements a complete data quality framework
- Tracks failures over time with trend analysis
- Explains business impact of data issues
- Includes executive readiness checklist
- Provides real-world impact examples

## License

This project is for demonstration purposes.
