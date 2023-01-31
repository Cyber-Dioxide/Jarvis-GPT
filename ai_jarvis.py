import openai
import json

with open('config.json' , 'r') as f:
    data = json.loads(f.read())


ORGANIATION_KEY = data['GPT_API_KEY']

openai.organization = data['GPT_ORGANIZARION_NAME']
openai.api_key = ORGANIATION_KEY
engine = openai.Engine().list()

def ai_jarvis(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response['choices'][0]['text']


