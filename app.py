import streamlit as st
import pandas as pd
import numpy as np

st.title("hello this is the title of the streamlit project")
st.write("this is a paragraph written by streamlit")
df=pd.DataFrame({
    'first column':[1,2,3,4,5],
    'second column':[6,7,8,9,0]
})
st.header("this is the dataframe")
st.write(df)
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.write(chart_data)
st.line_chart(chart_data)
st.header("user input")
name=st.text_input("enter your name")
if name:
    st.write(f"hello {name}")
st.header("Age slider")
age=st.slider("enter your age",0,100,25)
st.write(f"you have entered the age: {age}")
options=['one','two','three','four']
choice=st.selectbox("choose an option in the given ",options)
st.write(f"you have entered the choice{choice}")