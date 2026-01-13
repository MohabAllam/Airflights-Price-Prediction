from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

def preprocessing_pipeline():

    # Numerical pipeline
    scaler = StandardScaler()
    num_pipeline = Pipeline(steps= [ ('Scaling', scaler) ])

    # Cat Pipeline
    ohe = OneHotEncoder(drop= 'first', sparse_output= False)
    cat_pipeline = Pipeline(steps= [ ('OHE', ohe) ])

    # Assign each column to its corresponding Pipeline
    preprocessing = ColumnTransformer(transformers= [ ('Num Pipeline', num_pipeline, ['Duration', 'journey_month', 'journey_day', 'distance', 'Num_of_stops']), 
                                                    ('Cat Pipeline', cat_pipeline, ['Airline', 'Source', 'Destination', 'journey_weekday', 'Dep_hour']) ])

    return preprocessing