import pandas as pd
from src.preprocessing import preprocessing_pipeline
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
import joblib

def train_model():

    # Load Data
    df = pd.read_parquet('Data/clean/cleaned_df.parquet')

    # Split Data into Inputs and Output
    x = df.drop('Price', axis= 1)
    y = df['Price']
    
    # Model Pipeline
    model_pipeline = Pipeline(steps= [('Preprocessing', preprocessing_pipeline()),
                                      ('Model', XGBRegressor(learning_rate = 0.2, max_depth = 5, n_estimators = 200, subsample = 1.0))])
    
    # Fit Model
    model_pipeline.fit(x, y)

    # Save Model
    joblib.dump(model_pipeline, 'models/Xgb_model.pkl')

    # Save Column names
    joblib.dump(x.columns, 'metadata/inputs.pkl')

    # Save Unique Values
    uniq_val_dict = {}
    for col in x.columns:
        uniq_val_dict[col] = x[col].unique()

    joblib.dump(uniq_val_dict, 'metadata/unique_values_dict.pkl')
    
if __name__ == '__main__':
    train_model()