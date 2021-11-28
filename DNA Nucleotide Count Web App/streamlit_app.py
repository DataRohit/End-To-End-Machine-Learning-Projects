######################
# Import libraries
######################

import pandas as pd
from PIL import Image
import streamlit as st
import plotly.express as px

from helper_functions import *

######################
# Page Title
######################

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True) # Setting image to use full column width

st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")

######################
# Input Text Box
######################

st.sidebar.header('Enter DNA sequence')

# Sample DNA Squence
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

## Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')

X = DNA_nucleotide_count(sequence)
X

### 2.Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame()
df["nucleotide"] = X.keys()
df["name"] = ["Adenine", "Thymine", "Guanine", "Cytosine"]
df["count"] = X.values()
st.write(df)

### 3. Display Bar Chart using Plotly
fig = px.bar(df, x="nucleotide", y="count", title="<b>Nucleotide vs Count</b>")
st.plotly_chart(fig, use_container_width=True)
