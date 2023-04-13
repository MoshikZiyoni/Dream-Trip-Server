from django.shortcuts import render
import os
import openai
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import QueryChatGPT
import json

@api_view(['GET', 'POST'])
def gpt_func(request):
    # print (request.data)
    query = QueryChatGPT()

    ourmessage=f"Can you provide a JSON-formatted itinerary for a {request.data['budget']} {request.data['durring']}-day {request.data['travelers']} vacation in {request.data['mainland']}, including the country, city, description, and attractions for each city?"
    query.question = ourmessage


    # Load your API key from an environment variable or secret management service
    openai.api_key = 'API_KEY'
    model_id = 'gpt-3.5-turbo'

    def ChatGPT_conversation(conversation):
        response = openai.ChatCompletion.create(
            model=model_id,
            messages=conversation
        )
        conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
        return conversation 

    conversation = []
    conversation.append({'role': 'system', 'content': 'How may I help you?'})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

    prompt = (ourmessage)
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)
    our_answer=('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
    
    query.answer = our_answer
    ##Save to DATABASE
    query.save()
    start_index = our_answer.find('{')
    end_index = our_answer.rfind('}') + 1
    json_string = our_answer[start_index:end_index]
    data = json.loads(json_string)
    print (data)
    return Response(data)
    # return  Response('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
