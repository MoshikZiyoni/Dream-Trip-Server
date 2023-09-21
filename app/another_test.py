# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import threading
# import random
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import base64
import requests
# import json


import json
def my_night_life(landmarks):
    url=''
    query={
        "city":"tel aviv",
        "latitude": landmarks[0],
        "longitude": landmarks[1], 
		
    }
	
    response = requests.post(url, json=query)
	
    response_text=(response.text)
    jsonto=json.loads(response_text)
    print(jsonto)
    return jsonto


my_night_life(landmarks=[32.080168,34.780909])