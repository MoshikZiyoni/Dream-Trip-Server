from celery import shared_task
from django.http import JsonResponse
from app.models import QueryChatGPT
import os
import openai
import time

MAX_RETRIES = 3
WAIT_TIME = 5

@shared_task
def run_gpt_func(ourmessage):
    try:
        answer_from_data=QueryChatGPT.objects.filter(question__exact=ourmessage)
        if answer_from_data.exists():
            data=answer_from_data.values('answer')[0]
            answer = data['answer']
            print ('answer in data')
            return answer
        else:
            print('Not Found')

    except:
        print ('Internal Server Error')
    query = QueryChatGPT()
    query.question = ourmessage
    
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.environ.get('API_KEY')

    try_count = 0
    while try_count < MAX_RETRIES:
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": ourmessage}
                ]
                )
            
            ourdata = (completion.choices[0].message.content)

            query.answer = ourdata
            query.save()

            return ourdata

        except Exception as e:
            print(f"An error occurred in try {try_count+1}: {e}")
            try_count += 1
            time.sleep(WAIT_TIME)
