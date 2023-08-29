
# import json
# import requests
# from urllib.parse import quote
# from geopy.geocoders import Nominatim
# from dotenv import load_dotenv
# import os
# import time
# import flickrapi

# from models import Restaurant
# load_dotenv()


attractions_list1 = [  'Murchison Falls National Park', 'Ankara', 'Drammen', 'Oruro', 'Belo Horizonte', 'Eindhoven', 'Oulu', 'Daegu', 'Potosi', 'Gaziantep', 'Santo Domingo', 'Tampere', 'Mombasa', 'Gran Canaria', 'Adana', 'Antalya', 'Budva', 'Nizhny Novgorod', 'Gdansk', 'Ushuaia', 'Saint Petersburg', 'Patras', 'Fortaleza', 'Tilburg', 'Poznan', 'Shenzhen', 'Samara', 'Cali', 'Encarnacion', 'Heraklion', 'Ostrava', 'Escaldes-Engordany', 'Glasgow', 'Medellin', 'Kazan', 'Buzios', 'Waterford', 'El Calafate', 'Szczecin', 'Montevideo', 'Corfu', 'Tlemcen', 'Larissa', 'Funchal', 'Liverpool', 'Vantaa', 'Frankfurt', 'Ioannina', 'Boa Vista', 'Kampala', 'Stuttgart', 'Lausanne', 'Crete', 'Incheon', 'Konya', 'Punta del Este', 'Gwangju', 'Shanghai', 'Bergen', 'Santa Marta', 'Florianopolis', 'Punta Cana', 'Maasai Mara', 'Daejeon', 'Geneva', 'Ciudad del Este', 'Sao Luis', 'Tianjin', 'Wroclaw', 'Belem', 'Bursa', 'Tenerife', 'Oran', 'Ulsan', 'Mexico city', 'Novosibirsk', 'Porto Seguro', 'Krakow', 'Ayers Rock (Uluru)', 'Montego Bay', 'Basel', 'Birmingham', 'Izmir', 'Palma de Mallorca', 'Natal', 'Braga', 'Entebbe', 'Lodz', 'Espoo', 'Lucerne', 'Brasilia', 'Puerto Natales', 'Volos', 'Joao Pessoa', 'San Juan', 'Dubrovnik', 'Puebla City', 'Vlore', 'Foz do Iguacu', 'Lake Titicaca', 'St. Gallen', 'Salta', 'Khuvsgul Lake', 'Busan', 'Kotor', 'Stavanger', 'Fredrikstad', 'Curitiba', 'Leeds', 'Thessaloniki', 'Monterrey', 'Colonia', 'Coimbra', 'Liberec', 'Amadora', 'Trondheim', 'Hangzhou', 'Cayo Coco', 'Chengdu', 'Chelyabinsk', 'Maceio', 'Asuncion', 'Bern', 'Guangzhou', 'Valparaiso', 'Porto Alegre', 'Tijuana', 'Rhodes', 'Wuhan', 'Leipzig', 'Düsseldorf', 'Hradec Kralove', 'Plzen', 'Zurich', 'Yekaterinburg', 'Sandnes', 'Leticia', 'Amalfi Coast', 'La Massana', 'Samui', 'Mykonos', 'Turku', 'Vila Nova de Gaia']

