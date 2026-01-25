"""
Examples of Downstream Impact When Data Breaks

Real-world scenarios showing how data quality issues affect business operations.
"""

from typing import Dict, List
from dataclasses import dataclass


@dataclass
class ImpactExample:
    """An example of downstream impact"""
    scenario: str
    data_issue: str
    immediate_impact: str
    downstream_effects: List[str]
    business_cost: str
    affected_systems: List[str]
    prevention_strategy: str


class DownstreamImpactExamples:
    """Collection of downstream impact examples"""
    
    def __init__(self):
        self.examples: List[ImpactExample] = []
        self._load_examples()
    
    def _load_examples(self):
        """Load example scenarios"""
        
        # Example 1: Missing Customer Data
        self.examples.append(ImpactExample(
            scenario="E-commerce Revenue Reporting",
            data_issue="Customer ID field contains 15% null values in transactions table",
            immediate_impact="Revenue reports cannot attribute sales to specific customers",
            downstream_effects=[
                "Customer lifetime value (CLV) calculations are inaccurate",
                "Marketing attribution models fail to identify high-value customers",
                "Customer segmentation reports exclude 15% of revenue",
                "Personalization engine cannot recommend products to affected customers",
                "Customer support cannot link support tickets to purchase history"
            ],
            business_cost="Estimated $50K/month in lost marketing efficiency and customer retention",
            affected_systems=[
                "Business Intelligence Dashboard",
                "Marketing Automation Platform",
                "Customer Relationship Management (CRM)",
                "Recommendation Engine",
                "Customer Support System"
            ],
            prevention_strategy="Implement NOT_NULL expectation on customer_id with automatic data pipeline alerts"
        ))
        
        # Example 2: Duplicate Records
        self.examples.append(ImpactExample(
            scenario="Financial Reporting",
            data_issue="Duplicate invoice records in accounting system (5% duplication rate)",
            immediate_impact="Revenue appears inflated by 5% in financial reports",
            downstream_effects=[
                "Quarterly earnings reports show incorrect revenue figures",
                "Tax filings contain inaccurate financial data",
                "Investor relations materials present wrong metrics",
                "Budget forecasting models use incorrect baseline numbers",
                "Compliance audits flag discrepancies"
            ],
            business_cost="Risk of regulatory penalties, investor trust issues, and incorrect business decisions",
            affected_systems=[
                "General Ledger System",
                "Financial Reporting Dashboard",
                "Tax Preparation Software",
                "Investor Relations Portal",
                "Compliance Monitoring System"
            ],
            prevention_strategy="Implement UNIQUE expectation on invoice_id with referential integrity checks"
        ))
        
        # Example 3: Data Freshness
        self.examples.append(ImpactExample(
            scenario="Real-time Inventory Management",
            data_issue="Inventory levels not updated for 48 hours due to ETL pipeline failure",
            immediate_impact="Inventory dashboard shows stale data",
            downstream_effects=[
                "Customers order out-of-stock items, leading to cancellations",
                "Supply chain team makes incorrect procurement decisions",
                "Sales team promises products that are unavailable",
                "Warehouse operations become inefficient",
                "Customer satisfaction scores drop due to order cancellations"
            ],
            business_cost="$200K in lost sales, increased customer churn, operational inefficiency",
            affected_systems=[
                "E-commerce Platform",
                "Order Management System",
                "Supply Chain Planning",
                "Customer Service Portal",
                "Warehouse Management System"
            ],
            prevention_strategy="Implement TIMELINESS expectation with SLA monitoring (data must be < 1 hour old)"
        ))
        
        # Example 4: Data Accuracy
        self.examples.append(ImpactExample(
            scenario="Healthcare Analytics",
            data_issue="Patient age field contains invalid values (negative numbers, >150)",
            immediate_impact="Patient demographics reports are incorrect",
            downstream_effects=[
                "Clinical decision support systems make incorrect recommendations",
                "Medication dosing calculations fail for affected patients",
                "Epidemiological studies produce invalid results",
                "Insurance claims processing errors occur",
                "Regulatory reporting contains inaccurate patient data"
            ],
            business_cost="Patient safety risks, regulatory compliance violations, research validity issues",
            affected_systems=[
                "Electronic Health Records (EHR)",
                "Clinical Decision Support",
                "Pharmacy Management System",
                "Insurance Claims Processing",
                "Research Analytics Platform"
            ],
            prevention_strategy="Implement IN_RANGE expectation (age between 0-150) with data validation at source"
        ))
        
        # Example 5: Format Consistency
        self.examples.append(ImpactExample(
            scenario="Customer Data Integration",
            data_issue="Email addresses in inconsistent formats (missing @, spaces, invalid domains)",
            immediate_impact="Email marketing campaigns fail to send to 20% of customer base",
            downstream_effects=[
                "Customer communication is disrupted",
                "Password reset emails cannot be delivered",
                "Newsletter subscriptions fail",
                "Customer engagement metrics are inaccurate",
                "Marketing ROI calculations are skewed"
            ],
            business_cost="$30K/month in lost marketing reach, reduced customer engagement, support ticket increase",
            affected_systems=[
                "Email Marketing Platform",
                "Customer Authentication System",
                "Newsletter Management",
                "Marketing Analytics Dashboard",
                "Customer Support System"
            ],
            prevention_strategy="Implement MATCHES_PATTERN expectation for email format with data cleansing pipeline"
        ))
        
        # Example 6: Referential Integrity
        self.examples.append(ImpactExample(
            scenario="Multi-system Data Warehouse",
            data_issue="Product IDs in sales table reference non-existent products (orphaned records)",
            immediate_impact="Sales reports cannot join with product catalog",
            downstream_effects=[
                "Product performance analytics are incomplete",
                "Revenue cannot be broken down by product category",
                "Inventory planning uses incorrect sales data",
                "Marketing cannot analyze which products drive revenue",
                "Executive dashboards show incomplete metrics"
            ],
            business_cost="Inability to make data-driven product decisions, estimated $100K in opportunity cost",
            affected_systems=[
                "Data Warehouse",
                "Business Intelligence Platform",
                "Product Analytics Dashboard",
                "Inventory Planning System",
                "Executive Reporting Suite"
            ],
            prevention_strategy="Implement REFERENTIAL_INTEGRITY expectation ensuring all product_ids exist in products table"
        ))
    
    def get_example(self, scenario: str = None) -> List[ImpactExample]:
        """Get impact examples, optionally filtered by scenario"""
        if scenario:
            return [ex for ex in self.examples if scenario.lower() in ex.scenario.lower()]
        return self.examples
    
    def print_example(self, example: ImpactExample):
        """Print a formatted impact example"""
        print("=" * 80)
        print(f"SCENARIO: {example.scenario}")
        print("=" * 80)
        print(f"\n📊 DATA ISSUE:")
        print(f"   {example.data_issue}")
        
        print(f"\n⚡ IMMEDIATE IMPACT:")
        print(f"   {example.immediate_impact}")
        
        print(f"\n🔗 DOWNSTREAM EFFECTS:")
        for i, effect in enumerate(example.downstream_effects, 1):
            print(f"   {i}. {effect}")
        
        print(f"\n💰 BUSINESS COST:")
        print(f"   {example.business_cost}")
        
        print(f"\n🖥️  AFFECTED SYSTEMS:")
        for system in example.affected_systems:
            print(f"   • {system}")
        
        print(f"\n🛡️  PREVENTION STRATEGY:")
        print(f"   {example.prevention_strategy}")
        print("\n" + "=" * 80 + "\n")
    
    def print_all_examples(self):
        """Print all impact examples"""
        for example in self.examples:
            self.print_example(example)
    
    def generate_report(self) -> str:
        """Generate a markdown report of all examples"""
        report = "# Downstream Impact Examples\n\n"
        report += "This document illustrates real-world scenarios of how data quality issues cascade through systems.\n\n"
        
        for i, example in enumerate(self.examples, 1):
            report += f"## Example {i}: {example.scenario}\n\n"
            report += f"**Data Issue:** {example.data_issue}\n\n"
            report += f"**Immediate Impact:** {example.immediate_impact}\n\n"
            report += "**Downstream Effects:**\n"
            for effect in example.downstream_effects:
                report += f"- {effect}\n"
            report += f"\n**Business Cost:** {example.business_cost}\n\n"
            report += "**Affected Systems:**\n"
            for system in example.affected_systems:
                report += f"- {system}\n"
            report += f"\n**Prevention Strategy:** {example.prevention_strategy}\n\n"
            report += "---\n\n"
        
        return report
