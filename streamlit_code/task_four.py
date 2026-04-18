import streamlit as st


st.title("Text Style Explorer")

write = st.text_input("Write Something: ")
if write:
    st.title(write)
    st.divider()
    st.header(write)
    st.divider()
    st.subheader(write)
    st.divider()
    st.text(write)
    st.divider()
