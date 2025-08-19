# src/cleaning.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def fill_missing_median(df, columns):
    """
    Fill missing values in specified columns with their median values.
    
    Parameters:
    df (pd.DataFrame): Input dataframe
    columns (list): List of column names to fill missing values
    
    Returns:
    pd.DataFrame: Dataframe with missing values filled
    """
    df_copy = df.copy()
    for col in columns:
        if col in df_copy.columns:
            median_val = df_copy[col].median()
            df_copy[col] = df_copy[col].fillna(median_val)
    return df_copy

def drop_missing(df, threshold=0.5):
    """
    Drop columns with more than threshold percentage of missing values.
    
    Parameters:
    df (pd.DataFrame): Input dataframe
    threshold (float): Threshold percentage (0-1) for dropping columns
    
    Returns:
    pd.DataFrame: Dataframe with high-missing columns removed
    """
    df_copy = df.copy()
    missing_percentage = df_copy.isnull().mean()
    columns_to_drop = missing_percentage[missing_percentage > threshold].index.tolist()
    df_copy = df_copy.drop(columns=columns_to_drop)
    print(f"Dropped columns with >{threshold*100}% missing values: {columns_to_drop}")
    return df_copy

def normalize_data(df, columns):
    """
    Normalize specified columns using StandardScaler (z-score normalization).
    
    Parameters:
    df (pd.DataFrame): Input dataframe
    columns (list): List of column names to normalize
    
    Returns:
    pd.DataFrame: Dataframe with normalized columns
    """
    df_copy = df.copy()
    scaler = StandardScaler()
    
    for col in columns:
        if col in df_copy.columns:
            # Store original values for comparison
            original_values = df_copy[col].copy()
            
            # Normalize the column
            normalized_values = scaler.fit_transform(df_copy[[col]])
            df_copy[col] = normalized_values
            
            # Print normalization summary
            print(f"Normalized column '{col}':")
            print(f"  Original - Mean: {original_values.mean():.2f}, Std: {original_values.std():.2f}")
            print(f"  Normalized - Mean: {df_copy[col].mean():.2f}, Std: {df_copy[col].std():.2f}")
    
    return df_copy