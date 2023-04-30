import json
import os
import time
import openai
from app.models import QueryChatGPT
from app.task3 import lambda_handler


def run_long_poll_async(ourmessage):
    print ('start GPT')
    # Set up the long polling parameters
    timeout = 50  # Set the long poll timeout to 25 seconds
    start_time = time.time()
    # Loop until a response is received or the timeout is reached
    while True:
        # Check if the timeout has been reached
        elapsed_time = time.time() - start_time
        if elapsed_time >= timeout:
            print('Timeout reached')
            return "I'm sorry, I could not generate a response. Please try again later."
        
        
        try:
            # openai.api_key = os.environ.get('API_KEY')

# Set the API key for the OpenAI SDK
            print(lambda_handler())
            openai.api_key = (lambda_handler())
            

            
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": ourmessage}
                ]
            )
            answer=(completion.choices[0].message.content)
            
            print (answer,'ANSWERRRRRRRRRRRRRRRR')

            print (json.loads(answer),'with json loadssssssssssssssssss')
            return answer
        except openai.error.APIError as e:
            if e.status_code == 429:
                # If we hit the API rate limit, wait for a bit before trying again
                time.sleep(1)
            else:
                # If there's another API error, raise an exception
                raise



