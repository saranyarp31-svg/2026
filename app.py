import streamlit as st
from chunker import chunk_text
from translator import translate_to_tamil
from voice_output import tamil_voice
from pdf_generator import create_pdf

st.set_page_config(
    page_title="Phase-2 Advanced Tamil Translator",
    layout="centered"
)

st.title("Phase-2 : Any Language → Perfect Tamil 🇮🇳")
st.write("Supports long text • Tamil voice • PDF download")

user_text = st.text_area(
    "Enter text in any language",
    height=250,
    placeholder="Paste long paragraphs here..."
)

if st.button("Translate to Tamil"):
    if not user_text.strip():
        st.warning("Please enter some text")
    else:
        with st.spinner("Generating high-quality Tamil translation..."):
            chunks = chunk_text(user_text)
            tamil_text = translate_to_tamil(chunks)

        st.subheader("✅ Tamil Output")
        st.success(tamil_text)

        # 🔊 Tamil Voice Output
        audio_path = tamil_voice(tamil_text)
        st.audio(audio_path)

        # 📄 PDF Download
        pdf_path = create_pdf(tamil_text)
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Tamil as PDF",
                data=f,
                file_name="Tamil_Translation.pdf",
                mime="application/pdf"
            )

