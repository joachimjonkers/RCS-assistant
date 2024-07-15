import openai
import streamlit as st
import time
import os
import zipfile
import yaml
 
from inference_assistant import inference
from utils import create_assistant_from_config_file, upload_to_openai, export_assistant

st.set_page_config(
    page_title="10DLC to RCS Converter PoC",
    page_icon="🤖",
    layout="wide"
)

st.title("10DLC to RCS Converter PoC")

openaiKey = st.secrets["OPENAI_API_KEY"]

id_assistente = st.secrets["ASSISTANT_ID"]

inference(id_assistente)
