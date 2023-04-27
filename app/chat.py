import os
import time
import openai

from app.models import QueryChatGPT


# def run_gpt_func(conversation,first_prompt):
def run_long_poll(ourmessage):
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
    try:
        start_time = time.time()
        while time.time() - start_time < 60:
            openai.api_key = os.environ.get('API_KEY')
            print ('satrt GPT')
            completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": ourmessage}
        ]
        )
        if (completion.choices[0].message.content):
            answer=(completion.choices[0].message.content)
            query = QueryChatGPT(question=ourmessage, answer=answer)
            query.save()
            print (answer)
            return answer
        time.sleep(3)

    except:
        answer = "I'm sorry, I could not generate a response. Please try again later."
        return('Error generating answer with GPT-3.')
    
    


#     print ('start 3.5')
#     response = openai.ChatCompletion.create(
#         model='gpt-3.5-turbo',
#         messages=conversation
#     )
#     conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
#     return conversation

# # first_prompt = 'Give me a summarization Trip with attraction to Argentina, for Family trip, budget Premium 5 days in JSON'
# # second_prompt = 'Can you return me in the following JSON structure "country": "..", "cities": [{"city": "", "description": "", "attractions": [{"name": "", "description": ""}], "travelDay": 0}]'
# first_prompt = 'Give me a summarization Trip to Argentina, for Family trip, budget Premium 5 days return me in the following JSON structure "country":"..","cities":[{"city":"","description":"","travelDay": 0}] no more than 1000 tokens'
# second_prompt = 'Can you return also attractions for each city like ,"attractions":["name":]["descrpition":]'


# conversation = []
# conversation.append({'role': 'user', 'content':first_prompt })
# conversation = run_gpt_func(conversation,first_prompt)
# print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
# conversation.append({'role': 'user', 'content': second_prompt})
# conversation = run_gpt_func(conversation, first_prompt)
# print(conversation[-1]['content'].strip())
