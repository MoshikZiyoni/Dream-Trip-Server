from django.shortcuts import render
import os
import openai
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import QueryChatGPT
from rest_framework import status
import traceback


@api_view(['GET', 'POST'])
def gpt_func(request):
    question2="{country:'..',cities:[{city:,description:,attractions:[name:],travelDay:}]}"
    ourmessage=f"provide me a Trip to {request.data['mainland']} ,for {request.data['travelers']} trip,budget {request.data['budget']} {request.data['durring']},put the answer in the following JSON structure \n``` {question2}"
    # print (ourmessage)
    try:
        answer_from_data=QueryChatGPT.objects.filter(question__exact=ourmessage)
        if answer_from_data.exists():
            data=answer_from_data.values('answer')[0]
            answer = data['answer']
            print ('answer in data')
            return Response(answer, status=status.HTTP_200_OK)
        else:
            print('Not Found')
            
    except:
        print ('Internal Server Error')
    query = QueryChatGPT()
    query.question = ourmessage

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.environ.get('API_KEY')
    # openai.api_key = 
    model_id = 'gpt-3.5-turbo'

    def ChatGPT_conversation(conversation):
        response = openai.ChatCompletion.create(
            model=model_id,
            messages=conversation
        )
        conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
        return conversation 

    try:
        conversation = []
        conversation.append({'role': 'system', 'content': 'How may I help you?'})
        conversation = ChatGPT_conversation(conversation)
        # print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

        prompt = (ourmessage)
        conversation.append({'role': 'user', 'content': prompt})
        conversation = ChatGPT_conversation(conversation)
        # our_answer=('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
        our_answer = (conversation[-1]['content'].strip())
    except Exception as e:
            print ('cant GPT')
            print (our_answer,'our_answer ERROR')  
            traceback.print_exc()
            print (e)
    try:
        start = our_answer.index("```") + 3 # Add 3 to skip over the opening ```
        end = our_answer.rindex("```") # Find the index of the closing ```
        json_str = our_answer[start:end] # Extract the JSON string
    except:
        print ('json_str',json_str)
        our_answer=json_str
        print ('not found ''')
    # print('number 1',json_str)
    try:
        json_str= json_str.replace('json', '')
        # print('Success',json_str)
        query.answer = json_str
        query.save()
        return(Response(json_str))
    except:
        # print ('not possible')
        query.answer = json_str
        query.save()
        print ('excpet json_str',json_str)
        return (Response(json_str))
   