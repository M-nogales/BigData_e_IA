import speech_recognition as sr

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Cargar el archivo de audio (debe ser un archivo WAV)
audio_file = "audio/Crumble_de_frutos_del_bosque.wav"

# Cargar el archivo de audio usando SpeechRecognition
with sr.AudioFile(audio_file) as source:
    # Escuchar el audio
    audio_data = recognizer.record(source)

    # Intentar reconocer el texto
    try:
        texto = recognizer.recognize_google(audio_data, language='es-ES')  # Usa 'es-ES' para español
        print("Texto reconocido:", texto)
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError:
        print("Error en la solicitud al servicio de reconocimiento de voz")
