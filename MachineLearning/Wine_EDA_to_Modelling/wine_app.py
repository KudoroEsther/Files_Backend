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