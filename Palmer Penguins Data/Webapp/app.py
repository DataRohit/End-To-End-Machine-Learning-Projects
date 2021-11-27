# * Required Imports
import streamlit as st
import pandas as pd
import pickle

# * Getting Our Data and Model
penguins_df = pd.read_csv("./penguins_data.csv")
rfc_classifier = pickle.load(open("rfc_model.pkl", 'rb'))

# * Streamlit Code
st.write(
    """
# Penguins Prediction App

This app predicts the **Palmer Penguin** species!

Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst
"""
)

st.sidebar.header("User Input Features")

st.sidebar.markdown("""
[Example CSV inpur file](https://raw.githubusercontent.com/DataRohit/Palmer-Penguins-Stramlit/master/Webapp/penguins_example.csv)                    
""") # ! Change the link later

# * Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload you input CSV file", type=["csv"])
if uploaded_file: # If the uploaded file is not none the convert it into pandas dataframe
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        island = st.sidebar.selectbox("Island", tuple(sorted(penguins_df.island.unique())))
        sex = st.sidebar.selectbox("Sex", tuple(sorted(penguins_df.sex.unique())))
        bill_length_mm = st.sidebar.slider("Bill Length (mm)", 32.1, 59.6, 43.9)
        bill_depth_mm = st.sidebar.slider("Bill Depth (mm)", 13.1, 21.5, 17.2)
        flipper_length_mm = st.sidebar.slider("Flipper Length (mm)", 172.0, 231.0, 201.0)
        body_mass_g = st.sidebar.slider("Body Mass (g)", 2700.0, 6300.0, 4207.0)
        
        data = {
            "island":island,
            "sex":sex,
            "bill_length_mm":bill_length_mm,
            "bill_depth_mm":bill_depth_mm,
            "flipper_length_mm":flipper_length_mm,
            "body_mass_g":body_mass_g, 
        }
        
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

# * Displays the user input Features
st.subheader("User Input Features")

if uploaded_file:
    st.write(input_df)
else:
    st.write("Awaiting CSV file to be uploaded. Currently using input parameters from Sidebar Controls.")
    st.write(input_df)
    
# * Combines user input features with entire penguins dataset
# * This will be useful for the encoding phase
penguins_df_features = penguins_df.drop(columns=['species'])
df = pd.concat([input_df, penguins_df_features],axis=0)

# * Encode Categorical Features and get the firstrow i.e., User Input
cols_to_encode = ["island", "sex"]
for col in cols_to_encode:
    dummy_df = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy_df], axis=1)
    del df[col]

input_df = df[:1]

# * Use our Loaded RandomForestClassifier Model for Predictions
prediction = rfc_classifier.predict(input_df.values.tolist())
prediction_proba = rfc_classifier.predict_proba(input_df)

# * Display Prediction and Prediction Probabilities
st.subheader("Prediction")
st.write(prediction)

st.subheader('Prediction Probability')
st.write(pd.DataFrame(prediction_proba, columns=rfc_classifier.classes_))