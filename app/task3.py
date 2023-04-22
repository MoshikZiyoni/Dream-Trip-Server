import os
import openai

def run_gpt_app(ourmessage):
    openai.api_key = os.environ.get('API_KEY')
    print ('start 003')
    
    response=openai.Completion.create(
    model="text-davinci-003",
    prompt=ourmessage,
    max_tokens=1000,
    temperature=1
    )
    print (response['choices'][0]['text'])
    return (response['choices'][0]['text'])