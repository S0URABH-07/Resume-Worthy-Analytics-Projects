import pandas as pd
import numpy as np

def clean_delivery_matrix(var):
    print("[Cleaning] Executing data hygiene and geospatial calculations...")
    
    # 1. Clean String Whitespace & Null Strings
    # This dataset often contains trailing spaces or string-based 'NaN ' values.
    for col in var.columns:
        if var[col].dtype == 'object':
            var[col] = var[col].astype(str).str.strip()
            var[col] = var[col].replace(['NaN', 'nan', 'null', ''], np.nan)
            
    # 2. Datatype Enforcement & Missing Value Resolution
    var['Delivery_person_Age'] = pd.to_numeric(var['Delivery_person_Age'], errors='coerce')
    var['Delivery_person_Age'] = var['Delivery_person_Age'].fillna(var['Delivery_person_Age'].median())
    
    var['Delivery_person_Ratings'] = pd.to_numeric(var['Delivery_person_Ratings'], errors='coerce')
    var['Delivery_person_Ratings'] = var['Delivery_person_Ratings'].fillna(var['Delivery_person_Ratings'].median())
    
    var['multiple_deliveries'] = pd.to_numeric(var['multiple_deliveries'], errors='coerce').fillna(0)
    var['Time_taken(min)'] = pd.to_numeric(var['Time_taken(min)'], errors='coerce')
    
    # Drop rows missing the ultimate prediction target
    var = var.dropna(subset=['Time_taken(min)']).copy()
    
    # 3. Chronological Feature Engineering
    # Extract operational hour from order timestamp
    var['Order_Hour'] = var['Time_Orderd'].astype(str).str.split(':').str[0]
    var['Order_Hour'] = pd.to_numeric(var['Order_Hour'], errors='coerce')
    var['Order_Hour'] = var['Order_Hour'].fillna(var['Order_Hour'].median()).astype(int)
    
    # 4. ADVANCED FEATURE ENGINEERING: Geospatial Haversine Distance (Kilometers)
    # Converts coordinates to actual physical distance separating restaurant and delivery nodes
    def haversine_distance(lat1, lon1, lat2, lon2):
        # Earth's radius in kilometers
        R = 6371.0 
        
        # Convert degrees to radians
        lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arcsin(np.sqrt(a))
        return R * c

    var['Distance_KM'] = haversine_distance(
        var['Restaurant_latitude'].astype(float), var['Restaurant_longitude'].astype(float),
        var['Delivery_location_latitude'].astype(float), var['Delivery_location_longitude'].astype(float)
    )
    
    # Clip any extreme geospatial typos/anomalies
    var['Distance_KM'] = var['Distance_KM'].clip(lower=0.5, upper=50.0)
    
    return var