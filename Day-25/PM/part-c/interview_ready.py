import pandas as pd
import os

def run_part_c():
    # Use the existing CSV from AM as the dataset for Q2
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Assuming standard project structure where Day-25 holds the CSV
    csv_path = os.path.join(base_dir, "..", "..", "AI_Job_Market_Trends_2026.csv")
    
    print("--- Q2: Separate features and target from dataset ---")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        
        # Let's say we want to predict 'salary' (Target) using the rest as Features
        # For simplicity, let's take a subset of columns to display
        columns_to_use = ['experience_level', 'remote_type', 'job_openings', 'salary']
        df_subset = df[columns_to_use].dropna().head(10) # 10 rows for demo
        
        X = df_subset.drop(columns=['salary'])
        y = df_subset['salary']
        
        print("\nFeatures (X) showing first 5 rows:")
        print(X.head())
        print("\nTarget (y) showing first 5 rows:")
        print(y.head())
    else:
        print("Dataset not found!")

if __name__ == "__main__":
    run_part_c()
