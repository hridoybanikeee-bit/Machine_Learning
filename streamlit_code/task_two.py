import streamlit as st


st.title("Image showing app")
imag = st.file_uploader("Enter your images: ", type=['jpg','png','jpeg'], accept_multiple_files=True)


if imag:
    num_of_imag = len(imag)
    if num_of_imag > 3:
        st.error("Can't Upload more than 3 images")
    elif num_of_imag == 3:
        st.success("Great! You've uploaded 3 images")
        col = st.columns(3)
        for i, ima in enumerate(imag):
            with col[i]:
                st.image(ima)
    else:
        col = st.columns(num_of_imag)
        for i, ima in enumerate(imag):
            with col[i]:
                st.image(ima)






