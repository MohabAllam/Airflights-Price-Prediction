import pandas as pd
import joblib

def make_prediction(Values):

    # Load Model
    model = joblib.load('models/Xgb_model.pkl')

    # Load Columns names
    inputs = joblib.load('metadata/inputs.pkl')

    prediction_row = pd.DataFrame(data= [Values], columns= inputs)

    result = round(model.predict(prediction_row)[0], 2)

    return result