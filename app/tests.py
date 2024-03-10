
# import json
# import requests
# from dotenv import load_dotenv
# import os
# load_dotenv()

# api_key=os.environ.get('FOURSQUARE')
# print(api_key)

# def foursquare_hotels(landmarks):

#     url = "https://api.foursquare.com/v3/places/search?"

#     headers = {
#         "accept": "application/json",
#         "Authorization": api_key+'='
#     }
#     params= {
#         'categories':'19014',
#         "ll" :  f"{landmarks[0]},{landmarks[1]}",
#         'radius':5000,
#         'limit' : 20,
        
#         'fields':'geocodes,name,rating,website,photos,hours,location,tel,description,tips'
#     }
#     response = requests.get(url, params=params,headers=headers,timeout=5)

#     response_text=(response.text)
#     jsonto=json.loads(response_text)
#     print(jsonto)
#     # reslut=jsonto['results']
#     # return (reslut)
# foursquare_hotels(landmarks=["32.0853","34.7818"])




from email.mime.base import MIMEBase
import smtplib
from email.message import EmailMessage
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders


sender_email = "outseerofflinemail@gmail.com"  # Your Gmail address
# receiver_email = "AFCC@rsa-otms.com"
receiver_email = "moshiktm1994@gmail.com"

subject = "Reminder: Check the offline txt"
body = "Plesae check the txt file called 'URL-to-check-Offline' in Check offline scripts folder."
smtp_password = "Gr33tings1!"
smtp_username = "outseerofflinemail@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))
filename='URL-to-check-Offline.txt'
attachment = open(filename,'rb')
attachment_packge=MIMEBase('application','octet-stream')
attachment_packge.set_payload((attachment).read())
encoders.encode_base64(attachment_packge)
attachment_packge.add_header('Content-Disposition','attachment; filename= '+ filename)
message.attach(attachment_packge)

context = ssl.create_default_context()

try:
    print('connecting')
    TIE_server=smtplib.SMTP(smtp_server,smtp_port)
    TIE_server.starttls(context=context)
    TIE_server.login(sender_email,'zntwvcjihalclfbq')
    print('Connected')
    print()
    TIE_server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(e)

