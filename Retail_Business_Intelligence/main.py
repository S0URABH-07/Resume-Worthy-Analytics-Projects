import os
from src.data_loader import load_retail_data
from src.cleaning import clean_and_engineer_retail_data
from src.analysis import compute_executive_kpis
from src.visualization import generate_retail_visualizations

def run_pipeline():
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("reports/figures", exist_ok=True)
    
    raw_file_path = "data/raw/retail_sales_dataset.csv"
    raw_df = load_retail_data(raw_file_path)
    
    cleaned_df = clean_and_engineer_retail_data(raw_df)
    
    monthly_kpis = compute_executive_kpis(cleaned_df)
    
    generate_retail_visualizations(cleaned_df, monthly_kpis)
    
    processed_file_path = "data/processed/cleaned_retail_data.csv"
    cleaned_df.to_csv(processed_file_path, index=False)


if __name__ == "__main__":
    run_pipeline()