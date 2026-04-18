import streamlit as st

st.title("User information app")
#Take input and show your name
name = st.text_input("Enter your name: ",placeholder='Type your name please: ')
#Take  input and show your age
age = st.number_input("Enter your age: ",value = None, placeholder= "Type your age please")
#take input your profession from a selectbox
box = st.selectbox("Enter your professon: ",("Student","Employee","Businessman","Politician"), index= None, accept_new_options = True)
#Usage of Button
pressed  = st.button("Press to have all output: ",type = "primary")
if pressed:
    if name and age and box:
        st.write(f"Your name is {name} and you are {age} years old. You are a {box} now")
        st.success("Information collected successfully")
        
    else:
        st.write("Please fill up the form properly: ")
