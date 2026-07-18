import pandas as pd

def compute_operational_kpis(var):
    total_orders = var.shape[0]
    avg_time = var['Time_taken(min)'].mean()
    avg_dist = var['Distance_KM'].mean()
    
    print(f"Total Fleet Orders Managed: {total_orders} Records")
    print(f"Mean Delivery Cycle Duration: {avg_time:.2f} Minutes")
    print(f"Mean Transit Distance: {avg_dist:.2f} km")
    
    traffic_profile = var.groupby('Road_traffic_density').agg({
        'Time_taken(min)': 'mean',
        'Distance_KM': 'mean',
        'ID': 'count'
    }).rename(columns={'ID': 'Order_Volume', 'Time_taken(min)': 'Avg_Time_Min'}).sort_values(by='Avg_Time_Min', ascending=False)
    
    print("\nRoad Traffic Density Risk Profile:")
    print(traffic_profile)
    
    numeric_features = ['Delivery_person_Age', 'Delivery_person_Ratings', 'Distance_KM', 'Order_Hour', 'multiple_deliveries', 'Time_taken(min)']
    return var[numeric_features].corr()