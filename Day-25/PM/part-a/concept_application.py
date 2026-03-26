import pandas as pd

def run_part_a():
    print("--- Dataset Understanding ---")
    
    # Create a small Pandas dataframe for supervised machine learning
    # Example: Predicting house prices (regression)
    data = {
        'area_sqft': [1500, 2000, 1200, 1800, 2500],
        'num_bedrooms': [3, 4, 2, 3, 5],
        'age_years': [10, 5, 15, 2, 8],
        'price_thousands': [300, 450, 250, 400, 550]
    }
    
    df = pd.DataFrame(data)
    print("\nDataset:")
    print(df)
    
    # Separate features (X) and target (y)
    X = df.drop(columns=['price_thousands'])
    y = df['price_thousands']
    
    print("\nFeatures (X):")
    print(X)
    
    print("\nTarget (y):")
    print(y)

if __name__ == "__main__":
    run_part_a()
