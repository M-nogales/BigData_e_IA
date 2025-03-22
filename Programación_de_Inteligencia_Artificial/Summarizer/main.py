import os

import yt_dlp
import whisper
import datetime
import nltk

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

nltk.download('punkt_tab')

# Crear carpetas si no existen
os.makedirs("audio", exist_ok=True)
os.makedirs("transcription", exist_ok=True)
os.makedirs("summary", exist_ok=True)


def descargar_audio(url):
    """Descarga el audio de YouTube en formato WAV (sin usar FFmpeg)."""
    timestamp = datetime.datetime.now().strftime("-%Y%m%d-%H%M%S")
    audio_filename = f"audio/audio{timestamp}.wav"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': audio_filename,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print(f"✅ Audio descargado: {audio_filename}")
    return audio_filename

def transcribir_audio(audio_file):
    """Transcribe el audio usando Whisper y guarda la transcripción en 'transcription'."""
    model = whisper.load_model("medium")
    result = model.transcribe(audio_file)
    
    texto_transcrito = result["text"]
    print("\n📝 Transcripción:\n", texto_transcrito)

    # Guardar la transcripción en 'transcription/'
    transcription_filename = f"transcription/{os.path.basename(audio_file).replace('.wav', '.txt')}"
    with open(transcription_filename, "w", encoding="utf-8") as f:
        f.write(texto_transcrito)
    
    print(f"✅ Transcripción guardada en {transcription_filename}")

    return transcription_filename, texto_transcrito


def resumir_texto(texto, output_filename):
    """Resume el texto usando LexRank y guarda el resumen en 'summary/'."""
    parser = PlaintextParser.from_string(texto, Tokenizer("spanish"))
    summarizer = LexRankSummarizer()
    
    resumen = "\n".join(str(sentence) for sentence in summarizer(parser.document, 20))  # 20 oraciones

    print("\n📌 Resumen:\n", resumen)

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(resumen)

    print(f"✅ Resumen guardado en {output_filename}")

if __name__ == "__main__":
    url = input("🎥 Ingresa la URL del video de YouTube: ")

    audio_file = descargar_audio(url)
    transcription_filename, texto_transcrito = transcribir_audio(audio_file)

    # Guardar el resumen de la transcripción
    summary_filename = transcription_filename.replace("transcription", "summary")
    resumir_texto(texto_transcrito, summary_filename)