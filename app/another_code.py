#     sss=[
# ]
#     restaurnt_without__price = Attraction.objects.filter(tips__isnull=True) | Attraction.objects.filter(tips='')
#     for attraction in restaurnt_without__price:
#         # for i in sss:
#         #     if i["Name"]==attraction.name:
#         #         my_tips=i.get("tips") or i.get("Tips") 
#         #         attraction.tips=my_tips
#         #         attraction.save()
#         #         print ('success')

#         with open('tips.txt', 'a', encoding='utf-8') as f:
#             data_to_write = f"Name: {attraction.name}, City: {attraction.city.city}\n"
#             f.write(data_to_write)
#         # attraction.save()
#         # print ("save sucees")
#     # print(attraction.description,'------',attraction.city.city)  
#     return 'kk'



    # s=City.objects.all().values()
    # for  i in s:
    #     with open('cities.txt', 'a', encoding='utf-8') as f:
    #         f.write(str(i) + ',\n')
    # return 'kk'
    # city1=City.objects.all()
    # cities=[]x
    # for i in city1:
    #     cities.append(i.city)
    # print(cities)
    # from django.db.models import Count
    # attrac=Attraction.objects.filter(name='Eiffel Tower').first()
    # attrac.photos='https://lh3.googleusercontent.com/p/AF1QipOTdWRhZoy5lJGdxy_ir-mQsy6N3O6CYLaOj0vC=s1360-w1360-h1020'
    # attrac.save()
    
   

    # thread_poe = threading.Thread(target=poe)
    # thread_poe1 = threading.Thread(target=poe1)
    # thread_poe2 = threading.Thread(target=poe2)
    # thread_poe3 = threading.Thread(target=poe3)
    # thread_poe4 = threading.Thread(target=poe4)
    # # Start the threads
    # thread_poe.start()
    # thread_poe1.start()
    # thread_poe2.start()
    # thread_poe3.start()
    # thread_poe4.start()
    # # Wait for both threads to complete
    # thread_poe.join()
    # thread_poe1.join()
    # thread_poe2.join()
    # thread_poe3.join()
    # thread_poe4.join()

    # print("Both threads have completed.")
    # return 'kk'
    


   
    # from django.db.models import Count
    # attractions = Restaurant.objects.filter(place_id__isnull=False)
    # count=0
    # cities_list =set()
    # for attrac in attractions:
    #     print(attrac.name,attrac.place_id)
    #     cities_list.add(attrac.city.city)
    #     count+=1
    # print (count)
    # print(cities_list)
    # return 'kk'
    
    # # Get the count of matching attractions
    # count = attractions.count()

    # # Get a set of unique cities among the matching attractions
    # cities = attractions.values('city__city').distinct()

    # # Print the results
    # print(count)
    # print(cities)
   

  
    # cities_without_hotels = City.objects.filter(hotels__isnull=True)

    # for city in cities_without_hotels:
    #     print(city.city)
    #     try:
    #         landmarks=[city.latitude,city.longitude]
    #         result=foursquare_hotels(landmarks)
    #         hotels= []
    #         if len(result) == 0:
    #             continue
    #         for hotel in result:
    #             process_hotel(hotel=hotel, city_obj=city, hotels=hotels)    
    #     except Exception as e:
    #         print ('NOT GOOOODDDDDDDDDDDDDDDDDD',e)

    # return 'ok'



#     attractions_with_price = Attraction.objects.filter(real_price="['price']")
#     for attraction in attractions_with_price:
#         print(attraction.name)
# # Extract all the real_price values for these attractions
#     real_prices = attractions_with_price.values_list('real_price', flat=True)

#     # Convert the result to a list if needed
#     real_prices_list = list(real_prices)

#     # Now you have a list of all the real_price values where price is equal to 'price'
#     # print(real_prices_list)

        
#     return 'ok'


#     def qiuick_attraction+restarunt(cities_data):
#         for data in cities_data:
#                 country= (data['country'])
#                 try:
#                     existing_country = Country.objects.filter(name=country).first()
#                     country_id = existing_country.id
#                 except:
#                     print ('country not exist')
#                     country_query=Country(name=country)
#                     country_query.save()
#                     existing_country = Country.objects.filter(name=country).first()
#                     country_id = existing_country.id
#                     print (country_id)
                
