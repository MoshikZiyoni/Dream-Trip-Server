import os
import time
import openai
from app.models import QueryChatGPT


async def run_long_poll_async(ourmessage):
    try:
        answer_from_data = QueryChatGPT.objects.filter(question__exact=ourmessage)
        if answer_from_data.exists():
            data = answer_from_data.values('answer')[0]
            answer = data['answer']
            print('answer in data')
            return answer
        else:
            print('Not Found')
    except:
        print('Internal Server Error')
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
            openai.api_key = os.environ.get('API_KEY')
            print ('start GPT')
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": ourmessage}
                ]
            )
            answer=(completion.choices[0].message.content)
            
            # await database_sync_to_async(query.save)()

            print (answer)
            return answer
        except openai.error.APIError as e:
            if e.status_code == 429:
                # If we hit the API rate limit, wait for a bit before trying again
                time.sleep(1)
            else:
                # If there's another API error, raise an exception
                raise
