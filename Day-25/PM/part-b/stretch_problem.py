import pandas as pd

def run_part_b():
    print("--- Regression Example ---")
    print("Use Case: Predicting the fuel efficiency (MPG) of a car.")
    print("Input (Features): Engine size, weight, horsepower.")
    print("Output (Target): Continuous variable representing MPG.\n")
    
    reg_data = {
        'engine_size': [2.0, 1.5, 3.0, 1.8],
        'weight_lbs': [3000, 2500, 4000, 2800],
        'mpg': [25.5, 32.0, 18.5, 28.0]
    }
    print(pd.DataFrame(reg_data))

    print("\n--- Classification Example ---")
    print("Use Case: Predicting whether a bank transaction is fraudulent.")
    print("Input (Features): Transaction amount, location, user device.")
    print("Output (Target): Discrete class (0 for Legitimate, 1 for Fraud).\n")
    
    clf_data = {
        'amount': [50.0, 1200.0, 15.0, 3000.0],
        'location_score': [1, 5, 2, 8],
        'is_fraud': [0, 1, 0, 1]
    }
    print(pd.DataFrame(clf_data))

if __name__ == "__main__":
    run_part_b()
