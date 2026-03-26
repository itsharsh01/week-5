import pandas as pd
import os

def run_part_c():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "..", "..", "AI_Job_Market_Trends_2026.csv")
    
    if not os.path.exists(csv_path):
        print(f"Error: Could not find dataset at {csv_path}")
        return

    print("Loading dataset...")
    df = pd.read_csv(csv_path)

    print("\n--- Q2: Write code to filter rows where a column value is greater than average ---")
    
    # We will filter jobs where salary is greater than the average salary
    average_salary = df['salary'].mean()
    print(f"Average Salary: {average_salary:.2f}")

    above_average_jobs = df[df['salary'] > average_salary]
    
    print(f"Number of jobs with above-average salary: {len(above_average_jobs)}")
    print("\nSample of those jobs:")
    print(above_average_jobs[['job_title', 'company_size', 'salary']].head())

if __name__ == "__main__":
    run_part_c()
