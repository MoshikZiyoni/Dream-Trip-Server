# def extract_city_data(city_data):
#         for city_data in city_data:
#             country = city_data["country"]
#             city = city_data["city_name"]
#             description = city_data["description"]
#             latitude = city_data["latitude"]
#             longitude = city_data["longitude"]
#             print (city)
#             try:
#                 existing_country = Country.objects.filter(name=country).first()
#                 country_id = existing_country.id
#                 print ('there is the country')
#             except:
#                 print("Country does not exist")
#             if not existing_country:
#                 query_for_country = Country(name=country)
#                 query_for_country.save()
#                 print ('save country success')
#                 country_id = query_for_country.id
#             existing_city = City.objects.filter(city=city).first()
#             print ('there is already this city')
#             if not existing_city:
#                 city_query = City(
#                     country_id=country_id,
#                     city=city,
#                     latitude=latitude,
#                     longitude=longitude,
#                     description=description,
#                 )
#                 city_query.save()
#             city_objs = City.objects.filter(city=city).first()
#             if city_objs:
#                 attractions_exist = city_objs.attractions.exists()
#                 restaurants_exist = city_objs.restaurants.exists()

#                 if attractions_exist:
#                     # Attractions already exist for this city
#                     # Skip fetching attractions from Foursquare
#                     print("Attractions already exist for this city")
#                 else:
#                     # Fetch attractions from Foursquare
#                     landmarks = [city_objs.latitude, city_objs.longitude]
#                     result1 = foursquare_attraction(landmarks, city_name=city, country=city_objs.country)
#                     for attrac in result1:
#                         process_attraction(attrac=attrac, city_obj=city_objs)

#                 if restaurants_exist:
#                     # Restaurants already exist for this city
#                     # Skip fetching restaurants from Foursquare
#                     print("Restaurants already exist for this city")
#                 else:
#                     # Fetch restaurants from Foursquare
#                     landmarks = [city_objs.latitude, city_objs.longitude]
#                     result2 = foursquare_restaurant(landmarks)
#                     for restaur in result2:
#                         process_restaurant(restaur, city_obj=city_objs )

#                 print("Save success")
#             else:
#                 print("City not found")

