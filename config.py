from pathlib import Path

# Define project paths
BASE_DIR: str = Path(__file__).resolve().parent
DATA_DIR: str = BASE_DIR / 'data'
RAW_DATA_DIR: str = DATA_DIR / 'raw'
PROCESSED_DATA_DIR: str = DATA_DIR / 'processed'
RESULTS_DIR: str = BASE_DIR / 'results'
NOTEBOOKS_DIR: str = BASE_DIR / 'notebooks'
MODELS_DIR: str = BASE_DIR / 'models'

# Define file paths
RAW_DATA_FILE: str = RAW_DATA_DIR / 'house_prices.csv'
PROCESSED_ORIGINAL_FILE: str = PROCESSED_DATA_DIR / 'dataset_original.csv'
PROCESSED_REMOVED_FILE: str = PROCESSED_DATA_DIR / 'dataset_removed.csv'
PROCESSED_CAPPED_FILE: str = PROCESSED_DATA_DIR / 'dataset_capped.csv'

# Target variable
TARGET_VARIABLE: str = 'TARGET(PRICE_IN_LACS)'

# Categorical features
CATEGORICAL_FEATURES: list = [
  'POSTED_BY',
  'UNDER_CONSTRUCTION',
  'BHK_OR_RK',
  'RERA',
  'READY_TO_MOVE',
  'RESALE',
  'ADDRESS',
]

# Numerical features
NUMERICAL_FEATURES: list = [
  'BHK_NO.',
  'SQUARE_FT',
  'LONGITUDE',
  'LATITUDE',
]

# Features to drop
FEATURES_TO_DROP: list = [
  'ADDRESS',
]

# Engineered numerical features
ENGINEERED_NUMERICAL_FEATURES: list = [
  'PRICE_PER_SQFT',
  'TOTAL_ROOMS',
  'LARGE_PROPERTY',
  'LAT_LONG_INTERACTION',
]

# Engineered categorical features
ENGINEERED_CATEGORICAL_FEATURES: list = [
  'SIZE_CATEGORY',
]