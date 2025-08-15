import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
from src.utils import get_summary_stats

# 1. NumPy Operations
def numpy_operations():
    """Demonstrate NumPy array operations and compare with loops"""
    print("\n=== NumPy Operations ===")
    
    # Create arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([6, 7, 8, 9, 10])
    
    # Elementwise operations
    print("Array addition:", arr1 + arr2)
    print("Array multiplication:", arr1 * arr2)
    print("Array exponentiation:", arr1 ** 2)
    
    # Performance comparison
    size = 1000000
    a = np.random.rand(size)
    b = np.random.rand(size)
    
    # Vectorized operation
    start = time.time()
    c = a * b
    vectorized_time = time.time() - start
    
    # Loop operation
    start = time.time()
    c_loop = np.zeros(size)
    for i in range(size):
        c_loop[i] = a[i] * b[i]
    loop_time = time.time() - start
    
    print(f"\nVectorized operation took: {vectorized_time:.6f} seconds")
    print(f"Loop operation took: {loop_time:.6f} seconds")
    print(f"Vectorized operation was {loop_time/vectorized_time:.1f}x faster")

# 2. Dataset Loading
def load_and_inspect_data(filepath="data/starter_data.csv"):
    """Load and inspect the dataset"""
    print("\n=== Dataset Loading ===")
    
    # Create directories if they don't exist
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    
    # Load data
    df = pd.read_csv(filepath)
    
    # Inspect data
    print("\nData Info:")
    print(df.info())
    
    print("\nFirst 5 rows:")
    print(df.head())
    
    return df

# 3. Summary Statistics
def calculate_summary_stats(df):
    """Calculate summary statistics"""
    print("\n=== Summary Statistics ===")
    
    # Basic statistics
    print("\nDescriptive statistics:")
    desc_stats = df.describe()
    print(desc_stats)
    
    # Groupby operations (assuming there's a 'category' column)
    if 'category' in df.columns:
        print("\nGroupby statistics:")
        group_stats = df.groupby('category').agg(['mean', 'median', 'std'])
        print(group_stats)
    else:
        print("\nNo 'category' column found for groupby operations")
        group_stats = None
    
    return desc_stats, group_stats

# 4. Save Outputs
def save_outputs(desc_stats, group_stats):
    """Save outputs to files"""
    print("\n=== Saving Outputs ===")
    
    # Save descriptive statistics
    desc_stats.to_csv("data/processed/summary.csv")
    desc_stats.to_json("data/processed/summary.json")
    print("Saved summary statistics to CSV and JSON")
    
    # Save group statistics if available
    if group_stats is not None:
        group_stats.to_csv("data/processed/group_summary.csv")
        group_stats.to_json("data/processed/group_summary.json")
        print("Saved group statistics to CSV and JSON")
    
    # Bonus: Create and save a basic plot
    if 'value' in desc_stats.columns:
        plt.figure(figsize=(8, 4))
        plt.bar(desc_stats.columns, desc_stats.loc['mean'])
        plt.title("Mean Values by Column")
        plt.ylabel("Mean Value")
        plt.savefig("data/processed/basic_plot.png")
        print("Saved basic plot to data/processed/basic_plot.png")

# 5. Reusable Functions
def get_summary_stats(df, groupby_col=None):
    """
    Utility function to get summary statistics
    Args:
        df: pandas DataFrame
        groupby_col: column name to group by (optional)
    Returns:
        Dictionary containing summary statistics
    """
    stats = {
        'description': df.describe(),
        'dtypes': df.dtypes,
        'null_counts': df.isnull().sum()
    }
    
    if groupby_col and groupby_col in df.columns:
        stats['group_stats'] = df.groupby(groupby_col).agg(['mean', 'median', 'std'])
    
    return stats

def main():
    import time  # Import here to avoid confusion with other time variables
    
    # Execute all steps
    numpy_operations()
    
    df = load_and_inspect_data()
    
    desc_stats, group_stats = calculate_summary_stats(df)
    
    save_outputs(desc_stats, group_stats)
    
    # Demonstrate reusable function
    print("\n=== Reusable Function Demo ===")
    summary = get_summary_stats(df, 'category' if 'category' in df.columns else None)
    print("\nSummary from reusable function:")
    print(summary['description'])

if __name__ == "__main__":
    main()