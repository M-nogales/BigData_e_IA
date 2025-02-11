import pyttsx3

engine = pyttsx3.init()

with open("quijote.txt", "r", encoding="utf-8") as f:
    lines = [f.readline() for _ in range(50)]
    text = "".join(lines)

engine.say(text)
engine.runAndWait()