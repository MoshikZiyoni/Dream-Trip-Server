from django.shortcuts import render
import os
import openai
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import QueryChatGPT
import json

@api_view(['GET', 'POST'])
def gpt_func(request):
    query = QueryChatGPT()

    question2='{country,cities:[{city:,description:,attraction:[name:],travelDay:}]}'
    ourmessage=f"Can you provide me a Trip to {request.data['mainland']} ,for {request.data['travelers']} trip,budget {request.data['budget']} {request.data['durring']},return me as format {question2}"
    print(ourmessage)
    query.question = ourmessage

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.environ.get('API_KEY')
    # openai.api_key ='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'
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
    try:
        start_index = our_answer.find('{')
        end_index = our_answer.rfind('}') + 1
        json_string = our_answer[start_index:end_index]
        data = json.loads(json_string)
        return Response(data)
    except (ValueError, KeyError, TypeError) as e:
        # Catch specific exceptions that might be raised by json.loads()
        return Response({'error': str(e)})
    except Exception as e:
        # Catch any other exceptions
        return Response({'error': str(e)})
    # return  Response('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))



# @api_view(['GET', 'POST'])
# def all_country(request):
#     country_name=request.data['country']
#     country = Country(country_name=country_name)
#     country.save()



    