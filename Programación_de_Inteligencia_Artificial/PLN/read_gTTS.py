from gtts import gTTS

with open("quijote.txt", "r", encoding="utf-8") as f:
    lines = [f.readline() for _ in range(50)]
    text = "".join(lines)

tts = gTTS(text=text, lang='es')

# Guardar en mp3
tts.save("quijote.mp3")