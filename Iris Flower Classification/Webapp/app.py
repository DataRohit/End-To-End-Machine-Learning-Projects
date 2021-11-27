import streamlit as st
import pandas as pd
import pickle

iris_classifier = pickle.load(open("./lda_model.pkl", 'rb'))

# Streamlit web app code
st.write("""
    # Simple Iris Flower Prediction App
    
    This app predicts the Iris flower type!
"""
)

st.sidebar.header("User Input Parameters")

def user_input_features():
    sepal_length = st.sidebar.slider("Sepal Length", 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider("Sepal Length", 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider("Petal Length", 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider("Petal Wength", 0.1, 2.5, 0.2)
    
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader("User Input Parameters")
st.write(df)

prediction = iris_classifier.predict(df.values)
prediction_proba = iris_classifier.predict_proba(df.values)

st.subheader("Class labels and their correspondin index number")
st.write(iris_classifier.classes_)

st.subheader("Prediction")
st.write(prediction)

st.subheader("Prediction Probability")
st.write(pd.DataFrame(prediction_proba, columns=iris_classifier.classes_))