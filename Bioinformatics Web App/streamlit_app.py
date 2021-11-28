######################
# Import libraries
######################
import numpy as np
import pandas as pd
import pickle

import streamlit as st

from PIL import Image

from helper_functions import *

######################
# Page Title
######################

image = Image.open('solubility-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# Molecular Solubility Prediction Web App
This app predicts the **Solubility (LogS)** values of molecules!
NOTE: LogS (mol / liter) value is directly proportional to Solubility
Data obtained from the John S. Delaney. [ESOL:  Estimating Aqueous Solubility Directly from Molecular Structure](https://pubs.acs.org/doi/10.1021/ci034243x). ***J. Chem. Inf. Comput. Sci.*** 2004, 44, 3, 1000-1005.
***
""")

######################
# Input molecules (Side Panel)
######################

st.sidebar.header('User Input Features')

## Read SMILES input
SMILES_input = "NCCCC\nCCC\nCN"

SMILES = st.sidebar.text_area("SMILES input", SMILES_input)
SMILES = "C\n" + SMILES #Adds C as a dummy, first item
SMILES = SMILES.split('\n')

st.header('Input SMILES')
SMILES[1:] # Skips the dummy first item

## Calculate molecular descriptors
st.header('Computed molecular descriptors')
X = generate(SMILES)
X[1:] # Skips the dummy first item

######################
# Pre-built model
######################

# Reads in saved model - I Created Two Models using RandomForestRegressor(rfr) and LinearRegression(lr)
load_model = pickle.load(open('solubility_model_rfr.pkl', 'rb'))

# Apply model to make predictions
prediction = load_model.predict(X)
#prediction_proba = load_model.predict_proba(X)

st.header('Predicted LogS values')
prediction[1:] # Skips the dummy first item