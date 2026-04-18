"""
Build an app that:
Takes a sentence from user
Sends to Gemini with instruction:
 “Improve this sentence professionally”
Displays improved version
"""

from google import genai
import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)

user_response = st.text_input("Enter your response: ")
if user_response:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= "{}, now Improve this sentence professionally".format(user_response)

    )
    st.markdown(response.text)
