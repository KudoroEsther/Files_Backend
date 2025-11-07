from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

from fastapi import FastAPI
from pydantic import BaseModel
import joblib

import numpy as np
import pandas as pd

# Loading th saved model
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

#Initializing the application
app = FastAPI()

#creating the pydantic model
class WineFeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulphur_dioxide: float
    total_sulphur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

#Creating endpoints
@app.get("/")
def home():
    return{
        "message": "Welcome to Wine Quality Predictor"
    }

#prediciton endpoint
#Converting the features to 2d numpy array using [[]]
@app.post("/predict")
def predict(wine: WineFeatures):
    features= np.array([[
        wine.fixed_acidity,
        wine.volatile_acidity,
        wine.citric_acid,
        wine.residual_sugar,
        wine.chlorides,
        wine.free_sulphur_dioxide,
        wine.total_sulphur_dioxide,
        wine.density,
        wine.pH,
        wine.sulphates,
        wine.alcohol
    ]])

    #Scaling input features using the loaded scaler (to normalize the input)
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)

    # Return the pediction and prediction converted to string for serialization
    return {"predicted_quality": str(prediction[0])}

#Run the app using the uvicorn command:
# uvicorn wine_app:app --reload