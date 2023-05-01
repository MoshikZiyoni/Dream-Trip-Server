import os
import time
import openai
import requests

def run_long_poll_async1(message2):
    print ('start GPT2')
    try:
        url = "https://f6xh5hezzzorrdtzjkja63tziy0fbjmr.lambda-url.eu-north-1.on.aws/"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response)
        print(response.text)
        openai.api_key = response    
    except:
        print('key not good')
    # Set up the long polling parameters
    timeout = 50  # Set the long poll timeout to 50 seconds
    start_time = time.time()
    # Loop until a response is received or the timeout is reached
    while True:
        # Check if the timeout has been reached
        elapsed_time = time.time() - start_time
        if elapsed_time >= timeout:
            print('Timeout reached')
            return "I'm sorry, I could not generate a response. Please try again later."
        
        try:         
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": message2}
                ]
            )
            answer=(completion.choices[0].message.content)
            

            print (answer)
            return answer
        except openai.error.APIError as e:
            if e.status_code == 429:
                # If we hit the API rate limit, wait for a bit before trying again
                time.sleep(1)
            else:
                # If there's another API error, raise an exception
                raise
