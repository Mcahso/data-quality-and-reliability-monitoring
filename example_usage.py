"""
Example Usage of the Data Quality Framework

Demonstrates how to use the framework with realistic scenarios.
"""

from data_quality_framework import (
    DataQualityFramework, Expectation, ExpectationType, Severity
)
from executive_checklist import ExecutiveMetricReadinessChecklist
from downstream_impact_examples import DownstreamImpactExamples
import pandas as pd
from datetime import datetime


def create_sample_expectations(framework: DataQualityFramework):
    """Create sample data quality expectations"""
    
    # Example 1: Customer ID must not be null
    framework.add_expectation(Expectation(
        name="customer_id_not_null",
        expectation_type=ExpectationType.NOT_NULL,
        table_name="transactions",
        column_name="customer_id",
        description="Customer ID must be present for all transactions",
        severity=Severity.CRITICAL,
        downstream_impact="Missing customer IDs prevent revenue attribution, CLV calculations, and customer segmentation. Estimated impact: $50K/month in lost marketing efficiency."
    ))
    
    # Example 2: Email format validation
    def validate_email(email):
        import re
        if email is None or email == "":
            return False, "Email is null or empty"
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        is_valid = bool(re.match(pattern, email.strip()))
        return (is_valid, None if is_valid else f"Invalid email format: {email}")
    
    framework.add_expectation(Expectation(
        name="customer_email_valid_format",
        expectation_type=ExpectationType.CUSTOM,
        table_name="customers",
        column_name="email",
        description="Email addresses must be in valid format",
        severity=Severity.HIGH,
        downstream_impact="Invalid email formats prevent email marketing campaigns, password resets, and customer communications. Estimated impact: $30K/month in lost reach.",
        validation_func=validate_email
    ))
    
    # Example 3: Product ID referential integrity
    def validate_product_exists(product_id, products_table):
        # In real implementation, this would check against actual products table
        valid_products = [1, 2, 3, 4, 5]  # Mock valid product IDs
        exists = product_id in valid_products
        return (exists, None if exists else f"Product ID {product_id} does not exist in products table")
    
    framework.add_expectation(Expectation(
        name="product_id_referential_integrity",
        expectation_type=ExpectationType.REFERENTIAL_INTEGRITY,
        table_name="sales",
        column_name="product_id",
        description="All product IDs must reference existing products",
        severity=Severity.HIGH,
        downstream_impact="Orphaned product IDs prevent product performance analytics, revenue breakdowns, and inventory planning. Estimated impact: $100K in opportunity cost.",
        validation_func=lambda x: validate_product_exists(x, None)
    ))
    
    # Example 4: Age in valid range
    def validate_age(age):
        if age is None:
            return False, "Age is null"
        try:
            age_int = int(age)
            is_valid = 0 <= age_int <= 150
            return (is_valid, None if is_valid else f"Age {age_int} is out of valid range (0-150)")
        except (ValueError, TypeError):
            return False, f"Age '{age}' is not a valid number"
    
    framework.add_expectation(Expectation(
        name="customer_age_in_range",
        expectation_type=ExpectationType.IN_RANGE,
        table_name="customers",
        column_name="age",
        description="Customer age must be between 0 and 150",
        severity=Severity.MEDIUM,
        downstream_impact="Invalid age values cause demographic analysis errors and incorrect customer segmentation.",
        validation_func=validate_age
    ))
    
    # Example 5: Timeliness check (data freshness)
    def validate_data_freshness(last_updated):
        if last_updated is None:
            return False, "Last updated timestamp is null"
        try:
            if isinstance(last_updated, str):
                last_updated = datetime.fromisoformat(last_updated)
            hours_old = (datetime.now() - last_updated).total_seconds() / 3600
            is_valid = hours_old < 24
            return (is_valid, None if is_valid else f"Data is {hours_old:.1f} hours old (exceeds 24 hour threshold)")
        except Exception as e:
            return False, f"Error parsing timestamp: {str(e)}"
    
    framework.add_expectation(Expectation(
        name="inventory_data_freshness",
        expectation_type=ExpectationType.TIMELINESS,
        table_name="inventory",
        column_name="last_updated",
        description="Inventory data must be updated within last 24 hours",
        severity=Severity.CRITICAL,
        downstream_impact="Stale inventory data causes customers to order out-of-stock items, leading to cancellations and lost sales. Estimated impact: $200K/month.",
        validation_func=validate_data_freshness
    ))


