import pandas as pd

def compute_retention_kpis(var):

    total_subscribers = var.shape[0]
    churned_count = var['Churn'].sum()
    global_churn_rate = (churned_count / total_subscribers) * 100
    
    print(f"Aggregate Customer Ledger Tracked: {total_subscribers} Accounts")
    print(f"Cancelled Portfolio Subscriptions: {churned_count} Flags")
    print(f"Global Systemic Portfolio Attrition Rate: {global_churn_rate:.2f}%")
    
    contract_risk = var.groupby('Contract Length').agg({
        'Churn': 'mean',
        'Customer_Friction_Score': 'mean',
        'CustomerID': 'count'
    }).rename(columns={'CustomerID': 'Volume', 'Churn': 'Churn_Probability'}).sort_values(by='Churn_Probability', ascending=False)
    
    contract_risk['Churn_Probability'] *= 100
    print("\nContractual Agreement Term Risk Profiles:")
    print(contract_risk)
    
    numeric_features = ['Age', 'Tenure', 'Usage Frequency', 'Support Calls', 'Payment Delay', 'Total Spend', 'Last Interaction', 'Customer_Friction_Score', 'Churn']
    available_numeric = [col for col in numeric_features if col in var.columns]
    
    return var[available_numeric].corr()