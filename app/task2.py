import os
import openai


def run_gpt_func(ourmessage):
    openai.api_key = os.environ.get('API_KEY')
    print ('start 3.5')
    completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": ourmessage}
                        
                    ]
                )
    print (completion.choices[0].message.content)
    return(completion.choices[0].message.content)