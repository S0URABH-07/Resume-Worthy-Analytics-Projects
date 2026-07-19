import matplotlib.pyplot as plt
import seaborn as sns

def generate_analytical_plots(var, corr_matrix):
    print("...[Visualization]...")
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams['font.family'] = 'sans-serif'
    
    # Box Plot 
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=var, x='Churn_Label', y='Tenure', hue='Churn_Label', palette='Set2', legend=False)
    plt.title('Customer Retention Profile: Account Tenure Horizons vs Churn Status', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Account Status')
    plt.ylabel('Tenure Length (Months)')
    plt.tight_layout()
    plt.savefig("reports/figures/chart1_tenure_boxplot.png", dpi=300)
    plt.close()
    
    # KDE Continuous Distribution Plot (Support call operational bottlenecks)
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=var, x='Support Calls', hue='Churn_Label', fill=True, common_norm=False, palette='coolwarm', alpha=0.5, linewidth=2)
    plt.title('Operational Friction Profile: Support Call Density Curves vs Churn Status', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Number of Logged Support Calls')
    plt.ylabel('Density Weight')
    plt.tight_layout()
    plt.savefig("reports/figures/chart2_support_calls_kde.png", dpi=300)
    plt.close()
    
    # Heatmap Matrix (Pearson feature covariance interaction map)
    plt.figure(figsize=(11, 9))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, square=True, cbar=False)
    plt.title('Subscriber Behavioral Matrix: Feature Correlation Space Map', fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig("reports/figures/chart3_correlation_matrix.png", dpi=300)
    plt.close()

    # Count Plot (Contractual term vulnerabilities)
    plt.figure(figsize=(10, 6))
    sns.countplot(data=var, x='Contract Length', hue='Churn_Label', palette='viridis', edgecolor='black')
    plt.title('Contract Risk Vectors: Churn Volatility Across Term Brackets', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Contract Length Category')
    plt.ylabel('Account Volumes')
    plt.tight_layout()
    plt.savefig("reports/figures/chart4_contract_length_barplot.png", dpi=300)
    plt.close()

    fig, axes = plt.subplots(2, 2, figsize=(22, 16))
    
    sns.boxplot(data=var, x='Churn_Label', y='Tenure', hue='Churn_Label', palette='Set2', ax=axes[0, 0], legend=False)
    axes[0, 0].set_title('Customer Tenure Lifecycle vs Account Cancellation', fontsize=13, fontweight='bold')
    axes[0, 0].set_xlabel('Account Status')
    axes[0, 0].set_ylabel('Tenure (Months)')
    
    sns.kdeplot(data=var, x='Support Calls', hue='Churn_Label', fill=True, common_norm=False, palette='coolwarm', alpha=0.5, linewidth=2, ax=axes[0, 1])
    axes[0, 1].set_title('Friction Distribution Density (Support Call Footprint)', fontsize=13, fontweight='bold')
    axes[0, 1].set_xlabel('Support Calls')
    
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, square=True, ax=axes[1, 0], cbar=False)
    axes[1, 0].set_title('Customer Behavioral Matrix Covariance Map', fontsize=13, fontweight='bold')
    
    sns.countplot(data=var, x='Contract Length', hue='Churn_Label', palette='viridis', edgecolor='black', ax=axes[1, 1])
    axes[1, 1].set_title('Operational Account Attrition Slices by Contract Category', fontsize=13, fontweight='bold')
    axes[1, 1].set_xlabel('Contract Structure')
    axes[1, 1].set_ylabel('Account Volumes')
    
    plt.tight_layout()
    plt.savefig("reports/figures/credit_card_executive_master_dashboard.png", dpi=300, bbox_inches='tight')
    plt.close()
