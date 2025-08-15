import pandas as pd

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