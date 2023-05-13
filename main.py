import streamlit as st
import plotly.express as px
import pandas as pd


st.title("In Search for Happiness")

X_axis = st.selectbox("Select the data for X-axis", ("GDP", "Happiness", "Generosity"))

Y_axis = st.selectbox("Select data to view", ("GDP", "Happiness", "Generosity"))

df = pd.read_csv("happy.csv")
match X_axis:
    case "Happiness":
        X_value = df['happiness']
    case "Generosity":
        X_value = df['generosity']
    case "GDP":
        X_value = df['gdp']
match Y_axis:
    case "Happiness":
        Y_value = df['happiness']
    case "Generosity":
        Y_value = df['generosity']
    case "GDP":
        Y_value = df['gdp']

st.subheader(f"{X_axis} and {Y_axis}")
figure = px.scatter(x=X_value, y=Y_value, labels={"x": f"{X_axis}", "y": f"{Y_axis}"})
st.plotly_chart(figure)
