import streamlit as st

st.title("Input your information")
st.divider()


#text input
name = st.text_input("Enter your name")
st.write("Your name is : ",name)
st.divider()

#number input
age = st.number_input("Enter your age: ",value=None,placeholder="Type your age: ")
st.write("Your age is: ",age)
st.divider()

#password input
password = st.text_input("Enter your password: ",type = "password")
st.write("Your pasword is: ",password)
st.divider()

pressed = st.button("Enter to confirm",type = "primary")
if pressed:
    st.write(f"Your name is {name} and your age is {age}")