#                 city=data['city']
#                 latitude=data['latitude']
#                 longitude=data['longitude']
#                 landmarks=[latitude,longitude]
#                 description=data['description']
#                 city_obj=City.objects.filter(city=city).first()
#                 if city_obj:
#                     print ('continue')
#                     continue
#                     try:
#                         result1=foursquare_attraction(city_name=city,landmarks=landmarks,country=country)
#                         attractions=[]
#                     except:
#                         print ('no attraction')
#                     try:
#                         for attrac in result1:
#                             process_attraction(attrac, city_obj, attractions)
#                     except:
#                         print ('no attraction1')
#                     try:
#                         result=foursquare_restaurant(landmarks)
#                         for resta in result:
#                             restaurants=[]
#                             process_restaurant(resta,city_obj,restaurants)
#                     except:
#                         print ('no restarunt')
#                 else:
#                     city_query = City(
#                     country_id=country_id,
#                     city=city,
#                     latitude=latitude,
#                     longitude=longitude,
#                     description=description,
#                 )
#                     city_query.save()
#                     print("Save successfully for city")
#                     try:
#                         result1=foursquare_attraction(city_name=city,landmarks=landmarks,country=country)
#                         attractions=[]
#                     except:
#                         print ('no attraction')
#                     try:
#                         for attrac in result1:
#                             process_attraction(attrac, city_obj, attractions)
#                     except:
#                         print ('no attraction1')
#                     try:
#                         result=foursquare_restaurant(landmarks)
#                         for restaur in result:
#                             restaurants=[]
#                             process_restaurant(restaur,city_obj,restaurants)
#                     except:
#                         print ('no restarunt')


#     attraction_list=[
# ]


    # restaurnt_without__price = Attraction.objects.filter(description__isnull=True) | Attraction.objects.filter(description='')
    # for attraction in restaurnt_without__price:
    #     print(attraction.name,'------',attraction.city.city)  
    # return 'ok' 




#     restaurnt_without__price = Attraction.objects.filter(name__isnull=True) | Attraction.objects.filter(name='')
#     for attraction in restaurnt_without__price:
#         # for attr in attraction_list:
#         #     if attr["description"] == attraction.description:
#         #         attraction.name = attr["name"]
#         #         attraction.save()
#         #         print ("save sucees")
#         print(attraction.description,'------',attraction.city.city)  
#     return 'ok'  

    # restaurnt_without__price = Restaurant.objects.filter(price__isnull=True) | Restaurant.objects.filter(price='')
    # for attraction in restaurnt_without__price:
    #     print(attraction.name,'------',attraction.city.city)  
    # return 'ok'  

#     def excract_restaurant(attractions_listt):
#         for attrac in attractions_listt:
#             name= (attrac['name'])
#             new_price=attrac['price']
#             print(new_price)
#             try:
#                 attrac=Restaurant.objects.get(name=name)
#                 print (attrac.id,attrac.price)
#                 attrac.price=new_price
#                 attrac.save()
#                 print ('save success')
#                 attraction = Restaurant.objects.get(pk=attrac.id)
#                 print(attraction.price) 
#             except Exception as e:
#                 print(f'attrac not exsit,{name},{attrac},{e}')
                
#                 dupes = Restaurant.objects.filter(name=name)
#                 if dupes:
#                     # Keep the first one  
#                     keep = dupes[0] 
                    
#                     # Delete the rest
#                     for dupe in dupes[1:]:
#                         dupe.delete()
                        
#                     # Use the kept attraction
#                     attrac = keep 
#                     print ('deleteddddddddddddddddddddddddd')
#                     # Update price 
#                     attrac.price = new_price
#                     attrac.save()


#     excract_restaurant(attractions_listt=[

# ])
   
