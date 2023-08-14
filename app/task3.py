
import json
import requests
from urllib.parse import quote
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import os
import time
import flickrapi

from models import Restaurant
load_dotenv()




# from trip_advisor import foursquare_restaurant

# landmarks=[48.8534951,2.3483915]
# print(foursquare_restaurant(landmarks))



