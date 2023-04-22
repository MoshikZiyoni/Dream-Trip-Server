# from app.models import QueryChatGPT
# import os
# import openai
# import time
# import datetime

# MAX_RETRIES = 3
# WAIT_TIME = 5
# TIMEOUT = 35  # maximum time to wait for the result, in seconds

# def run_gpt_func(ourmessage):
# #     try:
# #         answer_from_data = QueryChatGPT.objects.filter(question__exact=ourmessage)
# #         if answer_from_data.exists():
# #             data = answer_from_data.values('answer')[0]
# #             answer = data['answer']
# #             print('answer in data')
# #             return answer
# #         else:
# #             print('Not Found')
# #     except:
# #         print('Internal Server Error')
    
# #     query = QueryChatGPT()
# #     query.question = ourmessage
    
#     openai.api_key = os.environ.get('API_KEY')
    

    
#     try_count = 0
#     while try_count < MAX_RETRIES:
#         try:
#             start_time = datetime.datetime.now()
#             completion = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo-0301",
#                 messages=[
#                     {"role": "user", "content": ourmessage}
                    
#                 ]
#             )
#             ourdata = (completion.choices[0].message.content)

#             # query.answer = ourdata
#             # query.save()

#             return ourdata

#         except Exception as e:
#             print(f"An error occurred in try {try_count+1}: {e}")
#             try_count += 1
#             time.sleep(WAIT_TIME)
        
#         # check if the maximum time has elapsed
#         elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
#         if elapsed_time >= TIMEOUT:
#             print(f"Timeout ({TIMEOUT}s) exceeded, returning None,moshikerror")
#             return None
    
#     # if we get here, it means all attempts failed
#     print("Maximum number of retries reached, returning None,moshikerror2")
#     return None
