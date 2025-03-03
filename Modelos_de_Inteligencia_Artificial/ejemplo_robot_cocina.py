import nemo.collections.asr as nemo_asr
import spacy

# Cargar modelo de reconocimiento de voz (STT - Speech to Text)
asr_model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="stt_es_quartznet15x5")

# Cargar modelo de PLN para análisis de intención
nlp = spacy.load("es_core_news_sm")

# Definir posibles comandos para el robot de cocina
COMANDOS_VALIDOS = {
    "mezclar": ["mezcla", "remueve", "bate"],
    "cocinar": ["cocina", "calienta", "hierve"],
    "agregar": ["añade", "agrega", "echa"],
    "detener": ["detén", "para", "stop"]
}

def analizar_intencion(texto):
    """ Analiza la intención del usuario a partir del texto transcrito """
    doc = nlp(texto.lower())
    
    for token in doc:
        for accion, palabras_clave in COMANDOS_VALIDOS.items():
            if token.lemma_ in palabras_clave:
                return accion
    return "desconocido"

def ejecutar_comando(accion):
    """ Simula la ejecución del comando en el robot de cocina """
    if accion == "mezclar":
        return "🌀 Mezclando ingredientes..."
    elif accion == "cocinar":
        return "🔥 Cocinando a la temperatura establecida..."
    elif accion == "agregar":
        return "➕ Añadiendo ingrediente..."
    elif accion == "detener":
        return "⏹️ Deteniendo el proceso..."
    else:
        return "⚠️ Comando no reconocido."

def procesar_audio(audio_path):
    """ Función principal que transcribe el audio, analiza intención y ejecuta acción """
    print("🎙️ Procesando audio...")
    texto_transcrito = asr_model.transcribe([audio_path])[0]
    print(f"📝 Texto transcrito: {texto_transcrito}")

    intencion = analizar_intencion(texto_transcrito)
    print(f"🤖 Intención detectada: {intencion}")

    respuesta = ejecutar_comando(intencion)
    print(f"✅ Acción: {respuesta}")

# Ejemplo de uso con un archivo de audio (se debe grabar un comando y pasarlo al modelo)
# procesar_audio("comando_usuario.wav")
procesar_audio("robot.mp3")