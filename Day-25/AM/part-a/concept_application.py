import pandas as pd
import os

def run_eda():
    # Attempt to load from parent directories if needed
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "..", "..", "AI_Job_Market_Trends_2026.csv")
    
    if not os.path.exists(csv_path):
        print(f"Error: Could not find dataset at {csv_path}")
        return

    print("Loading dataset...")
    df = pd.read_csv(csv_path)

    print("\n--- Basic Exploration ---")
    print("First 5 rows:")
    print(df.head())
    print("\nLast 5 rows:")
    print(df.tail())
    print(f"\nShape of the dataset: {df.shape}")
    print(f"Column Names: {list(df.columns)}")

    print("\n--- Data Cleaning ---")
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    
    df_cleaned = df.dropna()
    print("\nMissing values after dropping NAs:")
    print(df_cleaned.isnull().sum())

    print("\n--- Descriptive Statistics ---")
    print("Descriptive stats using describe():")
    print(df_cleaned.describe())
    
    print("\nInterpretation:")
    print("- Mean gives the average value for numerical features.")
    print("- Min and Max show the range of values in each column.")
    print("- Std (Standard Deviation) indicates the dispersion of data points from the mean.")

    print("\n--- Categorical Analysis ---")
    cat_columns = df_cleaned.select_dtypes(include=['object', 'category']).columns
    if len(cat_columns) > 0:
        # Pick the first categorical column for demonstration
        col = cat_columns[0]
        print(f"Analyzing categorical column: '{col}'")
        print("\nUnique values:")
        unique_vals = df_cleaned[col].unique()
        print(unique_vals)
        print("\nFrequency count:")
        print(df_cleaned[col].value_counts())
    else:
        print("No categorical columns found for analysis.")

if __name__ == "__main__":
    run_eda()
