import streamlit as st
from chunker import chunk_text
from translator import translate_to_tamil
from voice_output import tamil_voice
from pdf_generator import create_pdf

st.set_page_config(page_title="Phase-2 Tamil Translator", layout="centered")

st.title("Phase-2 : Advanced Tamil Translator")
st.write("Any Language Text → High-Quality Tamil + Voice + PDF")

user_text = st.text_area("Enter text (any language)", height=200)

if st.button("Translate to Tamil"):
    if not user_text.strip():
        st.warning("Please enter text")
    else:
        with st.spinner("Translating..."):
            chunks = chunk_text(user_text)
            tamil_text = translate_to_tamil(chunks)

        st.subheader("Tamil Output")
        st.success(tamil_text)

        # Tamil Voice
        audio = tamil_voice(tamil_text)
        st.audio(audio)

        # PDF Download
        pdf_file = create_pdf(tamil_text)
        with open(pdf_file, "rb") as f:
            st.download_button(
                "Download Tamil as PDF",
                f,
                file_name="Tamil_Output.pdf"
            )