def simulate_data_validation(framework: DataQualityFramework):
    """Simulate running validations against sample data"""
    
    print("=" * 80)
    print("RUNNING DATA QUALITY VALIDATIONS")
    print("=" * 80)
    
    # Simulate data provider
    def data_provider(table_name):
        # In real implementation, this would fetch from actual data source
        sample_data = {
            "transactions": [
                {"customer_id": 1, "amount": 100},
                {"customer_id": None, "amount": 50},  # This should fail
                {"customer_id": 2, "amount": 200},
            ],
            "customers": [
                {"email": "valid@example.com", "age": 30},
                {"email": "invalid-email", "age": 30},  # This should fail
                {"email": "another@test.com", "age": 200},  # This should fail
            ],
            "sales": [
                {"product_id": 1, "quantity": 10},
                {"product_id": 999, "quantity": 5},  # This should fail (doesn't exist)
            ],
            "inventory": [
                {"last_updated": datetime.now().isoformat()},
                {"last_updated": (datetime.now() - pd.Timedelta(hours=30)).isoformat()},  # This should fail
            ]
        }
        return sample_data.get(table_name, [])
    
    # Run validations
    results = framework.run_all_expectations(data_provider)
    
    # Print results
    for result in results:
        status = "✓ PASS" if result.passed else "✗ FAIL"
        print(f"\n{status} - {result.expectation.name}")
        print(f"  Table: {result.expectation.table_name}")
        print(f"  Severity: {result.expectation.severity.value}")
        if not result.passed:
            print(f"  Error: {result.error_message}")
            print(f"  Impact: {result.expectation.downstream_impact}")
    
    return results


def demonstrate_explanations(framework: DataQualityFramework):
    """Demonstrate the explanation system"""
    
    print("\n" + "=" * 80)
    print("GENERATING EXPLANATIONS")
    print("=" * 80)
    
    for expectation_name in framework.expectations.keys():
        explanation = framework.generate_explanation(expectation_name)
        
        print(f"\n📋 {explanation['expectation_name']}")
        print(f"   Status: {explanation['status']}")
        if explanation['status'] == 'failing':
            print(f"   What Broke: {explanation['what_broke']}")
            print(f"   Why It Matters: {explanation['why_it_matters']}")
            print(f"   Recent Failures (24h): {explanation['recent_failures_24h']}")
            print(f"   Trend: {explanation['failure_trend']}")
            print(f"   Recommendation: {explanation['recommendation']}")


def demonstrate_failure_tracking(framework: DataQualityFramework):
    """Demonstrate failure tracking over time"""
    
    print("\n" + "=" * 80)
    print("FAILURE TRACKING OVER TIME")
    print("=" * 80)
    
    # Get failure history
    failure_history = framework.get_failure_history(days=7)
    
    if failure_history:
        print(f"\nTotal failures in last 7 days: {len(failure_history)}")
        print("\nRecent Failures:")
        for failure in failure_history[:5]:  # Show first 5
            print(f"  • {failure['expectation_name']} - {failure['timestamp']}")
            print(f"    Severity: {failure['severity']}")
            print(f"    Impact: {failure['downstream_impact']}")
    else:
        print("\nNo failures in the last 7 days!")
    
    # Get trends for a specific expectation
    if framework.expectations:
        first_expectation = list(framework.expectations.keys())[0]
        trends = framework.get_failure_trends(first_expectation, days=30)
        print(f"\nTrend Analysis for '{first_expectation}':")
        if trends.get('trends'):
            for trend in trends['trends'][:7]:  # Show last week
                print(f"  {trend['date']}: {trend['failures']}/{trend['total_runs']} failures "
                      f"({trend['failure_rate']*100:.1f}%)")


def main():
    """Main demonstration function"""
    
    # Initialize framework
    framework = DataQualityFramework(db_path="example_data_quality.db")
    
    # Create expectations
    print("Setting up data quality expectations...")
    create_sample_expectations(framework)
    
    # Run validations
    results = simulate_data_validation(framework)
    
    # Demonstrate explanations
    demonstrate_explanations(framework)
    
    # Demonstrate failure tracking
    demonstrate_failure_tracking(framework)
    
    # Executive checklist
    print("\n" + "=" * 80)
    print("EXECUTIVE METRIC READINESS CHECKLIST")
    print("=" * 80)
    
    checklist = ExecutiveMetricReadinessChecklist()
    framework_results = {
        "has_completeness_checks": True,
        "has_timeliness_checks": True,
        "critical_failures_7d": sum(1 for r in results if not r.passed and r.expectation.severity == Severity.CRITICAL),
        "has_tracking": True,
        "has_trends": True
    }
    checklist.evaluate(framework_results)
    checklist.print_report()
    
    # Downstream impact examples
    print("\n" + "=" * 80)
    print("DOWNSTREAM IMPACT EXAMPLES")
    print("=" * 80)
    
    impact_examples = DownstreamImpactExamples()
    print("\nShowing first example:")
    impact_examples.print_example(impact_examples.examples[0])
    
    print(f"\nTotal examples available: {len(impact_examples.examples)}")
    print("Run impact_examples.print_all_examples() to see all scenarios")


if __name__ == "__main__":
    main()
