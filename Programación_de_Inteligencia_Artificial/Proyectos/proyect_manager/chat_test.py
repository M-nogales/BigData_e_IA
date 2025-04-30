import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="Key",
)

response = client.responses.create(
    model="gpt-4o",
    instructions="You are a weather assistant. Provide a brief weather report.",
    input="what's the weather in seville today?",
)

print(response.output_text)
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