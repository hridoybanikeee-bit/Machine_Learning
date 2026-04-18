import streamlit as st

st.title("Play with Audio and Video")


aud_file = st.file_uploader("Enter your audio file: ", type = ['mp3','ogg'])
vid_file = st.file_uploader("Enter your video file: ", type = ['mp4','mkv','mov'])
play_button = st.button('Play')
if play_button:
    if not aud_file and not vid_file:
        st.error("Please upload at least one file before play")
    else:
        if aud_file:
            st.audio(aud_file)
        if vid_file:
            st.video(vid_file)
