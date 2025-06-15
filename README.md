# House Price Prediction Project

## Project Overview
This project is an academic assignment focused on developing regression models to predict house prices using the "House Price Prediction Challenge" dataset from Kaggle. The core research question is to **investigate and quantify the impact of different outlier treatment strategies on model performance.**

## Project Structure
The project follows a standardized folder structure:
```
project_root/
├── data/
│   ├── raw/              # Original, unmodified data files
│   └── processed/        # Cleaned/split data (CSVs, JSON)
├── models/              # Saved, trained model files (.joblib, .h5)
├── notebooks/           # Jupyter notebooks (.ipynb)
├── results/            # Output tables and plots (.csv, .png)
├── src/                # Utility Python scripts
└── config.py           # Central configuration file
```

## Project Plan & Current Status

### 1. Data Exploration & Cleaning ✅
- Initial data loading and exploration
- Basic data quality checks
- Missing value analysis
- Data type verification

### 2. Outlier Detection & Analysis ✅
- Identification of outliers using IQR method
- Analysis of outlier characteristics
- Creation of three datasets:
  - Original (no treatment)
  - Removed Outliers (outliers removed)
  - Capped Outliers (values capped at 5th/95th percentiles)

### 3. Basic Feature Engineering ✅
- Feature creation and transformation
- Categorical encoding
- Feature scaling preparation
- Data split into train/test sets

### 4. Model Implementation 🔄 (In Progress)
- Implementation of three regression models:
  - Linear Regression
  - k-Nearest Neighbors (k-NN)
  - Neural Network
- Training on all three datasets
- Model evaluation and comparison

### 5. Evaluation & Comparison ❌
- Performance metrics analysis:
  - RMSE (Root Mean Square Error)
  - MAE (Mean Absolute Error)
  - R-squared
- Comparative analysis of outlier treatment strategies
- Visualization of results

### 6. Report Writing ❌
- Documentation of methodology
- Results interpretation
- Conclusions and recommendations

## Development Principles

### Configuration Management
- All static configurations are centralized in `config.py`
- Includes file paths, feature lists, and other constants
- Ensures consistency across the project

### Code Documentation
- All Python functions include professional docstrings
- Clear documentation of parameters and return values
- Consistent coding style and conventions

### Data Processing Pipeline
1. Data is processed in parallel for three different outlier treatments
2. Each dataset undergoes the same feature engineering steps
3. Models are trained and evaluated consistently across all datasets

## Next Steps
1. Complete the model implementation notebook
2. Train and evaluate all models
3. Generate performance comparison metrics
4. Create visualizations for results
5. Document findings and conclusions
