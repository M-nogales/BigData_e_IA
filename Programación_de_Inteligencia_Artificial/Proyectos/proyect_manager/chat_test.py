# import os
# from openai import OpenAI

# client = OpenAI(
#     # This is the default and can be omitted
#     api_key="secret api key",
# )

# response = client.responses.create(
#     model="gpt-4o",
#     instructions="You are a weather assistant. Provide a brief weather report.",
#     input="what's the weather in seville today?",
# )

# print(response.output_text)
#----

# from openai import OpenAI

# client = OpenAI()

# completion = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {"role": "weather assistant", "content": "provide a brief weather report."},
#         {
#             "role": "user",
#             "content": "what's the weather in seville today?",
#         },
#     ],
# )

# print(completion.choices[0].message.content)
#! gemini: 
'''
15 RPM	Máximo de 15 solicitudes por minuto (Requests Per Minute).
1,000,000 TPM	Máximo de 1 millón de tokens por minuto (Tokens Per Minute).
1,500 RPD	Máximo de 1,500 solicitudes por día (Requests Per Day).
'''

from google import genai

client = genai.Client(api_key="GEMINI_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)