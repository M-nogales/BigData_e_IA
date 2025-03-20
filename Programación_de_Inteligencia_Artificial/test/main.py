# Versión corregida y verificada con pytubefix
import os
import subprocess
from datetime import datetime
from pytubefix import YouTube
import speech_recognition as sr
from transformers import pipeline

def download_youtube_audio(url, output_path="audio"):
    if "/shorts/" in url:
        url = url.replace("/shorts/", "/watch?v=")
    
    yt = YouTube(url)
    audio_stream = yt.streams.get_audio_only()
    
    os.makedirs(output_path, exist_ok=True)
    
    # Generar nombre único con timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"audio_{timestamp}.{audio_stream.subtype}"
    
    # Descargar con nombre correcto
    m4a_path = audio_stream.download(
        output_path=output_path,
        filename=filename
    )
    return m4a_path

def convert_to_wav(m4a_path):
    wav_path = m4a_path.replace(".m4a", ".wav")
    
    try:
        subprocess.run(
            ['ffmpeg', '-i', m4a_path, '-vn', '-ar', '16000', '-ac', '1', wav_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return wav_path
    except subprocess.CalledProcessError as e:
        print(f"Error en conversión: {e.stderr.decode()}")
        raise

def transcribe_audio(wav_path):
    r = sr.Recognizer()
    try:
        with sr.AudioFile(wav_path) as source:
            audio = r.record(source)
            return r.recognize_google(audio, language='es-ES')
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""
    except sr.RequestError as e:
        print(f"Error de servicio: {e}")
        return ""

def summarize_text(text):
    try:
        summarizer = pipeline(
            "summarization",
            model="filco306/gpt2-small-spanish-summarization"
        )
        return summarizer(text, max_length=150, min_length=30)[0]['summary_text']
    except Exception as e:
        print(f"Error en resumen: {e}")
        return ""

if __name__ == "__main__":
    youtube_url = input("Ingresa la URL de YouTube: ")
    
    try:
        # 1. Descargar audio
        print("Descargando audio...")
        m4a_path = download_youtube_audio(youtube_url)
        
        # 2. Convertir a WAV
        print("Convirtiendo a WAV...")
        wav_path = convert_to_wav(m4a_path)
        
        # 3. Transcribir
        print("Transcribiendo...")
        transcription = transcribe_audio(wav_path)
        
        if transcription:
            print("\nTranscripción completa:")
            print(transcription)
            
            # 4. Resumir
            print("\nGenerando resumen...")
            summary = summarize_text(transcription)
            print("\nResumen:")
            print(summary)
        else:
            print("No se obtuvo transcripción para resumir")
        
        # Limpiar archivos
        os.remove(m4a_path)
        os.remove(wav_path)
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("Posibles soluciones:")
        print("1. Verifica que FFmpeg esté instalado y en el PATH")
        print("2. Ejecuta como administrador si hay problemas de permisos")
        print("3. Revisa espacios en nombres de archivo")