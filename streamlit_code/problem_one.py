import streamlit as st

a = st.number_input("Enter value of a: ")
b = st.number_input("Enter value of b: ")
op = st.selectbox("Select the operator",["+", "-", "*", "/"], index=None)
result = 0
if op:
    if op == "+":
        result = a+b
    elif op == '-':
        result = a-b
    elif op == '*':
        result = a*b
    elif op == '/':
        if b == 0:
            result = "Division by 0 is not possible"
        else:
            result = a/b
    else:
        st.write("You have pressed wrong operator")
st.write(result)
