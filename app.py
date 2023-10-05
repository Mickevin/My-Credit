import streamlit as st

st.set_page_config(
    page_title="My Credit App", 
    page_icon=":smiley:")

st.title("My Credit App 1")

st.button("Click me")

st.text_input("Name")
st.text_input("Age")
st.write("Hello World")