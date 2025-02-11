from googletrans import Translator
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Texto de prueba
texto = "La inteligencia artificial está transformando el mundo porque"

# Crear un objeto traductor
translator = Translator()

# Traducir el texto
entrada = translator.translate(texto, src='es', dest='en')

# Cargar el modelo GPT-2 y su tokenizador
model_name = "gpt2"
# model_name = "DeepESP/gpt2-spanish-medium" ejemplo de modelo en español entrenado con literatura y teatro,
# resultados raros
# entrada = "La inteligencia artificial está transformando el mundo porque"

tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Codificar la entrada
input_ids = tokenizer.encode(entrada, return_tensors="pt")

# Generar texto con el modelo
output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.92, temperature=0.7)

# Decodificar la salida
texto_generado = tokenizer.decode(output[0], skip_special_tokens=True)

# Imprimir el texto generado
print(texto_generado)