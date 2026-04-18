import streamlit as st

st.title("Fun with audio and video",anchor = False)
st.divider()

st.write("Audio file")
st.audio("E:\streamlit\pythonProject\Dil Hi Toh Hai - Full Video  The Sky Is Pink  Priyanka Chopra Jonas, Farhan Akhtar  Arijit Singh.mp3")
st.divider()
#taking input from user
aud = st.file_uploader("Enter your audio file:",
                       type = ['mp3','ogg','flac']
                       )
#print(type(aud))
if aud:
    st.audio(aud)