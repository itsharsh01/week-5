import pandas as pd
import os

def run_part_b():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "..", "..", "AI_Job_Market_Trends_2026.csv")
    
    if not os.path.exists(csv_path):
        print(f"Error: Could not find dataset at {csv_path}")
        return

    print("Loading dataset...")
    df = pd.read_csv(csv_path)

    print("\n--- 1. Filter dataset using multiple conditions ---")
    # Filters: experience_level == 'Senior' AND salary > 100000
    filtered_df = df[(df['experience_level'] == 'Senior') & (df['salary'] > 100000)]
    print(f"Number of senior roles with salary > 100K: {len(filtered_df)}")
    print(filtered_df[['job_title', 'experience_level', 'salary']].head())

    print("\n--- 2. Create a new column based on existing data ---")
    # New column: high_urgency_remote
    df['high_urgency_remote'] = (df['hiring_urgency'] == 'High') & (df['remote_type'] == 'Remote')
    print("Created 'high_urgency_remote' column.")
    print(df[['job_title', 'hiring_urgency', 'remote_type', 'high_urgency_remote']].head())

    print("\n--- 3. Sort dataset by a numerical column ---")
    # Sort by salary descending
    sorted_df = df.sort_values(by='salary', ascending=False)
    print("Top 5 highest paying jobs:")
    print(sorted_df[['job_title', 'company_size', 'salary']].head())

    print("\n--- 4. Group data and compute mean ---")
    # Group by job_title and compute mean salary
    grouped_df = df.groupby('job_title')['salary'].mean().reset_index()
    print("Mean salary by Job Title:")
    print(grouped_df)

if __name__ == "__main__":
    run_part_b()