#     extract_city_data(city_data = [
#    {"country": "Canada","city_name": "Toronto","latitude": 43.6532,"longitude": -79.3832, "description": "Toronto, the capital of Ontario, is Canada's largest city and a hub of trade and finance. It has a cosmopolitan atmosphere and a modern downtown with iconic skyscrapers."},
#     {"country": "Spain","city_name": "Madrid","latitude": 40.4168,"longitude": -3.7038, "description": "Madrid is the capital and most populous city of Spain. The city has almost 3.3 million inhabitants and a metropolitan area population of approximately 6.7 million."},
#     {"country": "Egypt","city_name": "Cairo","latitude": 30.0444,"longitude": 31.2357, "description": "Cairo is the capital of Egypt and one of the largest cities in Africa and the Middle East. Located near the Nile Delta, it is known as the \"city of a thousand minarets\"."},
#     {"country": "Turkey","city_name": "Istanbul","latitude": 41.0082,"longitude": 28.9784, "description": "Istanbul is a major city in Turkey that straddles Europe and Asia across the Bosphorus Strait. Its Old City reflects cultural influences of the many empires that once ruled here."},
#     {"country": "Brazil","city_name": "Rio de Janeiro","latitude": -22.9068,"longitude": -43.1729, "description": "Rio de Janeiro is a huge seaside city in Brazil, famed for its Copacabana and Ipanema beaches, 38m Christ the Redeemer statue atop Mount Corcovado and for Sugarloaf Mountain."},
#     {"country": "South Africa","city_name": "Cape Town","latitude": -33.9248,"longitude": 18.4241, "description": "Cape Town is a port city on South Africa’s southwest coast, on a peninsula beneath the imposing Table Mountain. Slowly rotating cable cars climb to the mountain’s flat top."},
#     {"country": "India","city_name": "Mumbai","latitude": 19.0760,"longitude": 72.8777, "description": "Mumbai, formerly Bombay, is a sprawling, densely populated city on India’s west coast. A financial center, it's India's largest city."},
#     {"country": "Argentina","city_name": "Buenos Aires","latitude": -34.6037,"longitude": -58.3816, "description": "Buenos Aires is Argentina's big, cosmopolitan capital city. Its center is the Plaza de Mayo, lined with stately 19th-century buildings including Casa Rosada, the iconic, balconied presidential palace."},
#     {"country": "United Arab Emirates","city_name": "Dubai","latitude": 25.2048,"longitude": 55.2708, "description": "Dubai is a city in the United Arab Emirates known for luxury shopping, modern architecture and a lively nightlife scene. Burj Khalifa, an 830m-tall tower, dominates the skyscraper-filled skyline."},
#     {"country": "South Korea","city_name": "Seoul","latitude": 37.5665,"longitude": 126.9780, "description": "Seoul is the capital and largest metropolis of South Korea. With a population of roughly 10 million people, Seoul is one of the world's largest cities."},
#     {"country": "Greece","city_name": "Athens","latitude": 37.9838,"longitude": 23.7275, "description": "Athens is the capital of Greece. It was also at the heart of Ancient Greece, a powerful civilization and empire. The city is still dominated by 5th-century BC landmarks, including the Acropolis."},
#     {"country": "Netherlands","city_name": "Amsterdam","latitude": 52.3702,"longitude": 4.8952, "description": "Amsterdam is the Netherlands’ capital, known for its artistic heritage, elaborate canal system and narrow houses with gabled facades, legacies of the city’s 17th-century Golden Age."},
#     {"country": "Czechia","city_name": "Prague","latitude": 50.0755,"longitude": 14.4378, "description": "Prague, capital city of the Czech Republic, is bisected by the Vltava River. Nicknamed \"the City of a Hundred Spires,\" it's known for its Old Town Square."},
#     {"country": "Austria","city_name": "Vienna","latitude": 48.2082,"longitude": 16.3738, "description": "Vienna, Austria’s capital, lies in the country's east on the Danube River. Its artistic and intellectual legacy was shaped by residents like Mozart, Beethoven and Sigmund Freud."},
#     {"country": "Finland","city_name": "Helsinki","latitude": 60.1699,"longitude": 24.9384, "description": "Helsinki, Finland's southern capital, sits on a peninsula in the Gulf of Finland. Its central avenue, Mannerheimintie, is flanked by institutions including the National Museum."},
#     {"country": "Thailand","city_name": "Bangkok","latitude": 13.7563,"longitude": 100.5018, "description": "Bangkok, Thailand's capital, is a large city known for ornate shrines and vibrant street life. The boat-filled Chao Phraya River feeds its network of canals, flowing past the Rattanakosin royal district."}, 
#     {"country": "Singapore","city_name": "Singapore","latitude": 1.3521,"longitude": 103.8198, "description": "Singapore, an island city-state off southern Malaysia, is a global financial center with a tropical climate and multicultural population."},
#     {"country": "Sweden","city_name": "Stockholm","latitude": 59.3294,"longitude": 18.0686, "description": "Built on 14 islands, Stockholm, the capital of Sweden, encompasses medieval lanes, modern architecture and green spaces."},
#     {"country": "Denmark","city_name": "Copenhagen","latitude": 55.6761,"longitude": 12.5683, "description": "Copenhagen, Denmark’s capital, sits on the coastal islands of Zealand and Amager. It's linked to Malmo in southern Sweden by the Öresund Bridge."},
#     {"country": "Hungary","city_name": "Budapest","latitude": 47.4979,"longitude": 19.0402, "description": "Budapest, Hungary’s capital, is bisected by the River Danube. Its 19th-century Chain Bridge connects the hilly Buda district with flat Pest."},
#     {"country": "Ireland","city_name": "Dublin","latitude": 53.3498,"longitude": -6.2603, "description": "Dublin, capital of the Republic of Ireland, is on Ireland's east coast at the mouth of the River Liffey. Its historic buildings include Dublin Castle and St Patrick's Cathedral."},  
#     {"country": "Poland","city_name": "Warsaw","latitude": 52.2297,"longitude": 21.0122, "description": "Warsaw is the sprawling capital of Poland. Its widely varied architecture reflects the city's long, turbulent history, from Gothic churches to Soviet-era blocks."},
#     {"country": "Portugal","city_name": "Lisbon","latitude": 38.7072,"longitude": -9.1355, "description": "Lisbon is Portugal's hilly, coastal capital city. The landmarks include Belem Tower, a 16th century fortress on the Tagus River, and the Jeronimos Monastery."},
#     {"country": "Norway","city_name": "Oslo","latitude": 59.9129,"longitude": 10.7461, "description": "Oslo, the capital of Norway, sits on the country’s southern coast at the head of the Oslofjord. It's known for its green spaces and museums."},
#     {"country": "Iceland","city_name": "Reykjavik","latitude": 64.1265,"longitude": -21.8174, "description": "Reykjavik is the capital and largest city of Iceland. It's home to the National and Saga museums, tracing Iceland's Viking history. The striking concrete Hallgrimskirkja church and rotating Perlan glass dome offer sweeping views of the sea and nearby farms."},
#     {"country": "Brazil","city_name": "Brasília","latitude": -15.7942,"longitude": -47.8825, "description": "Brasília is the federal capital of Brazil and seat of government of the Federal District. The city is located atop the Brazilian highlands and was founded in 1960."},
#     {"country": "Mexico","city_name": "Mexico City","latitude": 19.4326,"longitude": -99.1332, "description": "Mexico City is the densely populated, high-altitude capital of Mexico. It's known for its Templo Mayor (a 13th-century Aztec temple), the baroque Catedral Metropolitana de México of the Spanish conquistadors."},
#     {"country": "Chile","city_name": "Santiago","latitude": -33.4489,"longitude": -70.6693, "description": "Santiago, Chile's capital and largest city, lies in a valley surrounded by the snow-capped Andes and the Chilean Coast Range."},
#     {"country": "Colombia","city_name": "Bogota","latitude": 4.71099,"longitude": -74.0721, "description": "Bogotá is the capital and largest city of Colombia, located at an elevation of 2,640 meters in the Cordillera Oriental of the Andes."},
#     {"country": "Peru","city_name": "Lima","latitude": -12.0463,"longitude": -77.0428, "description": "Lima is the capital and largest city of Peru. It sits on the country's arid Pacific coast and has a historic center dating to the 16th century."},
#     {"country": "Venezuela","city_name": "Caracas","latitude": 10.4806,"longitude": -66.9036, "description": "Caracas, Venezuela's capital and largest city, sits on a high plateau in the northern part of the country. It has many cultural sites and several notable museums."},
#     {"country": "South Africa","city_name": "Johannesburg","latitude": -26.2041,"longitude": 28.0473, "description": "Johannesburg is South Africa's largest city, in the mineral-rich Witwatersrand range of hills. Its gold and diamond trades fueled growth in the 19th and early 20th centuries."},
#     {"country": "Kenya","city_name": "Nairobi","latitude": -1.2921,"longitude": 36.8219, "description": "Nairobi is the capital and largest city of Kenya. It's set on the Eastern edge of the Great Rift Valley and known as a commercial hub for East and Central Africa."},
#     {"country": "Morocco","city_name": "Casablanca","latitude": 33.5976,"longitude": -7.6189, "description": "Casablanca is a port city and commercial hub in western Morocco. The city's French colonial legacy is seen in its downtown Mauresque architecture."},
#     {"country": "Lebanon","city_name": "Beirut","latitude": 33.8938,"longitude": 35.5018, "description": "Beirut is the capital and largest city of Lebanon. As there is no official census data, the source of population data is the United Nations."},
#     {"country": "India","city_name": "New Delhi","latitude": 28.6139,"longitude": 77.2090, "description": "New Delhi is the capital city of India. It is home to important government buildings including Rashtrapati Bhavan, the parliament house, and India Gate."},
#     {"country": "Vietnam","city_name": "Hanoi","latitude": 21.0245,"longitude": 105.8412, "description": "Hanoi, Vietnam's capital, is known for its centuries-old architecture and a rich culture with Southeast Asian, Chinese and French influences."},
#     {"country": "Philippines","city_name": "Manila","latitude": 14.5995,"longitude": 120.9842, "description": "Manila is the densely populated capital of the Philippines, known for its bustling metropolitan atmosphere and mix of colonial, modern and indigenous architecture."},
#     {"country": "Indonesia","city_name": "Jakarta","latitude": -6.2088,"longitude": 106.8456, "description": "Jakarta is Indonesia's massive, sprawling capital city, and also happens to be the largest city proper in the world by population."},
#     {"country": "Malaysia","city_name": "Kuala Lumpur","latitude": 3.1502,"longitude": 101.6954, "description": "Kuala Lumpur is the capital city of Malaysia, boasting gleaming skyscrapers, colonial architecture, charming locals, and a myriad of natural attractions."},  
#     {"country": "New Zealand","city_name": "Wellington","latitude": -41.2865,"longitude": 174.7762, "description": "Wellington is the capital city and second most populous urban area of New Zealand. It is located at the southwestern tip of the North Island."},
#     {"country": "United States","city_name": "San Francisco","latitude": 37.7749,"longitude": -122.4194, "description": "San Francisco, in northern California, is a hilly city on the tip of a peninsula surrounded by the Pacific Ocean and San Francisco Bay."},
#     {"country": "United States","city_name": "Los Angeles","latitude": 34.0522,"longitude": -118.2437, "description": "Los Angeles is a sprawling Southern California city famed as the center of the nation’s film and television industry. Near its iconic Hollywood sign, studios such as Paramount Pictures, Universal and Warner Brothers offer behind-the-scenes tours."},
#     {"country": "United States","city_name": "Chicago","latitude": 41.8781,"longitude": -87.6298, "description": "Chicago, on Lake Michigan in Illinois, is among the largest cities in the U.S. Famed for its bold architecture, it has a skyline punctuated by skyscrapers such as the iconic John Hancock Center, 1,451-ft."},
#     {"country": "United States","city_name": "Miami","latitude": 25.7617,"longitude": -80.1918, "description": "Miami, Florida's southernmost city, sits on the shores of Biscayne Bay. It's home to South Beach, known for its dining, nightlife and art deco architecture."},
#     {"country": "United States","city_name": "Boston","latitude": 42.3601,"longitude": -71.0589, "description": "Boston, the capital of Massachusetts, is one of the oldest cities in the United States. It's home to prestigious colleges and historic sites."},
#     {"country": "United States","city_name": "Seattle","latitude": 47.6062,"longitude": -122.3321,"description": "Seattle, a city on Puget Sound in the Pacific Northwest, is surrounded by water, mountains and evergreen forests, and contains thousands of acres of parkland."},
# {"country": "United States","city_name":"Las Vegas","latitude":36.1699,"longitude":-115.1398,"description":"Las Vegas, in Nevada's Mojave Desert, is a resort city famed for its vibrant nightlife, centered around 24-hour casinos and other entertainment options."},
# {"country": "United States","city_name":"San Diego","latitude":32.7157,"longitude":-117.1611,"description":"San Diego is a city on the Pacific coast of California known for its beaches, parks and warm climate."},
# {"country": "United States","city_name":"Houston","latitude":29.7604,"longitude":-95.3698,"description":"Houston is a large metropolis in Texas, extending to Galveston Bay. It's closely linked with the Space Center Houston, the coastal visitor center at NASA's astronaut training and flight control complex."},
# {"country": "United States","city_name":"Dallas","latitude":32.7767,"longitude":-96.7970,"description":"Dallas, a modern metropolis in north Texas, is a commercial and cultural hub of the region. Downtown's Sixth Floor Museum at Dealey Plaza commemorates John F. Kennedy's assassination in 1963."},
# {"country": "United States","city_name":"Atlanta","latitude":33.7490,"longitude":-84.3880,"description":"Atlanta, the capital of Georgia, is a sprawling city with three urban skylines rising in different directions from the downtown area."},
# {"country": "United States","city_name":"Denver","latitude":39.7392,"longitude":-104.9903,"description":"Denver, the capital of Colorado, is an American metropolis dating to the Old West era. Larimer Square, the city’s oldest block, still features landmark 19th-century buildings that house restaurants and galleries."},
# {"country": "United States","city_name":"Phoenix","latitude":33.4484,"longitude":-112.0740,"description":"Phoenix, the capital of Arizona, is a sprawling Southwestern metropolis known for its year-round sun and warm temperatures."},
# {"country": "United States","city_name":"Portland","latitude":45.5122,"longitude":-122.6587,"description":"Portland, Oregon's largest city, sits on the Columbia and Willamette rivers, in the shadow of snow-capped Mount Hood."},
# {"country": "United States","city_name":"Philadelphia","latitude":39.9526,"longitude":-75.1652,"description":"Philadelphia, Pennsylvania's largest city, is notable for its rich history, on display at the Liberty Bell, Independence Hall and other American Revolutionary sites."},
# {"country": "Canada","city_name":"Vancouver","latitude":49.2827,"longitude":-123.1207,"description":"Vancouver, a bustling west coast seaport in British Columbia, is among Canada's densest, most ethnically diverse cities."},
# {"country": "Canada","city_name":"Montreal","latitude":45.5017,"longitude":-73.5673,"description":"Montreal is the largest city in Canada's Québec province. It’s set on an island in the Saint Lawrence River and named after Mt. Royal, the triple-peaked hill at its heart."},
# {"country": "Canada","city_name":"Calgary","latitude":51.0486,"longitude":-114.0708,"description":"Calgary, an Albertan city with frontier-era architecture, sits where the Canadian Prairies meet the Rocky Mountains."},
# {"country": "Canada","city_name":"Ottawa","latitude":45.4215,"longitude":-75.6972,"description":"Ottawa, Canada's capital, sits on the border between the provinces of Ontario and Quebec, on the Ottawa River."},
# {"country": "Canada","city_name":"Edmonton","latitude":53.5461,"longitude":-113.4938,"description":"Edmonton is the capital of the Canadian province of Alberta. Edmonton is located on the North Saskatchewan River and is the center of the Edmonton Metropolitan Region."},
# {"country": "Canada","city_name":"Quebec City","latitude":46.8139,"longitude":-71.2081,"description":"Québec City, capital of Canada's Québec province, sits on the Saint Lawrence River. Dating to 1608, it has a preserved Old Town, Place Royale, with stone buildings and narrow streets."},
# {"country": "Canada","city_name":"Sydney","latitude":46.1351,"longitude":-60.1849,"description":"Sydney is a historic city and the largest urban centre on Cape Breton Island in Nova Scotia, Canada."},
# {"country": "Australia","city_name":"Melbourne","latitude":-37.8136,"longitude":144.9631,"description":"Melbourne is the coastal capital of the southeastern Australian state of Victoria. At the city's centre is the modern Federation Square development."},
# {"country": "Australia","city_name":"Brisbane","latitude":-27.4698,"longitude":153.0251,"description":"Brisbane, capital of Queensland, is a large city on the Brisbane River. Clustered in its South Bank cultural precinct are the Queensland Museum and Sciencentre, with noted interactive exhibitions."},
# {"country": "Australia","city_name":"Perth","latitude":-31.9505,"longitude":115.8605,"description":"Perth, capital of Western Australia, sits where the Swan River meets the southwest coast. Sandy beaches line its suburbs, and the huge, riverside Kings Park and Botanic Garden on Mount Eliza offer sweeping views."},
# {"country": "Australia","city_name":"Adelaide","latitude":-34.9284,"longitude":138.6007,"description":"Adelaide is the capital city of the state of South Australia, and the fifth-most populous city of Australia."},
# {"country": "New Zealand","city_name":"Auckland","latitude":-36.8485,"longitude":174.7633,"description":"Auckland, based around 2 large harbors, is a major city in the north of New Zealand's North Island. In the center is the iconic Sky Tower, an observation and telecommunications tower."},
# {"country": "New Zealand","city_name":"Christchurch","latitude":-43.5256,"longitude":172.6362,"description":"Christchurch is the largest city in the South Island of New Zealand, and the country's third-most populous urban area."},
# {"country": "New Zealand","city_name":"Wellington","latitude":-41.2865,"longitude":174.7762,"description":"Wellington is the capital city and second most populous urban area of New Zealand. It is located at the southwestern tip of the North Island."}])
#     return 'ok'