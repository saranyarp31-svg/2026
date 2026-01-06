from transformers import pipeline

# Load once (important for Streamlit)
translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M",
    src_lang="eng_Latn",
    tgt_lang="tam_Taml"
)

def translate_to_tamil(chunks):
    tamil_output = []

    for chunk in chunks:
        translated = translator(chunk, max_length=512)
        tamil_output.append(translated[0]['translation_text'])

    return " ".join(tamil_output)
