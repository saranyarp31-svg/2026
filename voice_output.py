from gtts import gTTS
import tempfile

def tamil_voice(text):
    tts = gTTS(text=text, lang="ta")
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp.name)
    return temp.name

