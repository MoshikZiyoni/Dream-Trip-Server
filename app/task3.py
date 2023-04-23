import os
import openai
import json
from app.models import QueryChatGPT

def run_gpt_app(ourmessage):
    openai.api_key = os.environ.get('API_KEY')
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
    
    
    response=openai.Completion.create(
    model="text-davinci-003",
    prompt=ourmessage,
    max_tokens=3000,
    temperature=0.98
    )
    query = QueryChatGPT()
    query.question = ourmessage
    response_dict = json.loads(response['choices'][0]['text'])
    query.answer = response_dict
    query.save()

    print (response_dict)
    return (response_dict)