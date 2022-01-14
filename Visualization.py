#import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib
import seaborn as sns 
import numpy as np

st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Cars_Dataset")

df=pd.read_csv('cars_data.csv')
cars_datapart = df.head(20)

st.table(cars_datapart)

st.header("Visualisation Using Seaborn")

st.text("Total data rows:")
st.text(df['Dimensions.Height'].count())

st.text("Average fuel economy(City):")
st.text(df['Fuel Information.City mpg'].mean())

st.text("Average fuel economy(Highway):")
st.text(df['Fuel Information.Highway mpg'].mean())

#bar plot
st.subheader("Bar Plot")
cars_datapart.plot(kind='bar',y=['Dimensions.Height','Dimensions.Length','Dimensions.Width'])
st.pyplot()

#Displot
st.subheader("Displot")
sns.displot(cars_datapart['Fuel Information.Highway mpg'])
st.pyplot()

#Correation
st.subheader("Heatmap")
sns.heatmap(cars_datapart.corr(),cmap='coolwarm',annot=True)
st.pyplot()
