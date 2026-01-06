from transformers import pipeline

translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M",
    src_lang="eng_Latn",
    tgt_lang="tam_Taml"
)

def translate_to_tamil(chunks):
    output = []
    for chunk in chunks:
        result = translator(chunk, max_length=512)
        output.append(result[0]["translation_text"])
    return " ".join(output)