attractions_list2 = [          'Kutna Hora','Malmo','Munich', 'Istanbul', 'Pacific Harbour', 'New Delhi', 'Kandy', 'Boquete', 'Sofia', 'Puerto Vallarta', 'Ulaanbaatar', 'Cologne',  'Manaus', 'Porto', 'Hanoi', 'Nagoya',  'Lyon', 'Koh Samui', 'Barcelona', 'Beirut', 'Fukuoka', 'Cluj-Napoca',  ]
attractions_list3 = [   'Fukuoka', 'Ayutthaya','Belfast', 'Wellington', 'Granada', 'Valencia', 'Brussels', 'The Hague',  'La Paz', 'Bruges', 'Jerusalem', 'Hamburg', 'Vienna',   'Iquitos',    'Dallas',  'Kharkhorin', 'Paris', 'Cusco',   'Auckland', 'Nairobi', 'Puerto Vallarta', 'La Fortuna']
attractions_list4=[     'Tlemcen','Warsaw','Pucon', 'Algiers','Nazareth','Singapore',  'Nice', 'Pilsen',     'Colombo',  'Mont Saint-Michel', 'Gothenburg',  'Krabi', 'Cologne', 'Siem Reap', 'Santiago', 'Houston', 'Merida', 'Sydney', 'Seoul',  'Kandy', 'Budapest',  'Istanbul']
attractions_list5=[  'Bordeaux','Reykjavik', 'Perth',     'Mexico City',  'Denver', 'Sintra', 'Linkoping', 'Pucon', 'Phoenix', 'Kolding', 'Nassau', 'Dead Sea', 'Strasbourg', 'Cork', 'Playa del Carmen', 'Buenos Aires', 'Arusha', 'Vancouver',  'Guadalajara',  'Athens', 'Toronto', 'Havana']
# new=['', ', 'Fukuoka',  '', 'Tlemcen', 'Bordeaux', '',, '', 'Olomouc',   '',   '',]
print (len(attractions_list1))
print (len(attractions_list2))
print (len(attractions_list3))
print (len(attractions_list4))
print (len(attractions_list5))
print()

