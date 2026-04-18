import streamlit as st

st.title("Input your files",anchor = False)
st.divider()

images = st.file_uploader("Enter your image: ",
                 type = ['jpg','jpeg','png'],
                          accept_multiple_files= True)
if images:
    col = st.columns(len(images))
    for i, imag in enumerate(images):
        with col[i]:
            st.image(imag)