#     return 'kk'
 


    # attractions_without_real_price = Attraction.objects.filter(real_price__isnull=True) | Attraction.objects.filter(real_price='')
    # for attraction in attractions_without_real_price:
    #     if 'Ristorante' in attraction.name or 'Restaurant' in attraction.name:
    #         attraction.delete()
    #         print('delete')
    #     print(attraction.name,",",attraction.city.city)  
    # return 'ok'  
   
#     def excract_attraction(attractions_listt):
#         for attrac in attractions_listt:
#             name= (attrac['name'])
#             new_price=attrac['price']
#             print(new_price)
#             try:
#                 attrac=Attraction.objects.get(name=name)
#                 print (attrac.id,attrac.real_price)
#                 attrac.real_price=new_price
#                 attrac.save()
#                 print ('save success')
#                 attraction = Attraction.objects.get(pk=attrac.id)
#                 print(attraction.real_price) 
#             except Exception as e:
#                 print(f'attrac not exsit,{name},{attrac},{e}')
                
#                 dupes = Attraction.objects.filter(name=name)
#                 if dupes:
#                     # Keep the first one  
#                     keep = dupes[0] 
                    
#                     # Delete the rest
#                     for dupe in dupes[1:]:
#                         dupe.delete()
                        
#                     # Use the kept attraction
#                     attrac = keep 
#                     print ('deleteddddddddddddddddddddddddd')
#                     # Update price 
#                     attrac.real_price = new_price
#                     attrac.save()
#     excract_attraction(attractions_listt=[

# ])


   
#     return 'kk'

#     def extract_attraction_data(attractions):
#         try:
           
#             user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"

#             # Set up the Chrome WebDriver with User-Agent and headless mode
#             chrome_options = webdriver.ChromeOptions()
#             chrome_options.add_argument(f"user-agent={user_agent}")
#             # chrome_options.add_argument("--headless")  # Run in headless mode
#             random_time = random.uniform(3,6)

#             # Create a Chrome WebDriver instance
#             # service_path = "C:/Users/moshi/Downloads/chromedriver.exe"
#             # service = Service(service_path)
#             driver = webdriver.Chrome( options=chrome_options)
#             # Initialize the WebDriver (in this case, using Chrome)
#             for attraction_data in attractions:
#                 city = attraction_data["city"]
#                 name = attraction_data["name"]
#                 normalized_city_name = unidecode(city)
#                 try:
#                     city_objs = City.objects.filter(city=city).first()
#                     print(city_objs.city)
#                 except:
#                     print ('no regular')
#                     normalized_city_name = normalized_city_name.strip()
#                     city_objs = City.objects.filter(Q(city__iexact=normalized_city_name) | Q(city__icontains=normalized_city_name)).first()
#                 check_name=Attraction.objects.filter(name=name,city_id=city_objs.id).first()
                      
#                 if not check_name:  
#                     latitude= attraction_data["latitude"]
#                     longitude= attraction_data["longitude"]
#                     name_for_flicker=f"{name}, {city}"
#                     try:
#                         driver.get(f"https://www.google.com/search?tbm=isch&q={name_for_flicker}")
#                         first_image = driver.find_element(By.XPATH,"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img").get_attribute("src")
#                     except:
#                         first_image=""
#                         photos=""
#                     if len(first_image)>2:
#                         image_data = first_image.split(',')[1].encode()
#                         url = "https://api.imgbb.com/1/upload"
#                         api_key = '670a51c4852893f80aa46108e03e0bbc'
#                         payload = {
#                             "key": api_key,
#                             "image": image_data,
#                         }
#                         response = requests.post(url, payload)
#                         print (response.text)
#                         photos=(response.json()["data"]["url"])
#                     # photos = flickr_api(name=name_for_flicker, latitude=latitude, longitude=longitude)
#                     # if photos==None:
#                     #     photos=""
#                     # print (photos,'@@@@@',name)
#                     review_score= attraction_data["review_score"]
#                     description = attraction_data["description"]
#                     website= attraction_data["website"]
#                     try:
#                         hours= attraction_data["hours"]
#                     except:
#                         hours=""
#                     distance = attraction_data["distance"]
#                     real_price = attraction_data["real_price"]
#                     try:
#                         formatted_address=attraction_data["formatted address"]
#                     except:
#                         pass
#                     try:
#                         formatted_address=attraction_data["formatted_address"]
#                     except:
#                         pass

