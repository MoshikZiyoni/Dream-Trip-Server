    # api_key=os.environ.get('FOURSQUARE')
 
# def foursquare_restaurant(city_name, country,lat, lon):

    #     url = "https://api.foursquare.com/v3/places/search?"
    #     headers = {
    #         "accept": "application/json",
    #         "Authorization": api_key
    #     }
    #     query = {
    #         'query': f"attractions in {city_name} {country}",
    #          'categories':'10027,10025,10055,10068,16000',
    #         "ll": f"{lat},{lon}",
    #         'radius': 8000,
    #         'limit': 20,
    #         'fields': 'distance,geocodes,name,rating,distance,website,photos,menu,hours_popular,hours,location,tel,tips'
    #     }
    #     response = requests.get(url, params=query, headers=headers)
    #     response_text = response.text
    #     jsonto = json.loads(response_text)
    #     result = jsonto.get('results', [])
    #     return result

    # # Retrieve all Restaurant objects
    # # starting_id = 8600
    # # resta = Attraction.objects.filter(id__gte=starting_id)
    # cities = City.objects.all()
    # for cit in cities:
    #     city_name = cit.city
    #     lat = cit.latitude
    #     lon = cit.longitude
    #     country=cit.country.name
    #     id=cit.id
    #     print (id,'IDDDDDDDDDDDDDDDD')
    #     result=foursquare_restaurant(city_name=city_name,country=country,lat=lat,lon=lon)
    #     attractions = Attraction.objects.filter(city_id=id)
        
    #     for i in result:
    #         tips = []
    #         result_tips = i.get("tips", [])  # Get the list of tips from the current result
    #         for j, tip in enumerate(result_tips):
    #             if j >= 3:
    #                 break
    #             tip_text = tip.get("text", "")  # Get the text from the tip dictionary
    #             tips.append(tip_text)
    #         hours = i.get('hours', {}).get('display', "")
    #         name_res = i['name']
    #         address = i.get('location', {}).get('formatted_address', "")
    #         tel = i.get('tel', "")
    #         # print ("hours:",hours,"tel:",tel,"name_res:",name_res)
            
    #            # Check if an attraction with the name from Foursquare exists in the database
    #         existing_attraction = attractions.filter(name=name_res).first()

    #         if existing_attraction:
    #             # An attraction with the same name exists, update its fields
    #             try:
    #                 existing_attraction.tel = tel
    #                 existing_attraction.address = address
    #                 existing_attraction.hours = hours
    #                 existing_attraction.tips=tips
    #                 existing_attraction.save()  # Save the changes to the database
    #                 print(f"Updated details for attraction '{name_res}' (ID: {existing_attraction.id},successssssss)")
    #             except Exception as e:
    #                 print('Error while updating attraction details:', e)
    #         else:
    #             # The attraction doesn't exist, you may choose to create it or take other actions
    #             # print(f"Attraction '{name_res}' does not exist in the database. You can handle this case as needed.")
    #             hours = i.get('hours', {}).get('display', "")
    #             name_res = i['name']
    #             address = i.get('location', {}).get('formatted_address', "")
    #             tel = i.get('tel', "")
    #             name1 = i.get("name", "")
    #             distance1 = i.get("distance", "")
    #             latitude1 = (
    #                 i["geocodes"]["main"]["latitude"]
    #                 if "geocodes" in i
    #                 and "main" in i["geocodes"]
    #                 and "latitude" in i["geocodes"]["main"]
    #                 else ""
    #             )
    #             longitude1 = (
    #                 i["geocodes"]["main"]["longitude"]
    #                 if "geocodes" in i
    #                 and "main" in i["geocodes"]
    #                 and "longitude" in i["geocodes"]["main"]
    #                 else ""
    #             )
    #             rating1 = i.get("rating", "0")
    #             website1 = i.get("website", "")
    #             hours_popular1 = i.get("hours_popular", "")
    #             description = i.get("description", "")
    #             distance1=i.get("distance","")
    #             if len(description)==0:
    #                     try:
    #                         wiki=process_query(name1)
    #                         description=wiki[0]
    #                         print ('descrption from wiki')
    #                     except:
    #                         print ('descrption from wiki not gooodddddddddddddddd')
    #             photos1 = i.get("photos", "")
    #             if photos1:
    #                 first_photo = photos1[0]
    #                 prefix = first_photo.get("prefix", "")
    #                 suffix = first_photo.get("suffix", "")
    #                 url1 = f"{prefix}original{suffix}"
    #                 photos1=url1
                    
    #             else:
    #                 try:
    #                     photos1 = flickr_api(name=name1, latitude=latitude1, longitude=longitude1)
    #                 except:
    #                     print ("flickr api can't bring an image")

    #             atrc_query = Attraction(
    #             name=name_res,
    #             city=cit,
    #             latitude=latitude1,
    #             longitude=longitude1,
    #             photos=photos1,
    #             review_score=rating1,
    #             description=description,
    #             website=website1,
    #             hours_popular=hours_popular1,
    #             distance=distance1,
    #             tel = tel,
    #             address = address,
    #             hours = hours,
    #             tips=tips

    #         )
    #             atrc_query.save()
    #             print (f'NEWWWWW save success{id}')
            
                
    # return 'kk'