list_for_poe=[ 'Seattle', 'Kutna Hora', 'Naples', 'Nantes', 'Fukuoka', 'Delhi', 'Gyor', 'Yokohama', 'San Pedro de Atacama', 'Helsinki','Valencia', 'Tlemcen', 'Klagenfurt', 'Bordeaux', 'Hamburg', 'Lyon', 'Maasai Mara', 'Cluj-Napoca', 'Olomouc', 'Guadalajara', 'Vik', 'Houston', 'Hanoi', 'Porto', 'Dead Sea', 'Ayutthaya', 'Belfast', 'Linkoping', 'Edinburgh', 'Gothenburg',]
list_for_poe1=[ 'Plovdiv', 'Antwerp', 'Kuala Lumpur', 'Mérida', 'Bath', 'Moscow', 'Randers', 'Rome', 'Linz','Berlin', 'Malmo', 'Gyor', 'Faro', 'Cinque Terre', 'Aalborg', 'Gjirokaster', 'Eilat', 'Sydney', 'Český Krumlov', 'Nagoya','Manaus', 'Savusavu',  'Athens', 'San Sebastian', 'Mumbai', 'Edmonton', 'Trinidad', 'Seville', 'Salvador', 'Szeged',]
list_for_poe2=[   'Strasbourg', 'Bocas del Toro', 'Ibiza', 'Cannes', 'Helsinki', 'Bucharest', 'Cesky Krumlov', 'Galway', 'Agra', 'Bath','Jaipur', 'Agra', 'Delhi', 'Kharkhorin', 'Cancun', 'Kutná Hora', 'Haifa', 'Beijing', 'Uyuni', 'Oaxaca','Ulaanbaatar', 'Sucre', 'Jerusalem', 'Maastricht', 'Venice', 'Aarhus', 'Puerto Varas', 'La Paz', 'San Diego', 'Nassau',]
list_for_poe3=[  'Yokohama', 'Kyoto', 'Oran', 'Bogota','Canillo', 'Madrid', 'Oran', 'Berlin', 'Cairo', 'Venice', 'Torres del Paine', 'Cancún', 'Siem Reap', 'Luanda', 'Seoul', 'Cork', 'Kampot', 'Odense', 'Buenos Aires', 'Vienna','Bangkok',  'Nyiregyhaza', 'Granada', 'Barcelona', 'Limerick', 'Savusavu', 'Jakarta', 'Banff', 'Hiroshima', 'Pecs',]
list_for_poe4=[  ]
print (len(list_for_poe))
print (len(list_for_poe1))
print (len(list_for_poe2))
print (len(list_for_poe3))
print (len(list_for_poe4))
attraction_listttttttttttttttt_new=["Funchal","Eilat","Lake Titicaca","Miami","Houston","Porto Alegre","Belo Horizonte","Buenos Aires","Toronto","Varna","Coimbra","Adana","Sao Paulo","Auckland","Stuttgart","San Diego","Samui"]
# number_3={'Prague', 'Boquete', 'San Francisco', 'Fukuoka', 'Denver', 'Innsbruck', 'Kabul', 'Ouro Preto', 'Andorra la Vella', 'Mendoza', 'Cairo', 'Kandy', 'Marseille', 'Johannesburg', 'Malaga', 'Pilsen', 'Recife', 'Puerto Vallarta', 'Cork', 'La Fortuna', 'San Diego', 'Oslo', 'Osaka', 'Strasbourg', 'Salzburg', 'Koh Phangan', 'Uyuni', 'Edmonton', 'Limerick', 'Rio de Janeiro', 'Ella', 'Seville', 'Lyon', 'Milan', 'Seattle', 'Athens', 'Nuwara Eliya', 'Colombo', 'Sintra', 'Debrecen', 'Avignon', 'Manaus', 'Cannes', 'Vik', 'Bangkok', 'Dead Sea', 'Oran', 'Gyor', 'Bogota', 'Berlin', 'Jerusalem', 'Pecs', 'Aswan', 'Munich', 'Porto', 'Varadero', 'Pacific Harbour', 'Maasai Mara', 'Koh Samui', 'Tokyo', 'Malmo', 'Monteverde', 'Utrecht', 'Portland', 'Amsterdam', 'Quebec City', 'Caracas', 'Havana', 'Belfast', 'Český Krumlov', 'Gothenburg', 'Kolding', 'Randers', 'Eilat', 'Phuket', 'Chiang Mai', 'Ottawa', 'Groningen', 'Mumbai', 'Pucon', 'Esbjerg', 'Graz', 'Kampala', 'Lima', 'Antwerp', 'Iquitos', 'Manila', 'Delhi', 'Paris', 'Atlanta', 'Beijing', 'Madrid', 'Encamp', 'Oxford', 'Cusco', 'Florence', 'Heidelberg', 'Bucharest', 'Brașov', 'Cinque Terre', 'Galle', 'Rotterdam', 'Miami', 'Pune', 'Serengeti National Park', 'Florianópolis', 'Granada', 'Linkoping', 'Seoul', 'Amalfi', 'Cape Town', 'Kuala Lumpur', 'Christchurch', 'Brasília', 'Calgary', 'Nazareth', 'Nantes', 'Szeged', 'Berat', 'Santorini', 'The Hague', 'Tlemcen', 'Odense', 'Salvador', 'Torres del Paine', 'Venice', 'Sucre', 'Mont Saint-Michel', 'Melbourne', 'Merida', 'Alicante', 'Saranda', 'Hanoi', 'Bruges', 'Kampot', 'Manchester', 'Soldeu', 'Manuel Antonio', 'Ibiza', 'Boston', 'Banff', 'Cancun', 'Galway', 'Wellington', 'Philadelphia', 'Kutná Hora', 'Klagenfurt', 'Perth', 'Bilbao', 'Varna', 'Cluj-Napoca', 'Aalborg', 'Gjirokaster', 'Kharkhorin', 'Nyiregyhaza', 'Edinburgh', 'Kyoto', 'Montreal', 'Algiers', 'Brisbane', 'Siem Reap', 'Brussels', 'Playa del Carmen', 'Nagoya', 'São Paulo', 'Haifa', 'Dallas', 'Ghent', 'Guadalajara', 'Sydney', 'Mexico City', 'Vancouver', 'Belize City', 'Rothenburg ob der Tauber', 'Naples', 'Haarlem', 'Aarhus', 'La Paz', 'Houston', 'Miskolc', 'San Sebastian', 'Bariloche', 'Antigua', 'Bordeaux', 'Suva', 'Terelj National Park', 'Jakarta', 'Valparaíso', 'Auckland', 'Hiroshima', 'Toulouse', 'Mombasa', 'Puerto Varas', 'Linz', 'Brasov', 'Uppsala', 'Sapporo', 'Kutna Hora', 'Warsaw', 'Maastricht', 'Tirana', 'Cologne', 'Oaxaca', 'Dublin', 'Las Vegas', 'Los Angeles', 'Arusha', 'Akureyri', 'Yokohama', 'Helsinki', 'Plovdiv', 'Chicago', 'Mérida', 'Hamburg', 'Buenos Aires', 'Nairobi', 'Panama City', 'Canillo', 'Sofia', 'Ordino', 'Pattaya', 'Paraty', 'Moscow', 'Barcelona', 'Krabi', 'Bath', 'Adelaide', 'Cairns', 'Orebro', 'Entebbe', 'Lisbon', 'Bocas del Toro', 'Cancún', 'Agra', 'Vasteras', 'Tel Aviv', 'San Jose', 'Faro', 'Iguazu Falls', 'Cesky Krumlov', 'Denarau', 'Toronto', 'Istanbul', 'Casablanca', 'Santiago', 'Trinidad', 'Jaipur', 'Reykjavik', 'Luanda', 'Dubai', 'Vienna', 'Brno', 'Ayutthaya', 'Valencia', 'Zaragoza', 'Nassau', 'Phnom Penh', 'Copenhagen', 'Ulaanbaatar', 'Lahti', 'Karlovy Vary', 'Singapore', 'Savusavu', 'Beirut', 'New Delhi', 'Olomouc', 'San Pedro de Atacama', 'Varanasi', 'Phoenix', 'Stockholm', 'London', 'Budapest', 'Nice', 'Rome'}
# # Iterate through the attractions and distribute them among the three lists
# current_list = 1  # Initialize with the first list
# for attraction in number_3:
#     if current_list == 1:
#         attractions_list1.append(attraction)
#         current_list = 2
#     elif current_list == 2:
#         attractions_list2.append(attraction)
#         current_list = 3
#     elif current_list==3:
#         attractions_list3.append(attraction)
#         current_list = 4
#     elif current_list==4:
#         attractions_list4.append(attraction)
#         current_list = 5
#     else:
#         attractions_list5.append(attraction)
#         current_list = 1

