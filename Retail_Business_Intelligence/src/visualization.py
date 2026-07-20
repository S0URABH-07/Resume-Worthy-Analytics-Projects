import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_retail_visualizations(var, monthly_kpis):
    print("...[Visualization]...")
    
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams['font.family'] = 'sans-serif'
    
    output_dir = "reports/figures"
    os.makedirs(output_dir, exist_ok=True)
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_kpis, x='YearMonth', y='Net_Sales', label='Net Sales ($)', color='navy', marker='o', linewidth=2)
    sns.lineplot(data=monthly_kpis, x='YearMonth', y='Net_Profit', label='Net Profit ($)', color='forestgreen', marker='s', linewidth=2)
    plt.title('Financial Trajectory: Monthly Net Sales vs Net Profit', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Year-Month')
    plt.ylabel('Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "chart1_revenue_profit_trend.png"), dpi=300)
    plt.close()
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=var, x='SalesRegion', y='Net_Sales', hue='Category', palette='Set2', errorbar=None)
    plt.title('Regional Market Share: Net Sales Breakdown Across Product Categories', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Sales Region')
    plt.ylabel('Net Sales ($)')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "chart2_regional_category_sales.png"), dpi=300)
    plt.close()
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=monthly_kpis, x='YearMonth', y='OrderNumber', palette='Blues_d')
    plt.title('Order Trajectory: Monthly Unique Orders Processed', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Year-Month')
    plt.ylabel('Unique Orders')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "chart3_monthly_customer_growth.png"), dpi=300)
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=var, x='Category', y='Profit_Margin_%', palette='viridis')
    plt.title('Margin Health Analysis: Profit Margin Percentage Distribution Across Categories', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Product Category')
    plt.ylabel('Profit Margin (%)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "chart4_category_profit_margins.png"), dpi=300)
    plt.close()
    
    fig, axes = plt.subplots(2, 2, figsize=(22, 16))
    
    sns.lineplot(data=monthly_kpis, x='YearMonth', y='Net_Sales', label='Net Sales ($)', ax=axes[0, 0], color='navy', marker='o', linewidth=2)
    sns.lineplot(data=monthly_kpis, x='YearMonth', y='Net_Profit', label='Net Profit ($)', ax=axes[0, 0], color='forestgreen', marker='s', linewidth=2)
    axes[0, 0].set_title('Financial Trajectory: Monthly Net Sales vs Net Profit', fontsize=13, fontweight='bold', pad=15)
    axes[0, 0].set_ylabel('Amount ($)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    sns.barplot(data=var, x='SalesRegion', y='Net_Sales', hue='Category', palette='Set2', errorbar=None, ax=axes[0, 1])
    axes[0, 1].set_title('Regional Sales Breakdown Across Product Categories', fontsize=13, fontweight='bold', pad=15)
    axes[0, 1].set_ylabel('Net Sales ($)')
    axes[0, 1].tick_params(axis='x', rotation=30)
    
    sns.barplot(data=monthly_kpis, x='YearMonth', y='OrderNumber', palette='Blues_d', ax=axes[1, 0])
    axes[1, 0].set_title('Order Trajectory: Monthly Unique Orders Processed', fontsize=13, fontweight='bold', pad=15)
    axes[1, 0].set_ylabel('Unique Orders')
    axes[1, 0].tick_params(axis='x', rotation=45)
    
    sns.boxplot(data=var, x='Category', y='Profit_Margin_%', palette='viridis', ax=axes[1, 1])
    axes[1, 1].set_title('Profit Margin Distribution Across Categories', fontsize=13, fontweight='bold', pad=15)
    axes[1, 1].set_ylabel('Profit Margin (%)')
    
    plt.tight_layout()
    dashboard_path = os.path.join(output_dir, "retail_executive_master_dashboard.png")
    plt.savefig(dashboard_path, dpi=300, bbox_inches='tight')
    plt.close()
    
