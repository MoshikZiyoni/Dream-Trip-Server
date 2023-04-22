import os
import openai


def run_gpt_func(ourmessage):
    openai.api_key = os.environ.get('API_KEY')
    print ('start')
    completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0301",
                    messages=[
                        {"role": "user", "content": ourmessage}
                        
                    ]
                )
    return(completion.choices[0].message.content)