#                     try:
#                         tel=attraction_data['telephone']
#                     except:
#                         tel=""
#                     website= website or ""
#                     try:
#                         tips=attraction_data["tips"]
#                         if isinstance(tips, list):
#                             pass
#                         elif isinstance(tips, str):
#                             tips_list = [tip.strip() for tip in re.split(r'\d+\.', tips) if tip.strip()]
#                             tips=tips_list
#                             print (tips)
#                     except:
#                         tips= ""
                    
#                     # print (name,latitude,longitude,review_score,description,website,hours,distance,real_price,tips,formatted_address)
                    
#                     if city_objs:
#                         try:
#                             print (city_objs.id,'AAAAAAA')
#                             # city_obj = city_objs[0]
#                             # print (city_objs.id,'AAAAAAA')
#                             atrc_query = Attraction(
#                             name=name,
#                             city=city_objs,
#                             latitude=latitude,
#                             longitude=longitude,
#                             photos=photos,
#                             review_score=review_score,
#                             description=description,
#                             website=website,
#                             hours=hours,
#                             distance=distance,
#                             real_price=real_price,
#                             address=formatted_address,
#                             tips=tips,
#                             tel=tel
#                         )
#                             atrc_query.save()
#                             print("Save attraction successfully")
#                             with open('attractions_saved.txt', 'a', encoding='utf-8') as f:
#                                 f.write(name + '\n')
#                         except Exception as e:
#                             print (e)

#                     else:
#                         print ("no city obj")
#                         with open('attractions_not_saved.txt', 'a', encoding='utf-8') as f:
#                             f.write(name + '\n')
#                 else:
#                     print ('there is the attrac already')
#         except Exception as e:
#             print (e)


#     extract_attraction_data( attractions=[
	

	
# ]
# )

