import streamlit as st

selected = st.selectbox("Choose your profession", ("Student","Employee","Businessman"),index = None,accept_new_options = True
                        )
st.write("You selected : ",selected)