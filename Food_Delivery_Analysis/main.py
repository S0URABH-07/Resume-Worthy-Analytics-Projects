import os
from src.data_loader import load_delivery_ledger
from src.cleaning import clean_delivery_matrix
from src.analysis import compute_operational_kpis
from src.visualization import build_reporting_graphics

def run_pipeline():

    print("[Pipeline] Initializing modular workspace folders...")
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("reports/figures", exist_ok=True)

    # 1. Ingestion
    raw_file = "data/raw/food_delivery_orders.csv"
    raw_var = load_delivery_ledger(raw_file)
    
    # 2. Hygiene Cleanse
    cleaned_var = clean_delivery_matrix(raw_var)
    
    # 3. Compute Complex Analytics Matrix
    correlation_space = compute_operational_kpis(cleaned_var)
    
    # 4. Fire Visualization Export Suite
    build_reporting_graphics(cleaned_var, correlation_space)
    
    # 5. Processed CSV output check
    cleaned_var.to_csv("data/processed/cleaned_delivery_orders.csv", index=False)

if __name__ == "__main__":
    run_pipeline()