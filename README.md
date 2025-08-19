# bootcamp_alan_wang

# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Note: Notebooks for Homeworks 3-6 (Stages 03-06) are stored in the `notebooks` folder
- Include all required files for grading.

## Project Folder Rules
- Keep project files organized and clearly named.

## Data Storage

### Folder Structure
- `data/raw/`: Contains immutable input data in its original form (CSV format)
- `data/processed/`: Contains cleaned and processed data in Parquet format for efficient analysis

### Formats
- **CSV**: Used for raw data as it's human-readable and universally supported
- **Parquet**: Used for processed data as it's compressed and preserves data types

### Environment Variables
Paths are configured via `.env.example` file:

## Data Cleaning Strategy

### Overview
This project implements a systematic data cleaning pipeline to handle missing values, remove irrelevant features, and normalize data for machine learning readiness.

### Cleaning Steps

#### 1. Column Removal
- **Strategy**: Remove columns with more than 50% missing values
- **Rationale**: Columns with excessive missing data may not provide meaningful information and could introduce noise
- **Implementation**: `drop_missing()` function with configurable threshold

#### 2. Missing Value Imputation
- **Numeric Columns**: Fill with median values
  - **Rationale**: Median is robust to outliers compared to mean
  - **Implementation**: `fill_missing_median()` function

- **Categorical Columns**: Fill with mode (most frequent value)
  - **Rationale**: Simple and effective for categorical data
  - **Implementation**: Mode imputation in the cleaning pipeline

#### 3. Data Normalization
- **Strategy**: Z-score standardization (StandardScaler)
- **Applied to**: All numeric columns except binary features
- **Rationale**: Brings all features to similar scales, improving algorithm performance
- **Implementation**: `normalize_data()` function using sklearn's StandardScaler

#### 4. Order of Operations
1. Drop high-missing columns first
2. Fill numeric missing values
3. Normalize numeric features
4. Handle categorical missing values

### Assumptions
- Dataset contains both numeric and categorical columns
- 50% missing threshold is appropriate for the domain
- Median imputation is suitable for numeric features
- Z-score normalization benefits the downstream ML tasks
- Binary numeric features should not be normalized

### Usage
```python
from src import cleaning

# Load data
df = pd.read_csv('data/raw/sample_data.csv')

# Apply cleaning pipeline
df = cleaning.drop_missing(df, threshold=0.5)
df = cleaning.fill_missing_median(df, numeric_columns)
df = cleaning.normalize_data(df, columns_to_normalize)
```