import whisper
import tempfile

model = whisper.load_model("base")

def voice_to_text(audio_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(audio_file.read())
        temp_path = tmp.name

    result = model.transcribe(temp_path)
    return result["text"]
