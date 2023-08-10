import requests

def get_cities_by_country(country, limit):
    url = f"https://api.teleport.org/api/cities/?search={country}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    # print (data)
    cities = []
    for item in data['_embedded']['city:search-results']:
        city = {}
        city['name'] = item['matching_full_name']
        city_url = item['_links']['city:item']['href']
        city_response = requests.get(city_url)
        city_data = city_response.json()
        # print(city_data)
        if 'city:urban_area' in city_data['_links']:
            urban_area_url = city_data['_links']['city:urban_area']['href']
            urban_area_response = requests.get(urban_area_url)
            urban_area_data = urban_area_response.json()
            if 'ua:details' in urban_area_data['_links']:
                details_url = urban_area_data['_links']['ua:details']['href']
                details_response = requests.get(details_url)
                details_data = details_response.json()
                cost_of_living_data = {}
                climate_first_value = None
                for category in details_data['categories']:
                    if category['label'] == 'Cost of Living':
                        # for item in category['data']:
                        #     print(item)
                        cost_of_living_data = {}
                        for item in category['data']:
                            if 'currency_dollar_value' in item:
                                cost_of_living_data[item['label']] = item['currency_dollar_value']
                    elif category['label'] == 'Climate':
                        climate_first_value = category['data'][0].get('float_value')
                  
                if cost_of_living_data:
                    return cost_of_living_data
                else:
                    continue
                print('average daily',climate_first_value)             
                # city['description'] = details_data['sections'][0]['body']
    #     cities.append(city)
    # return cities
# cities = get_cities_by_country('italy', limit=2)

# if cities:
#     transport_cost=(cities['Monthly public transport'])
#     Lunch=cities['Lunch']
#     print(Lunch)
# else:
#     print('No cities found.')

