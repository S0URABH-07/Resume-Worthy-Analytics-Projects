import pandas as pd

def perform_fraud_quantifications(var):
    
    total_txns = var.shape[0]
    fraud_cases = var['is_fraud'].sum()
    fraud_ratio = (fraud_cases / total_txns) * 100
    print(f"Aggregate Systemic Records Tracked: {total_txns} Rows")
    print(f"Confirmed Fraud Exploits Flagged: {fraud_cases} entries ({fraud_ratio:.2f}%)")
    
    # Profile category vulnerabilities
    category_risk = var.groupby('category').agg({
        'is_fraud': 'mean',
        'amt': 'mean',
        'trans_num': 'count'
    }).rename(columns={'trans_num': 'Volume', 'is_fraud': 'Risk_Rate'}).sort_values(by='Risk_Rate', ascending=False)
    
    print("\nHigh-Risk Spending Categories Summary Matrix:")
    print(category_risk.head(5))
    
    # Calculate core continuous attribute co-dependencies
    numeric_features = ['amt', 'TransactionHour', 'city_pop', 'Customer_Age', 'is_fraud']
    available_numeric = [col for col in numeric_features if col in var.columns]
    
    return var[available_numeric].corr()