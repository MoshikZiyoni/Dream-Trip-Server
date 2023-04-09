from django.shortcuts import render
import os
import openai
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def gpt_func(request):
    ourmessage = list(request.data.keys())[0]

    print('this is the request print',ourmessage)
    # Load your API key from an environment variable or secret management service
    openai.api_key = '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'
    model_id = 'gpt-3.5-turbo'

    def ChatGPT_conversation(conversation):
        response = openai.ChatCompletion.create(
            model=model_id,
            messages=conversation
        )
        # api_usage = response['usage']
        # print('Total token consumed: {0}'.format(api_usage['total_tokens']))
        # stop means complete
        # print(response['choices'][0].finish_reason)
        # print(response['choices'][0].index)
        conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
        return conversation 

    conversation = []
    conversation.append({'role': 'system', 'content': 'How may I help you?'})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

    prompt = (ourmessage)
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)
    return  Response('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

    # return Response({'response': conversation[-1]['content']})

