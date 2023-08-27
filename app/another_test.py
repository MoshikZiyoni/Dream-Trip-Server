# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import threading
# import random
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import base64
# import requests
# import json
# # random_time = random.uniform(5, 20)

# ['Afghanistan', 'Albania', 'Antigua and Barbuda', 'Armenia', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Benin', 'Bhutan', 'Bosnia and Herzegovina', 'Botswana', 'Brunei', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Central African Republic', 'Chad', 'Chile', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'Gabon', 'Gambia', 'Georgia', 'Ghana', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Jamaica', 'Jordan', 'Kazakhstan', 'Kiribati', 'Korea, North', 'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Micronesia', 'Moldova', 'Monaco', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Egypt', 'Bulgaria', 'Spain', 'Angola', 'Greece', 'Japan', 'China', 'Andorra', 'Australia', 'Canada', 'Germany', 'France', 'Kenya', 'Argentina', 'Mexico', 'Bolivia', 'Belgium', 'Taiwan', 'Tajikistan', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe', 'USA', 'South Korea', 'Czechia', 'Puerto Rico', 'Peru/Bolivia', 'Mongolia', 'The Bahamas', 'spain', 'israel', 'Brazil', 'Tanzania', 'Belize', 'Austria', 'Uganda', 'Algeria', 'Thailand', 'greece', 'Israel', 'brazil', 'italy', 'Italy']



# return me the avrage price in USD for trip in this countires return me as list json [{country:"",avrage price:""}]