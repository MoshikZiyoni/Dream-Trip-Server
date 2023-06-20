 # try:
                        #     if isinstance(landmarks, list):
                        #         print ('this is a list')
                        #         if len(landmarks)>2:
                        #             print (landmarks,'sucess to landmapr 0')
                        #             landmarks = landmarks[0]
                        #             test_a=7
                        #         else:
                        #             print('skip landmarks')
                        # except:
                        #         print('not list')
                        # try:
                        #     latitude = city_data['landmarks']['latitude']
                        #     longitude = city_data['landmarks']['longitude']
                        #     landmarks = [latitude, longitude]
                        #     print('NEW PRINT FOR LANDMARKS')
                        # except:
                        #         print('not good')






# city_name = city_data ['city']
                        # description = city_data ['description']
                        # location = geolocator.geocode(f"{city_name},{country}")
                        # landmarks=[location.latitude, location.longitude]
                        # existing_city = City.objects.filter(city=city_name).first()
                        # if existing_city:
                        #     # Add attractions and restaurants to city_data dictionary
                        #     attract=Attraction.objects.filter(city_id=existing_city.id).values()
                        #     attractions_list = list(attract)
                        #     city_data['attractions'] = attractions_list
                        #     restaura=Restaurant.objects.filter(city_id=existing_city.id).values()
                        #     restaurants_list = list(restaura)
                        #     city_data['restaurants']=restaurants_list
                        #     print ('continue')
                        #     continue
                        
                        # print("City:", city_name, landmarks)
                        # if not existing_city:
                        #     city_query = City(country=country,city=city_name, latitude=landmarks[0], longitude=landmarks[1],description=description)
                        #     city_query.save()
                        #     print ('save successefuly for city')
                        # city_to_save=City.objects.filter(city=city_name)

                        
                        # reslut=foursquare_restaurant(landmarks)
                        # restaurants=[]
                        # if len(reslut) == 0:
                        #     restaurant_=trip_advisor_restaurants(city_name,country,landmarks)
                        #     restaurants.append(restaurant_)
                        # else:
                        #     for i in reslut:
                                
                        #         name= (i['name'])
                        #         latitude = i['geocodes']['main']['latitude']
                        #         longitude = i['geocodes']['main']['longitude']
                        #         flickr_photos1=flickr_api(name,latitude,longitude)
                        #         goog_result1=google_search(f"{name},{city_name},{country}")
                                
                        #         restaurants_info={
                        #             'name':name,
                        #             'latitude':latitude,
                        #             'longitude':longitude,
                        #             'photos':flickr_photos1,
                        #             'review_score': goog_result1['review_score'],
                        #         }
                        #         restaurants.append(restaurants_info)
                        #         try:
                        #             city_obj = city_to_save.first()  # Get the first city object
                        #             if city_obj is not None:
                        #                 resta_query = Restaurant(name=name, city=city_obj, details=restaurants_info)
                        #                 resta_query.save()
                        #             else:
                        #                 print(f"No city found for {city_name}")
                        #         except Exception as e:
                        #             print(f"Error occurred: {e}")
                        
                        # reslut1=foursquare_attraction(landmarks)
                        # attractions=[]
                        # if len(reslut1)==0:
                        #     attractions_info_trip=trip_advisor_attraction(city_name,country,landmarks)
                        #     attractions.append(attractions_info_trip)
                           
                        # else:
                        #     for i in reslut1:
                        #         name= (i['name'])
                        #         latitude = i['geocodes']['main']['latitude']
                        #         longitude = i['geocodes']['main']['longitude']
                        #         flickr_photos=flickr_api(name,latitude,longitude)
                        #         goog_result=google_search(f"{name},{city_name},{country}")
                        #         attractions_info={
                        #             'name':name,
                        #             'latitude':latitude,
                        #             'longitude':longitude,
                        #             'photos':flickr_photos,
                        #             'review_score': goog_result['review_score'],
                                    
                        #         }
                        #         attractions.append(attractions_info)
                        #         try:
                        #             city_obj = city_to_save.first()  # Get the first city object
                        #             if city_obj is not None:
                        #                 atrc_query = Attraction(name=name, city=city_obj, details=attractions_info)
                        #                 atrc_query.save()
                        #             else:
                        #                 print(f"No city found for {city_name}")
                        #         except Exception as e:
                        #             print(f"Error occurred: {e}")
                        
                        
                        # city_data['attractions'] = attractions
                        # city_data['restaurants'] = restaurants