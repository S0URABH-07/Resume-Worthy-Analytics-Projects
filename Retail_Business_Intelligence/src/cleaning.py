import pandas as pd
import numpy as np

def clean_and_engineer_retail_data(var):
    print("...[Cleaning]...")
    
    var = var.copy()
    var.columns = var.columns.str.strip()
    
    # 1. Parse chronological dates
    for date_col in ['Orderdate', 'Duedate', 'Shipdate']:
        if date_col in var.columns:
            var[date_col] = pd.to_datetime(var[date_col], errors='coerce')
            
    var = var.dropna(subset=['Orderdate', 'SalesAmount']).sort_values('Orderdate').reset_index(drop=True)
    var['YearMonth'] = var['Orderdate'].dt.to_period('M').astype(str)
    
    if 'Shipdate' in var.columns and 'Orderdate' in var.columns:
        var['Fulfillment_Days'] = (var['Shipdate'] - var['Orderdate']).dt.days
        var['Fulfillment_Days'] = var['Fulfillment_Days'].clip(lower=0) # Handle anomalies
        
    numeric_cols = ['ListPrice', 'OrderQuantity', 'UnitPrice', 'SalesAmount', 'DiscountAmount', 'TaxAmount', 'Freight']
    for col in numeric_cols:
        if col in var.columns:
            var[col] = pd.to_numeric(var[col], errors='coerce').fillna(0)
            
    cat_cols = ['ProductName', 'Color', 'Category', 'Subcategory', 'PromotionName', 'SalesRegion']
    for col in cat_cols:
        if col in var.columns:
            var[col] = var[col].astype(str).str.strip().fillna('Unknown')

    var['Net_Sales'] = var['SalesAmount'] - var['DiscountAmount']
    
    var['Net_Profit'] = var['Net_Sales'] - var['TaxAmount'] - var['Freight']
    
    var['Profit_Margin_%'] = np.where(var['Net_Sales'] > 0, (var['Net_Profit'] / var['Net_Sales']) * 100, 0)
    
    return var