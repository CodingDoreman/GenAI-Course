import streamlit as st

st.title("🧮 Simple Calculator")
st.write("If you can see this text, Streamlit is working!")

# Simple inputs
num1 = st.number_input("First number", value=10.0)
num2 = st.number_input("Second number", value=5.0)
operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    
    st.success(f"Result: {result}")