#     return 'ok'


    # def extract_restaurants_data(attractions):
        
    #     try:
    #         user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"

    #         # Set up the Chrome WebDriver with User-Agent and headless mode
    #         chrome_options = webdriver.ChromeOptions()
    #         chrome_options.add_argument(f"user-agent={user_agent}")
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
    #             normalized_city_name = unidecode(city)
    #             try:
    #                 city_objs = City.objects.filter(city=city).first()
    #                 print(city_objs.city)
    #             except:
    #                 print ('no regular')
    #                 normalized_city_name = normalized_city_name.strip()
    #                 city_objs = City.objects.filter(Q(city__iexact=normalized_city_name) | Q(city__icontains=normalized_city_name)).first()
    #             check_name=Restaurant.objects.filter(name=name,city_id=city_objs.id).first()
                      
    #             if not check_name:
    #                 time.sleep(random_time)
                    
    #                 latitude= attraction_data["latitude"]
    #                 longitude= attraction_data["longitude"]
    #                 name_for_flicker=f"{name} restaurant, {city}"
    #                 try:
    #                     driver.get(f"https://www.google.com/search?tbm=isch&q={name_for_flicker}")
    #                     first_image = driver.find_element(By.XPATH,"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img").get_attribute("src")
    #                 except:
    #                     first_image=""
    #                     photos=""
    #                 if len(first_image)>2:
    #                     image_data = first_image.split(',')[1].encode()
    #                     url = "https://api.imgbb.com/1/upload"
    #                     api_key = '0ceb697fbeb4ad555cad07deddcbf4f4'
    #                     payload = {
    #                         "key": api_key,
    #                         "image": image_data,
    #                     }
    #                     response = requests.post(url, payload)
    #                     print (response.text)
    #                     photos=(response.json()["data"]["url"])

    #                 # image_data = base64.b64decode(first_image.split(',')[1])
    #                 # headers = {
    #                 #     "Authorization": "Client-ID 92a43ec7ca67375" 
    #                 # }
    #                 # url = "https://api.imgur.com/3/image"
    #                 # response = requests.post(url, headers=headers, data=image_data)
    #                 # imgur_response = json.loads(response.text)
    #                 # print (imgur_response)
    #                 # # Get image link
    #                 # image_link = imgur_response['data']['link']
    #                 # photos=(image_link)
    #                 # photos = flickr_api(name=name_for_flicker, latitude=latitude, longitude=longitude)
    #                 if photos==None:
    #                     photos=""
    #                 print (photos,'@@@@@',name)
    #                 review_score= attraction_data["review_score"]
    #                 website= attraction_data["website"]
    #                 try:
    #                     hours= attraction_data["hours"]
    #                 except:
    #                     hours=""
    #                 price_range= attraction_data["price_range"]
    #                 category=attraction_data["category"]
    #                 try:
    #                     formatted_address=attraction_data["formatted address"]
    #                 except:
    #                     pass
    #                 try:
    #                     formatted_address=attraction_data["formatted_address"]
    #                 except:
    #                     pass

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
    #                         atrc_query = Restaurant(
    #                         name=name,
    #                         city=city_objs,
    #                         latitude=latitude,
    #                         longitude=longitude,
    #                         photos=photos,
    #                         review_score=review_score,
    #                         website=website,
    #                         hours=hours,
    #                         category=category,
    #                         price=price_range,
    #                         address=formatted_address,
    #                         tips=tips,
    #                         tel=tel
    #                     )
    #                         atrc_query.save()
    #                         print("Save attraction successfully")
    #                         with open('restaurants_saved.txt', 'a', encoding='utf-8') as f:
    #                             f.write(name + '\n')
    #                     except Exception as e:
    #                         print (e)

    #                 else:
    #                     print ("no city obj")
    #                     with open('restaurants_not_saved.txt', 'a', encoding='utf-8') as f:
    #                         f.write(name + '\n')
    #             else:
    #                 print ('there is the attrac already')
    #     except Exception as e:
    #         print (e,'erorrrrrr')
    # extract_restaurants_data(attractions  = [
  
 



  
    # ])
    # return 'ok'


    # def city_has_few_attractions():
    #     cities_with_few_attractions = []

    #     # Get all cities and their attraction count using the Django ORM
    #     cities = City.objects.all()

    #     for city in cities:
    #         # Count the number of attractions for each city
    #         attraction_count = city.attractions.count()

    #         # Check if the city has fewer than 10 attractions
    #         if attraction_count < 10:
    #             cities_with_few_attractions.append({"city":city.city,"lat":city.latitude,"lon":city.longitude,"city_obj":city.id})

    #     return cities_with_few_attractions
    # print(city_has_few_attractions())
    # return 'ko'


   
    # # attrac=Attraction.objects.filter(city_id=345).values()
    # # for i in attrac:
    # #     print(i)
    # # return 'ok'
    # # print("Cities without restaurants:")
    # for city in cities_without_restaurants:
    #     print({"city":city.city,"city_obj":city.id,"lat":city.latitude,"lon":city.longitude},',')

    # return 'ok'

   
    # QueryChatGPT.objects.all().delete()
    
    # City.objects.all().delete()
    # Attraction.objects.all().delete()
    # Restaurant.objects.all().delete()
    

   # from django.db.models import Count
# from django.db import transaction

# attractions = Attraction.objects.values('name').annotate(name_count=Count('name')).filter(name_count__gt=1)


    # for attraction in attractions:
    #     name = attraction['name']
    #     duplicates = Attraction.objects.filter(name=name).order_by('id')

    #     city_ids = set(duplicates.values_list('city_id', flat=True))

    #     with transaction.atomic():
    #         for city_id in city_ids:
    #             city_duplicates = duplicates.filter(city_id=city_id)

    #             # Print the duplicates in the same city
    #             delete_list = city_duplicates.exclude(id=city_duplicates.first().id)
    #             for duplicate in delete_list:
    #                 print(f"Deleting duplicate: {duplicate.name}, City ID: {duplicate.city_id}")

    #             # Delete all duplicates except the first one per city (on commit)
    #             delete_list.delete()
    # # return 'ok'