# def extract_restaurants_data(attractions):
#         geolocator = Nominatim(user_agent="dream-trip")


#         # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
#         user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0"

#         # Set up the Chrome WebDriver with User-Agent and headless mode
#         chrome_options = webdriver.ChromeOptions()
#         # chrome_options.add_argument(f"user-agent={user_agent}")
#         # chrome_options.add_argument("--headless")  # Run in headless mode
#         random_time = random.uniform(3,6)

#         # Create a Chrome WebDriver instance
#         # service_path = "C:/Users/moshi/Downloads/chromedriver.exe"
#         # service = Service(service_path)
#         driver = webdriver.Chrome( options=chrome_options)
#         # Initialize the WebDriver (in this case, using Chrome)
#         cities_list=['Las Vegas', 'Brașov', 'Cluj-Napoca', 'Boquete','Kandy']
#         for attraction_data in attractions:
#             city = attraction_data["city"]
#             # if city not in cities_list:
#             #     print ('continue')
#                 # continue
            
#             name = attraction_data["name"]
#             description=attraction_data["description"]
#             normalized_city_name = unidecode(city)
#             try:
#                 formatted_address=attraction_data["formatted address"]
#             except:
#                 pass
#             try:
#                 formatted_address=attraction_data["formatted_address"]
#             except:
#                 pass
#             try:
#                 city_objs = City.objects.filter(city=city).first()
#                 if not city_objs:
#                     print ('no regular')
#                     normalized_city_name = normalized_city_name.strip()
#                     print(normalized_city_name)
#                     city_objs = City.objects.filter(Q(city__iexact=normalized_city_name) | Q(city__icontains=normalized_city_name)).first()
#                 if city_objs:
#                     print(city_objs.city)
#                     print(name)
                
#             except:
                    
#                     words = formatted_address.split()
#                     last_word = words[-1]
#                     last_word = last_word.strip('",)')
#                     location = geolocator.geocode(f"{last_word}")
#                     if location:
#                         landmarks = [location.latitude, location.longitude]
#                         print (landmarks)
#                         city_query = City(
#                         city=city,
#                         latitude=landmarks[0],
#                         longitude=landmarks[1],
#                         )
#                         city_query.save()
#                         city_objs = City.objects.filter(city=city).first()
#                     else:
#                         print(f"Could not geocode: {last_word}")
#             check_name=Attraction.objects.filter(name=name,city_id=city_objs.id).first()
                    
#             if not check_name:
                
                
#                 latitude= attraction_data["latitude"] if attraction_data["latitude"] else ""
#                 longitude= attraction_data["longitude"] if attraction_data["longitude"] else ""
#                 name_for_flicker=f"{name}, {city}"
                
#                 # driver.get(f"google.com/search?tbm=isch&q={name_for_flicker}")
#                 driver.get(f"https://www.google.com/search?tbm=isch&q={name_for_flicker}")
#                 # /html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img
#                 time.sleep(random_time)
#                 first_image = driver.find_element(By.XPATH,"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img").get_attribute('src')
                
#                 # first_image=""
#                 # photos=""
#                 # if len(first_image)>2:
#                 base64_data = first_image.split(',')[1]
#                     # Remove any whitespace characters from the base64 data
#                 base64_data = ''.join(base64_data.split())
#                 # image_data = first_image.split(',')[1].encode()
#                 url = "https://api.imgbb.com/1/upload"
#                 api_key = os.environ.get('imgbb')
#                 payload = {
#                     "key": api_key,
#                     "image": base64_data,
#                 }
#                 response = requests.post(url, payload)
#                 print (response.text)
#                 photos=(response.json()["data"]["url"])

#                 # image_data = base64.b64decode(first_image.split(',')[1])
#                 # headers = {
#                 #     # "Authorization": "Client-ID 92a43ec7ca67375" 
#                 #     "Authorization": "Client-ID ffa26035d00c21a" 

#                 # }
#                 # url = "https://api.imgur.com/3/image"
#                 # response = requests.post(url, headers=headers, data=image_data)
#                 # imgur_response = json.loads(response.text)
#                 # print (imgur_response)
#                 # # Get image link
#                 # image_link = imgur_response['data']['link']
#                 # photos=(image_link)
#                 # # photos = flickr_api(name=name_for_flicker, latitude=latitude, longitude=longitude)
#                 # if photos==None:
#                 #     photos=""
#                 print (photos,'@@@@@',name)
#                 review_score= attraction_data["review_score"] if attraction_data["review_score"] else ""
#                 website = attraction_data.get("website", "")
#                 try:
#                     hours= attraction_data["hours"] 
#                 except:
#                     hours=""
#                 real_price= attraction_data["real_price"] if attraction_data["real_price"] else ""
#                 # category=attraction_data["category"] if attraction_data["category"] else ""
                

#                 try:
#                     tel=attraction_data['telephone']
#                 except:
#                     tel=""
#                 website= website or ""
#                 try:
#                     tips=attraction_data["tips"]
#                     if isinstance(tips, list):
#                         pass
#                     elif isinstance(tips, str):
#                         tips_list = [tip.strip() for tip in re.split(r'\d+\.', tips) if tip.strip()]
#                         tips=tips_list
#                         print (tips)
#                 except Exception as e:
#                     tips= ""
#                     print(e)
                
#                 # print (name,latitude,longitude,review_score,description,website,hours,distance,real_price,tips,formatted_address)
                
#                 if city_objs:
#                     try:
#                         print (city_objs.id,'AAAAAAA')
#                         # city_obj = city_objs[0]
#                         # print (city_objs.id,'AAAAAAA')
#                         atrc_query = Attraction(
#                         name=name,
#                         city=city_objs,
#                         latitude=latitude,
#                         longitude=longitude,
#                         description=description,
#                         review_score=review_score,
#                         website=website,
#                         real_price=real_price,
#                         hours=hours,
#                         tel=tel,
#                         address=formatted_address,
#                         tips=tips,
#                         photos=photos)
                    
#                         atrc_query.save()
#                         print("Save attraction successfully")
#                     except Exception as e:
#                         print('not good 227 ',e)



#     extract_restaurants_data(attractions=[
   
    

# ])
#     return 'kk'