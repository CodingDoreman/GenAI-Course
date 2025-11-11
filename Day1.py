import streamlit as st

st.title("Greeting Form")

# Text input for name
name = st.text_input("Enter your name:")

# Slider for age
age = st.slider("Select your age:", 1, 100, 25)

# Submit button
if st.button("Greet Me"):
    if name.strip():
        st.success(f"Hello **{name}**! You are **{age}** years old 🎉")
    else:
        st.warning("Please enter your name!")
