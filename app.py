import streamlit as st
from utils import transcribe_audio, extract_medical_info

st.title("🏥 Medical Conversation Transcriber")

uploaded_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if uploaded_file:
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())

    st.audio("temp.wav")

    st.write("Processing...")

    text = transcribe_audio("temp.wav")
    structured = extract_medical_info(text)

    st.subheader("📝 Transcription")
    st.write(text)

    st.subheader("📊 Structured Data")
    st.json(structured)