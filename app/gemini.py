import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
google_gemini_api_key = os.environ.get("google_gemini_key")

def chat_gemini(message):
    genai.configure(api_key=google_gemini_api_key)
    generation_config = {
      "temperature": 0.9,
      "top_p": 1,
      "top_k": 1,
      "max_output_tokens": 2048,
    }

    safety_settings = [
    #   {
    #     "category": "HARM_CATEGORY_HARASSMENT",
    #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    #   },
    #   {
    #     "category": "HARM_CATEGORY_HATE_SPEECH",
    #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    #   },
    #   {
    #     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    #   },
    #   {
    #     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    #   },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    convo.send_message(message)
    print(convo.last.text)
    return(convo.last.text)

