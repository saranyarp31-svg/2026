import streamlit as st
from chunker import chunk_text
from translator import translate_to_tamil
from voice_input import voice_to_text
from voice_output import tamil_voice
from pdf_generator import create_pdf

st.title("Phase-2: Advanced Tamil Translator")

input_mode = st.radio("Input Mode", ["Text", "Voice"])

if input_mode == "Text":
    user_text = st.text_area("Enter text")
else:
    audio = st.file_uploader("Upload voice", type=["wav", "mp3"])
    if audio:
        user_text = voice_to_text(audio)
        st.success(user_text)

if st.button("Translate to Tamil"):
    chunks = chunk_text(user_text)
    tamil = translate_to_tamil(chunks)

    st.subheader("Tamil Output")
    st.write(tamil)

    audio_file = tamil_voice(tamil)
    st.audio(audio_file)

    pdf = create_pdf(tamil)
    with open(pdf, "rb") as f:
        st.download_button("Download PDF", f, file_name="Tamil_Output.pdf")