# print ('@@@@@@@@@@@@@@@@@@@@',attractions_list1)
# print ('@@@@@@@@@@@@@@@@@@@@',attractions_list2)
# print ('@@@@@@@@@@@@@@@@@@@@',attractions_list3)
# print ('@@@@@@@@@@@@@@@@@@@@',attractions_list4)
# print ('@@@@@@@@@@@@@@@@@@@@',attractions_list5)
# print(len(attractions_list1))
# print(len(attractions_list2))
# print(len(attractions_list3))
# print(len(attractions_list4))
# print(len(attractions_list5))


# number_11=['Cancun', 'Groningen', 'Adana', 'Debrecen', 'Varna', 'Brasilia', 'Luanda', 'Beirut', 'Nice', 'Koh Samui', 'Randers', 'Brisbane', 'Bern', 'Luxor', 'Patras', 'Sydney', 'Budva', 'New Delhi', 'Encarnacion', 'Brno', 'Mexico City', 'Asuncion', 'Pune', 'Marrakesh', 'Corfu', 'Tianjin', 'Punta del Este', 'Zaragoza', 'Wellington', 'Wroclaw', 'St. Gallen', 'Grand Canyon', 'Los Angeles', 'Zanzibar', 'Tijuana', 'Edinburgh', 'Saint Petersburg', 'Buenos Aires', 'Coimbra', 'Houston', 'Drammen', 'Valle de los Caídos', 'Düsseldorf', 'Kathmandu']
# number_22=['Birmingham', 'Lahti',  'Odense', 'Osaka', 'Kabul', 'Puebla City', 'Buzios', 'Oran',  'Utrecht', 'Florianopolis', 'Seville', 'San Pedro de Atacama', 'Salta', 'Varanasi', 'Nassau', 'Rome', 'Ottawa', 'La Fortuna', 'Basel', 'Montevideo', 'Delhi', 'Graz', 'Puerto Vallarta', 'San Francisco', 'Santo Domingo', 'Palma de Mallorca', 'Foz do Iguacu',  'Fortaleza', 'Hiroshima', 'Oxford', 'Kazan', 'Johannesburg', 'Uppsala', 'Montreal', 'Hangzhou', 'Cluj-Napoca', 'Volos', 'Ioannina', 'Warsaw', 'Potosi', 'Pecs']
# number_33=['Granada', 'Belo Horizonte', 'Geneva', 'Vantaa', 'Torres del Paine', 'Oulu', 'Cairo', 'Nizhny Novgorod', 'Trondheim', 'Braga', 'Gran Canaria',  'Algiers', 'Yokohama', 'Punta Cana', 'Santa Marta', 'Szeged', 'Bilbao', 'Wuhan', 'Hradec Kralove', 'Adelaide', 'Bangkok', 'Chiang Mai',  'Chelyabinsk', 'Antalya', 'Bali', 'Linz', 'Soldeu', 'Boa Vista', 'Bucharest', 'The Hague', 'Tenerife', 'Antwerp', 'Gwangju', 'Guadalajara', 'Lima', 'Denver', 'Daegu', 'Guangzhou', 'Trinidad', 'Monterrey', 'Ostrava']
# number_44=['Sapporo', 'Lodz', 'Kandy', 'Maastricht', 'Machu Picchu', 'Puerto Natales', 'Ghent', 'Kotor', 'Haifa', 'Fukuoka', 'Andorra la Vella',  'Daejeon', 'Savusavu', 'Gjirokaster', 'Ushuaia', 'Rhodes', 'Phoenix', 'Leticia', 'Aswan', 'Vancouver', 'Samara', 'Kutná Hora', 'Siem Reap', 'Taveuni', 'Incheon', 'Heidelberg', 'Turku', 'Jaipur', 'Nyiregyhaza', 'Perth', 'Killarney', 'Alicante', 'El Calafate', 'Orebro', 'Salzburg', 'Boquete', 'Ankara', 'Cesky Krumlov', 'Varadero', 'Atlanta', 'Khorgo', 'Leipzig', 'Agra', 'Shenzhen', 'Ordino', 'Ciudad del Este']
# number_55=[ 'Tirana', 'Melbourne', 'Venice', 'Lausanne', 'Cairns', 'Ibiza', 'Ayers Rock (Uluru)', 'Nuwara Eliya', 'Portland', 'Gdansk', 'Dallas', 'Vienna', 'Vila Nova de Gaia', 'Arusha', 'Ella', 'Waterford', 'Novosibirsk', 'Crete', 'Pattaya', 'Valparaiso', 'Jerusalem', 'Naples', 'Colonia', 'Český Krumlov', 'Sihanoukville', 'Busan', 'Edmonton', 'London', 'Manuel Antonio', 'Stuttgart', 'Eilat', 'Miami', 'Quebec City', 'San Diego',  'Porto Alegre', 'Cinque Terre', 'Plzen', 'Olomouc', 'Shanghai',  'Lucerne', 'Easter Island', 'Auckland', 'Oslo']
# number_66=['Nazareth', 'Mombasa', 'Entebbe', 'Seoul', 'Casablanca', 'Iquitos', 'Eindhoven', 'Maasai Mara', 'Kolding', 'Bocas del Toro', 'Petra',  'Hanoi', 'Florence', 'Liberec', 'Bergen', 'La Paz', 'Bogota', 'Natal', 'Jakarta', 'Oaxaca', 'Tikal', 'Bariloche', 'Izmir', 'Koh Phangan', 'Medellin', 'Oruro', 'San Jose', 'Budapest', 'Belem', 'Istanbul', 'Malaga', 'Banff', 'Haarlem', 'Sao Luis', 'Krakow', 'Brașov', 'Saranda', 'Madrid', 'Stavanger', 'Gyor', 'Kuala Lumpur', 'Vasteras']
# number_77=['Brussels', 'Sandnes', 'Linkoping', 'Calgary',  'Denarau', 'Innsbruck', 'Larissa', 'Valencia', 'Thessaloniki', 'Dubai', 'Gaziantep', 'Suva', 'Ayutthaya', 'Mendoza', 'Lake Atitlán',   'Las Vegas', 'New York city', 'Malmo', 'Beijing', 'Zurich', 'Milan',  'Krabi', 'Antigua', 'Frankfurt', 'Encamp', 'Yekaterinburg', 'Kampot', 'Merida', 'Terelj National Park', 'Galle', 'Caracas', 'Moscow', 'San Juan', 'Tlemcen', 'Tampere', 'Bursa', 'Ulaanbaatar']
# number_88=['Helsinki', 'Havana', 'Sucre', 'Boston', 'Tilburg', 'Amadora', 'Stockholm', 'Pucon', 'Angkor Wat', 'Pacific Harbour', 'Konya', 'Queenstown', 'Espoo', 'Vlore', 'Amalfi', 'Uyuni', 'Hamburg',  'Montego Bay', 'Cape Town', 'Miskolc', 'Cusco', 'Bath', 'Chicago', 'Colombo', 'Valparaíso', 'Philadelphia', 'Fredrikstad',  'Singapore', 'Esbjerg', 'Leeds', 'Amsterdam', 'Cartagena', 'Glasgow', 'Pilsen',  'Karlovy Vary', 'Toronto',  'Phuket', 'Ulsan', 'Puerto Varas', 'Funchal']
# number_99=['Kyoto', 'Santiago', 'Porto Seguro', 'Vik', 'Playa del Carmen', 'Chengdu', 'Panama City', 'Rothenburg ob der Tauber', 'Mumbai', 'Tokyo', 'York', 'Joao Pessoa', 'Liverpool', 'Bruges', 'San Sebastian', 'Nantes', 'Klagenfurt', 'Rotterdam', 'Szczecin', 'Nagoya', 'Belize City', 'Monteverde', 'Poznan', 'Christchurch', 'Gothenburg', 'Nairobi', 'Cali', 'Dubrovnik', 'Kampala', 'Barcelona', 'Prague', 'Mykonos', 'Heraklion', 'Manila', 'Seattle', 'Maceio', 'Paris', 'Curitiba', 'Phnom Penh', 'Manchester', 'Canillo', 'Kharkhorin']
# print (len(number_11))
# print (len(number_22))
# print (len(number_33))
# print (len(number_44))
# print (len(number_55))
# print (len(number_66))
# print (len(number_77))
# print (len(number_88))
import re
def split_tips(tips_str):
    # Split the tips string based on the newline character and numbers with periods
    tips_list = [tip.strip() for tip in re.split(r'\d+\.', tips_str) if tip.strip()]
    return tips_list

# Example usage:
tips_str = "1. Check out the rotating exhibitions in the main building. 2. Don't miss the Ploeg collection featuring 20th-century Groningen artists. 3. Stop for a drink or meal at the Grand Cafe."
tips_list = split_tips(tips_str)
print(tips_list)