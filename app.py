from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()   ## load all environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="My Chat Bot",page_icon="🗣️")

st.header("My Chat Bot Web Application")

question = st.text_input("Write a question here....")

submit = st.button("Submit")

if submit:
    model = genai.GenerativeModel("gemini-1.5-flash")
    answer = model.generate_content(question)
    st.write(answer.text)