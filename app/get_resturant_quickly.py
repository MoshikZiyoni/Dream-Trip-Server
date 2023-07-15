# def foursquare_restaurant(city,landmark):
#         api_key=os.environ.get('FOURSQUARE')
#         url = "https://api.foursquare.com/v3/places/search?"
#         print(landmark[0])
#         headers = {
#             "accept": "application/json",
#             "Authorization": api_key
#         }

#         query = {
#             'categories': '13000',
#             "ll" :  f"{landmark[0]},{landmark[1]}",
#             'radius': 5000,
#             'limit': 10,
#             'fields':'distance,geocodes,name,rating,price,distance,website,photos,social_media,menu'
#         }

#         response = requests.get(url, params=query, headers=headers)
#         response_text = response.text
#         jsonto = json.loads(response_text)
#         results = jsonto['results']
#         city_obj = City.objects.filter(city=city).first()
#         if not city_obj:
#             pass
#         for i in results:
#             process_restaurant(city_obj=city_obj,restaur=i,restaurants=[])

#     def get_landmarks(city):
#         landmarks = {  # Example landmarks for Nantes, France
#         "Strasbourg": [48.5839, 7.7455],  # Example landmarks for Strasbourg, France
#         "Bordeaux": [44.8378, -0.5792],  # Example landmarks for Bordeaux, France
#         "Berlin": [52.5200, 13.4050],  # Example landmarks for Berlin, Germany
#         "Hamburg": [53.5511, 9.9937],  # Example landmarks for Hamburg, Germany
#         "Munich": [48.1351, 11.5820],  # Example landmarks for Munich, Germany
#     }
#         return landmarks.get(city, [])

#     # Example usage
#     cities = [
#         "Strasbourg",
#         "Bordeaux",
#         "Berlin",
#         "Hamburg",
#         "Munich"
#     ]

#     for city in cities:
#         landmark = get_landmarks(city)
#         print(landmark,'first')
#         foursquare_restaurant(city,landmark)

#     return 'ok'







[
    {
        "combined_data": {
            "city": "",
            "description": "",
            "schedules": [
                {
                    "city": "Prague",
                    "description": "The historic capital of Czech Republic known for its stunning architecture and vibrant nightlife.",
                    "restaurants": [
                        {
                            "id": 4822,
                            "city_id": 502,
                            "name": "Hemingway Bar",
                            "latitude": 50.084107,
                            "longitude": 14.414346,
                            "photos": "https://fastly.4sqi.net/img/general/original/30021_0V2w_ERR4QEGsisVa7IcazhXwcikucBVW5xyFrwboIE.jpg",
                            "review_score": "9.3",
                            "website": "http://www.hemingwaybar.cz/bar-praha",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 630
                        },
                        {
                            "id": 4823,
                            "city_id": 502,
                            "name": "Stalin",
                            "latitude": 50.094681,
                            "longitude": 14.416,
                            "photos": "https://fastly.4sqi.net/img/general/original/88538798_sGMgk80QTC_37Rl51KxJwbWA5bFYlpieD2N2OdvgfIg.jpg",
                            "review_score": "9.1",
                            "website": "http://www.containall.cz/stalin",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 878
                        },
                        {
                            "id": 4824,
                            "city_id": 502,
                            "name": "Kantýna",
                            "latitude": 50.083494,
                            "longitude": 14.428625,
                            "photos": "https://fastly.4sqi.net/img/general/original/6790857_ZvCxgUwJNk4uIq6BnI1xAd6gjBcY_OGHXlCpW5c6Z-E.jpg",
                            "review_score": "9.4",
                            "website": "https://www.kantyna.ambi.cz",
                            "social_media": "restaurace_kantyna",
                            "price": "4",
                            "menu": "",
                            "distance": 707
                        },
                        {
                            "id": 4825,
                            "city_id": 502,
                            "name": "Restaurace Tiskárna",
                            "latitude": 50.084194,
                            "longitude": 14.429037,
                            "photos": "https://fastly.4sqi.net/img/general/original/23124630_9g4pzoLbM4vOnMhDTMTbmn8jeGYHOqsN4HQCMdiniyk.jpg",
                            "review_score": "8.8",
                            "website": "https://www.restauracetiskarna.com",
                            "social_media": "restauracetiskarna",
                            "price": "",
                            "menu": "https://www.restauracetiskarna.com/poledniacute-menu.html",
                            "distance": 659
                        },
                        {
                            "id": 4827,
                            "city_id": 502,
                            "name": "Ambiente Pizza Nuova",
                            "latitude": 50.089344,
                            "longitude": 14.427741,
                            "photos": "https://fastly.4sqi.net/img/general/original/8354352_QEb4SiO7VQKrkddnAjFDJohqMpIhC4dkhMa_E4uXXy8.jpg",
                            "review_score": "8.7",
                            "website": "http://www.ambi.cz",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 521
                        },
                        {
                            "id": 4826,
                            "city_id": 502,
                            "name": "Letná Beer Garden",
                            "latitude": 50.095909,
                            "longitude": 14.425562,
                            "photos": "https://fastly.4sqi.net/img/general/original/28888231_n_CY5Yc_iMww1QY2CpruF1O8VqngiPNV-HhpFAoD-pg.jpg",
                            "review_score": "9.2",
                            "website": "http://www.praguebeergarden.com/pubs/post/letna-beer-garden",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 997
                        },
                        {
                            "id": 4828,
                            "city_id": 502,
                            "name": "Executive Lounge Marriott Hotel",
                            "latitude": 50.088121,
                            "longitude": 14.431377,
                            "photos": "https://fastly.4sqi.net/img/general/original/12468342_r_HUxLq4JTTPgHLXuvfmjRGxhnm50eEzPq-4Y59MMIc.jpg",
                            "review_score": "8.7",
                            "website": "",
                            "social_media": "",
                            "price": "3",
                            "menu": "",
                            "distance": 725
                        },
                        {
                            "id": 4829,
                            "city_id": 502,
                            "name": "La Bodeguita del Medio",
                            "latitude": 50.08848,
                            "longitude": 14.417156,
                            "photos": "https://fastly.4sqi.net/img/general/original/51526926_mwRmYNLXghu8JtN58F5hM2ZEwxP_WZDUFNw8cwqHh7M.jpg",
                            "review_score": "8.3",
                            "website": "http://www.labodeguitadelmedio.cz",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 320
                        },
                        {
                            "id": 4830,
                            "city_id": 502,
                            "name": "Angelato",
                            "latitude": 50.08209,
                            "longitude": 14.404681,
                            "photos": "https://fastly.4sqi.net/img/general/original/28380501_hxLv7QAF2CZGFmJZy0Ahhxccahx0SKoO2seXBxbnkMI.jpg",
                            "review_score": "9.3",
                            "website": "http://angelato.cz",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 1338
                        },
                        {
                            "id": 4831,
                            "city_id": 502,
                            "name": "Mr.HotDoG",
                            "latitude": 50.099626,
                            "longitude": 14.427809,
                            "photos": "https://fastly.4sqi.net/img/general/original/69019396_fdEC4r2Uf5p8nf1rAT7LZuc4rkEPo536zGM1fd06Klo.jpg",
                            "review_score": "9.2",
                            "website": "http://www.mrhotdog.cz",
                            "social_media": "mr.hotdogprague",
                            "price": "2",
                            "menu": "",
                            "distance": 1409
                        }
                    ],
                    "schedules": [
                        {
                            "day": 1,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3228,
                                        "city_id": 502,
                                        "name": "Illusion Art Museum Prague - IAM Prague: Hours, Address",
                                        "latitude": 50.087164,
                                        "longitude": 14.421946,
                                        "photos": "https://fastly.4sqi.net/img/general/original/187745480_Tubu3LUNmnNHan3F4ZWKJ_pQa8XQl-BBrRMgIv8bIOY.jpg",
                                        "review_score": "6.3",
                                        "description": "used to describe a wonderful event/happening. mirum videtur quod sit factum iam diu Does it seem wonderful [merely] because it was done a long time/so long",
                                        "website": "https://www.iamprague.eu",
                                        "hours_popular": "[{'close': '2100', 'day': 1, 'open': '1000'}, {'close': '1300', 'day': 2, 'open': '1100'}, {'close': '2000', 'day': 2, 'open': '1500'}, {'close': '2100', 'day': 3, 'open': '1100'}, {'close': '1900', 'day': 4, 'open': '1000'}, {'close': '2200', 'day': 5, 'open': '1200'}, {'close': '2000', 'day': 6, 'open': '0900'}, {'close': '1900', 'day': 7, 'open': '1000'}]",
                                        "distance": "79",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 2,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3227,
                                        "city_id": 502,
                                        "name": "Madame Tussauds Prague",
                                        "latitude": 50.087354,
                                        "longitude": 14.422587,
                                        "photos": "https://fastly.4sqi.net/img/general/original/390899993_9c1aBQ3-Av1q5gqFmiDnBDDMZwpsJtjy_EbG5ybV5vo.jpg",
                                        "review_score": "6.0",
                                        "description": "Madame Tussauds (UK: /tuːˈsɔːdz/, US: /tuːˈsoʊz/) is a wax museum founded in 1835 (188 years ago) (1835) by French wax sculptor Marie Tussaud in London",
                                        "website": "http://www.madametussauds.com/Prague",
                                        "hours_popular": "[{'close': '2000', 'day': 1, 'open': '1000'}, {'close': '2000', 'day': 2, 'open': '1000'}, {'close': '2000', 'day': 3, 'open': '1000'}, {'close': '2100', 'day': 4, 'open': '1000'}, {'close': '1900', 'day': 5, 'open': '1000'}, {'close': '2100', 'day': 6, 'open': '1000'}, {'close': '2000', 'day': 7, 'open': '1000'}]",
                                        "distance": "108",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 3,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3224,
                                        "city_id": 502,
                                        "name": "Prague Astronomical Clock (Pražský orloj)",
                                        "latitude": 50.08701,
                                        "longitude": 14.420725,
                                        "photos": "https://fastly.4sqi.net/img/general/original/24834822_pise1hRq_QaXC4wW7g82eUWOUq-8iejc0Ukgt2N6Fvw.jpg",
                                        "review_score": "9.1",
                                        "description": "The Prague astronomical clock or Prague Orloj (Czech: Pražský orloj [praʃskiː orloj]) is a medieval astronomical clock attached to the Old Town Hall in",
                                        "website": "http://www.staromestskaradnicepraha.cz/",
                                        "hours_popular": "[{'close': '2200', 'day': 1, 'open': '1100'}, {'close': '2100', 'day': 2, 'open': '1100'}, {'close': '2100', 'day': 3, 'open': '1100'}, {'close': '2100', 'day': 4, 'open': '1100'}, {'close': '2200', 'day': 5, 'open': '1100'}, {'close': '2200', 'day': 6, 'open': '1000'}, {'close': '2100', 'day': 7, 'open': '1000'}]",
                                        "distance": "71",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 4,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3225,
                                        "city_id": 502,
                                        "name": "Czech Beer Museum Prague",
                                        "latitude": 50.085083,
                                        "longitude": 14.418052,
                                        "photos": "https://fastly.4sqi.net/img/general/original/394858_NsyjusTj-RIoV25MQJgFdWayBa2q3S8dAXKm4SeANAw.jpg",
                                        "review_score": "7.6",
                                        "description": "Beer (Czech: pivo) has a long history in what is now the Czech Republic, with brewing taking place in Břevnov Monastery in 993. The city of Brno had the",
                                        "website": "http://www.beermuseum.cz",
                                        "hours_popular": "[{'close': '2000', 'day': 1, 'open': '1100'}, {'close': '2000', 'day': 2, 'open': '1000'}, {'close': '2100', 'day': 3, 'open': '1200'}, {'close': '1900', 'day': 4, 'open': '1200'}, {'close': '2000', 'day': 5, 'open': '1100'}, {'close': '2000', 'day': 6, 'open': '1100'}, {'close': '2000', 'day': 7, 'open': '1100'}]",
                                        "distance": "366",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 5,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3226,
                                        "city_id": 502,
                                        "name": "Republic Square (Náměstí Republiky)",
                                        "latitude": 50.088819,
                                        "longitude": 14.429677,
                                        "photos": "https://fastly.4sqi.net/img/general/original/64739172_ZFo1QWe8NaHMUbd7--X6joGXF8pDeu0Lj-Wb5V98zGg.jpg",
                                        "review_score": "8.5",
                                        "description": "Náměstí Republiky (Republic Square) is a city square in Prague, Czech Republic, lying at the boundary of the Old Town and New Town. On the square, or",
                                        "website": "http://www.dpp.cz",
                                        "hours_popular": "[{'close': '2000', 'day': 1, 'open': '0800'}, {'close': '2100', 'day': 2, 'open': '0800'}, {'close': '2100', 'day': 3, 'open': '0800'}, {'close': '2100', 'day': 4, 'open': '0800'}, {'close': '2100', 'day': 5, 'open': '0900'}, {'close': '2100', 'day': 6, 'open': '1200'}, {'close': '2000', 'day': 7, 'open': '1300'}]",
                                        "distance": "619",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 6,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3221,
                                        "city_id": 502,
                                        "name": "Palatial Gardens below Prague Castle (Palácové zahrady pod Pražským hradem)",
                                        "latitude": 50.090814,
                                        "longitude": 14.405888,
                                        "photos": "https://fastly.4sqi.net/img/general/original/337030353_aSxRMe3EkIObVQumjVAaaEykDy6fT6AauqqtxGtP99U.jpg",
                                        "review_score": "8.6",
                                        "description": "",
                                        "website": "http://www.palacove-zahrady.cz",
                                        "hours_popular": "[{'close': '1800', 'day': 1, 'open': '1200'}, {'close': '1800', 'day': 2, 'open': '1300'}, {'close': '1900', 'day': 3, 'open': '1100'}, {'close': '1800', 'day': 4, 'open': '1000'}, {'close': '1900', 'day': 5, 'open': '1100'}, {'close': '1900', 'day': 6, 'open': '1100'}, {'close': '1900', 'day': 7, 'open': '1000'}]",
                                        "distance": "1175",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 7,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3220,
                                        "city_id": 502,
                                        "name": "Czech Museum of Music (České muzeum hudby)",
                                        "latitude": 50.084909,
                                        "longitude": 14.40472,
                                        "photos": "https://fastly.4sqi.net/img/general/original/141220335_zHGPxT9AXB90oon7RQHMIzLiR48HRP5PThBNes5pgBM.jpg",
                                        "review_score": "7.4",
                                        "description": "Muzeum se nachází v bývalém barokním kostele sv. Máří Magdaleny. / Museum presents musical instruments not only as remarkable evidence of skill in craft and art, but as a fundamental mediator between human beings and music.",
                                        "website": "http://www.nm.cz/Ceske-muzeum-hudby",
                                        "hours_popular": "[{'close': '1400', 'day': 1, 'open': '0900'}, {'close': '2000', 'day': 1, 'open': '1600'}, {'close': '1400', 'day': 2, 'open': '0900'}, {'close': '2200', 'day': 2, 'open': '1600'}, {'close': '2100', 'day': 3, 'open': '0900'}, {'close': '1400', 'day': 4, 'open': '0800'}, {'close': '2100', 'day': 4, 'open': '1600'}, {'close': '1400', 'day': 5, 'open': '0900'}, {'close': '2000', 'day': 5, 'open': '1600'}, {'close': '2300', 'day': 6, 'open': '0900'}, {'close': '2000', 'day': 7, 'open': '0900'}]",
                                        "distance": "1189",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "city": "Cesky Krumlov",
                    "description": "A picturesque town famous for its medieval castle and charming old town.",
                    "restaurants": [
                        {
                            "id": 4802,
                            "city_id": 501,
                            "name": "Apotheka",
                            "latitude": 48.812556,
                            "longitude": 14.317551,
                            "photos": "https://fastly.4sqi.net/img/general/original/44274368_6ks1hkwK7t4qObtv2w74emgrqPuXWY9XNKAWjWC9FG0.jpg",
                            "review_score": "9.0",
                            "website": "http://apothekabar.wz.cz",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 845
                        },
                        {
                            "id": 4803,
                            "city_id": 501,
                            "name": "Synagoga Cafe & Bistrot",
                            "latitude": 48.807598,
                            "longitude": 14.318126,
                            "photos": "https://fastly.4sqi.net/img/general/original/16840105_ubsXZa-hCozn8OjX9oqhuEhdQBE9wSUh9Nx_OIolcZg.jpg",
                            "review_score": "8.5",
                            "website": "http://www.synagoga-krumlov.cz",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 286
                        },
                        {
                            "id": 4804,
                            "city_id": 501,
                            "name": "Řízková restaurace Pivoňka",
                            "latitude": 48.804393,
                            "longitude": 14.311705,
                            "photos": "https://fastly.4sqi.net/img/general/original/5284583_iGgI3aTojaH7yGBlzWaVe4cX3U__iCklk9woWie4tVs.jpg",
                            "review_score": "8.6",
                            "website": "https://www.rizekprespultalire.cz/pivonka",
                            "social_media": "restaurace_pivonka",
                            "price": "1",
                            "menu": "",
                            "distance": 338
                        },
                        {
                            "id": 4805,
                            "city_id": 501,
                            "name": "Papa's Living Restaurant",
                            "latitude": 48.811769,
                            "longitude": 14.316708,
                            "photos": "https://fastly.4sqi.net/img/general/original/6335431_1wu8pK5ejbnsAiBQjQRnTKfHAmi-JLmzQhhZtWlwn1Y.jpg",
                            "review_score": "8.0",
                            "website": "http://www.papas.cz",
                            "social_media": "",
                            "price": "3",
                            "menu": "",
                            "distance": 735
                        },
                        {
                            "id": 4806,
                            "city_id": 501,
                            "name": "Zapa Bar",
                            "latitude": 48.812208,
                            "longitude": 14.316979,
                            "photos": "https://fastly.4sqi.net/img/general/original/31673292_gAv5wXFK2-Ld8okV00KyPSVYZUvMbzDpKfq_TFz-2Lk.jpg",
                            "review_score": "9.0",
                            "website": "http://www.zapabar.cz",
                            "social_media": "",
                            "price": "3",
                            "menu": "http://www.zapabar.cz/napoje/top-10",
                            "distance": 767
                        },
                        {
                            "id": 4807,
                            "city_id": 501,
                            "name": "Krčma Šatlava",
                            "latitude": 48.810613,
                            "longitude": 14.315936,
                            "photos": "https://fastly.4sqi.net/img/general/original/8723429_zYgoxkaUL2-T5eX66kbrIpd6u1C2bc_ptrro1UTTyUs.jpg",
                            "review_score": "8.1",
                            "website": "",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 625
                        },
                        {
                            "id": 4808,
                            "city_id": 501,
                            "name": "Restaurace Jelenka",
                            "latitude": 48.813779,
                            "longitude": 14.312555,
                            "photos": "https://fastly.4sqi.net/img/general/original/6481952_niiG9StXZ9PAKKxid-R5WyjOSdf5eExB8Vyfg8JQeRY.jpg",
                            "review_score": "8.3",
                            "website": "http://www.firmy.cz/detail/2325941-restaurace-jelenka-cesky-krumlov-latran.html",
                            "social_media": "",
                            "price": "3",
                            "menu": "",
                            "distance": 1011
                        },
                        {
                            "id": 4809,
                            "city_id": 501,
                            "name": "Grill bar Pod Barevnou skálou",
                            "latitude": 48.792942,
                            "longitude": 14.305947,
                            "photos": "https://fastly.4sqi.net/img/general/original/3962106_BncdW_s9-v1b-Lq6KqyMxxFKKixdbTYstVY7vVy7MrE.jpg",
                            "review_score": "8.2",
                            "website": "http://www.jedu-vodu.cz",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 1549
                        },
                        {
                            "id": 4810,
                            "city_id": 501,
                            "name": "Synagoga",
                            "latitude": 48.807577,
                            "longitude": 14.317733,
                            "photos": "https://fastly.4sqi.net/img/general/original/49498248_fOV2ze5FHcVnKr2-kqJJ-GSkxCI4MRI-sDJ2B6l4IaM.jpg",
                            "review_score": "7.5",
                            "website": "http://www.synagoga-krumlov.cz",
                            "social_media": "",
                            "price": "",
                            "menu": "",
                            "distance": 292
                        },
                        {
                            "id": 4811,
                            "city_id": 501,
                            "name": "IDEÁL - Pražírna kávy / Coffee roastery",
                            "latitude": 48.808302,
                            "longitude": 14.316892,
                            "photos": "https://fastly.4sqi.net/img/general/original/4117318_j4lVpBZgp1xCoe2_uh8zcrlBYLnlNNe5S_ZUGxZYYlQ.jpg",
                            "review_score": "7.7",
                            "website": "http://www.ideal.coffee",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 363
                        }
                    ],
                    "schedules": [
                        {
                            "day": 1,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3200,
                                        "city_id": 501,
                                        "name": "Krumlovská Fontána",
                                        "latitude": 48.810659,
                                        "longitude": 14.314978,
                                        "photos": "https://fastly.4sqi.net/img/general/original/520266088_uSi70vgvnOkKYSX1ZUiRWnAcnQOUPi_lQCBUn2auPOs.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "622",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3203,
                                        "city_id": 501,
                                        "name": "Museum of torture Cesky Krumlov: Address, Phone Number",
                                        "latitude": 48.810895,
                                        "longitude": 14.31523,
                                        "photos": "https://fastly.4sqi.net/img/general/original/49498248_E6UQcVRZeZw32mMaTpxZCypuOa65FfWvTbETMKy_TGw.jpg",
                                        "review_score": "6.2",
                                        "description": "",
                                        "website": "http://www.waxmuseumprague.cz/wax-museum-cesky-krumlov",
                                        "hours_popular": "",
                                        "distance": "629",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3204,
                                        "city_id": 501,
                                        "name": "Krumlov",
                                        "latitude": 48.81052,
                                        "longitude": 14.313213,
                                        "photos": "https://live.staticflickr.com/5616/15639960098_ca2993820a_o.jpg",
                                        "review_score": "0",
                                        "description": "Krumlov may refer to:Český Krumlov, a town in South Bohemia, Czech Republic\nDuchy of Krumlov, a titular duchy of the Bohemia\nMoravský Krumlov, a town in South Moravia, Czech Republic\n",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "639",
                                        "real_price": "",
                                        "start_time": "16:00",
                                        "end_time": "19:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 2,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3205,
                                        "city_id": 501,
                                        "name": "Český Krumlov Vltava",
                                        "latitude": 48.811821,
                                        "longitude": 14.314685,
                                        "photos": "https://fastly.4sqi.net/img/general/original/53148607_-PMBmPl3n3aF9j09hLuMENUjxapIeYQR6N6ltE-kzBY.jpg",
                                        "review_score": "0",
                                        "description": "Český Krumlov (Czech pronunciation: [ˈtʃɛskiː ˈkrumlof] (listen); German: Krumau or Böhmisch Krumau) is a town in the South Bohemian Region of the Czech",
                                        "website": "",
                                        "hours_popular": "[{'close': '1500', 'day': 1, 'open': '1100'}, {'close': '1900', 'day': 1, 'open': '1800'}, {'close': '1700', 'day': 2, 'open': '1200'}, {'close': '1900', 'day': 3, 'open': '1100'}, {'close': '1700', 'day': 4, 'open': '1100'}, {'close': '1600', 'day': 5, 'open': '1100'}, {'close': '2000', 'day': 6, 'open': '1000'}, {'close': '1700', 'day': 7, 'open': '1100'}]",
                                        "distance": "766",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3208,
                                        "city_id": 501,
                                        "name": "Muzeum stavebních dějin a řemesel v Českém Krumlově",
                                        "latitude": 48.811674,
                                        "longitude": 14.313905,
                                        "photos": "https://live.staticflickr.com/65535/53027010395_89ff6eccc9_o.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "http://www.ckrumlov.cz/artes",
                                        "hours_popular": "",
                                        "distance": "804",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3201,
                                        "city_id": 501,
                                        "name": "Regionální muzeum v Českém Krumlově",
                                        "latitude": 48.810702,
                                        "longitude": 14.317606,
                                        "photos": "https://fastly.4sqi.net/img/general/original/966054_e2lkPpJXEyIUPofJ1UzGffU5IzwJLYeApm2rlSRnD2A.jpg",
                                        "review_score": "7.3",
                                        "description": "",
                                        "website": "http://www.museum-krumlov.eu",
                                        "hours_popular": "",
                                        "distance": "624",
                                        "real_price": "",
                                        "start_time": "16:00",
                                        "end_time": "19:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 3,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3207,
                                        "city_id": 501,
                                        "name": "Český Krumlov Castle (Státní hrad a zámek Český Krumlov)",
                                        "latitude": 48.812683,
                                        "longitude": 14.314932,
                                        "photos": "https://fastly.4sqi.net/img/general/original/6419761_Ni97ot5ZXOb5aHvFJRbZchGGdxlySMNgs8YB-FDE7yU.jpg",
                                        "review_score": "9.3",
                                        "description": "30 July 2019. History of Český Krumlov castle Státní hrad a zámek Český Krumlov web pages \"Tales of the White Lady\". Castle.ckrumlov.cz. Wikimedia Commons",
                                        "website": "https://www.zamek-ceskykrumlov.cz",
                                        "hours_popular": "[{'close': '1600', 'day': 1, 'open': '1100'}, {'close': '1700', 'day': 2, 'open': '1000'}, {'close': '1700', 'day': 3, 'open': '1000'}, {'close': '1700', 'day': 4, 'open': '1100'}, {'close': '2000', 'day': 5, 'open': '1000'}, {'close': '2100', 'day': 6, 'open': '1000'}, {'close': '1800', 'day': 7, 'open': '1000'}]",
                                        "distance": "830",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3202,
                                        "city_id": 501,
                                        "name": "Běžecká stezka Český Krumlov",
                                        "latitude": 48.815666,
                                        "longitude": 14.309223,
                                        "photos": "https://fastly.4sqi.net/img/general/original/52674843_mjoAFJ3U5SMtGTQWg5eJUYFB4PeDAJSveI4ZSdqWFxg.jpg",
                                        "review_score": "8.1",
                                        "description": "",
                                        "website": "",
                                        "hours_popular": "[{'close': '1600', 'day': 1, 'open': '1000'}, {'close': '1700', 'day': 2, 'open': '1000'}, {'close': '2200', 'day': 2, 'open': '2100'}, {'close': '1700', 'day': 3, 'open': '1000'}, {'close': '2000', 'day': 4, 'open': '0900'}, {'close': '1400', 'day': 5, 'open': '0900'}, {'close': '1700', 'day': 5, 'open': '1600'}, {'close': '1800', 'day': 6, 'open': '0900'}, {'close': '1700', 'day': 7, 'open': '1200'}]",
                                        "distance": "1278",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3199,
                                        "city_id": 501,
                                        "name": "Grafitový důl pod Českým Krumlovem",
                                        "latitude": 48.816967,
                                        "longitude": 14.30459,
                                        "photos": "https://fastly.4sqi.net/img/general/original/584383187_ebgUljXrjeImger-xfDRdD-CbxywLjS4ZRBBhQby1Xs.jpg",
                                        "review_score": "8.7",
                                        "description": "prohlídka v češtině (Děti od 3 - 15 let - 80Kč) 150 Kč prohlídka v cizím jazyce (Děti 3 - 15 let - 100Kč) 200 Kč",
                                        "website": "http://www.grafitovydul.cz",
                                        "hours_popular": "[{'close': '1600', 'day': 1, 'open': '0900'}, {'close': '1600', 'day': 2, 'open': '0900'}, {'close': '1500', 'day': 3, 'open': '0900'}, {'close': '1700', 'day': 4, 'open': '1000'}, {'close': '2000', 'day': 4, 'open': '1900'}, {'close': '1400', 'day': 5, 'open': '0900'}, {'close': '2300', 'day': 5, 'open': '2100'}, {'close': '1900', 'day': 6, 'open': '0900'}, {'close': '1600', 'day': 7, 'open': '1000'}]",
                                        "distance": "1547",
                                        "real_price": "",
                                        "start_time": "16:00",
                                        "end_time": "19:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "city": "Karlovy Vary",
                    "description": "A spa town known for its hot springs, beautiful promenades, and stunning architecture.",
                    "restaurants": [
                        {
                            "id": 4772,
                            "city_id": 498,
                            "name": "Čajovna Universal",
                            "latitude": 50.230636,
                            "longitude": 12.869115,
                            "photos": "https://fastly.4sqi.net/img/general/original/523347386_3N6Mh2xZEnTBSw_E-ZWb4t-KatnF_Q1YLQtC7dyEuzo.jpg",
                            "review_score": "9.1",
                            "website": "",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 79
                        },
                        {
                            "id": 4773,
                            "city_id": 498,
                            "name": "Café KAVA",
                            "latitude": 50.228729,
                            "longitude": 12.870166,
                            "photos": "https://fastly.4sqi.net/img/general/original/34091958_gus1xxPGNhH7dK3z6qt6YrK3QxKtLRsmrJFEuzU9muE.jpg",
                            "review_score": "8.8",
                            "website": "http://cafekava.cz",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 198
                        },
                        {
                            "id": 4774,
                            "city_id": 498,
                            "name": "Republica Coffee",
                            "latitude": 50.23007,
                            "longitude": 12.869209,
                            "photos": "https://fastly.4sqi.net/img/general/original/7596817_mQ6wplEjCo0kEm_8YG2KqNntBmumCQb-uMF_0tRlfTo.jpg",
                            "review_score": "8.6",
                            "website": "",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 101
                        },
                        {
                            "id": 4775,
                            "city_id": 498,
                            "name": "Rad's Baguettes",
                            "latitude": 50.229449,
                            "longitude": 12.869258,
                            "photos": "https://fastly.4sqi.net/img/general/original/31506981_H7c9oG_WZLY3FGOdvbxzzVn_7-XS9ywCaolaEL3mnXw.jpg",
                            "review_score": "8.1",
                            "website": "",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 159
                        },
                        {
                            "id": 4776,
                            "city_id": 498,
                            "name": "Becherplatz",
                            "latitude": 50.230326,
                            "longitude": 12.867118,
                            "photos": "https://fastly.4sqi.net/img/general/original/43829714_Jx2UnwlqQulpu7taCFWM4NnL1Z2vqFxafsKtfPUioOY.jpg",
                            "review_score": "8.3",
                            "website": "http://www.becherplatz.cz",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 213
                        },
                        {
                            "id": 4777,
                            "city_id": 498,
                            "name": "Bagel Lounge",
                            "latitude": 50.230047,
                            "longitude": 12.868061,
                            "photos": "https://fastly.4sqi.net/img/general/original/83219471_tqK12JqxSqs47xIthMr8HGyCly3vNVmHPY-jSL3EN_U.jpg",
                            "review_score": "8.6",
                            "website": "http://bagellounge.cz",
                            "social_media": "bagellounge_kv",
                            "price": "1",
                            "menu": "",
                            "distance": 149
                        },
                        {
                            "id": 4778,
                            "city_id": 498,
                            "name": "Rozhledna Diana",
                            "latitude": 50.218738,
                            "longitude": 12.871653,
                            "photos": "https://fastly.4sqi.net/img/general/original/115042_NrTWzBXXNnmGXLGrJw5ZTYVy3YTuqdaozw4fbqGZw4A.jpg",
                            "review_score": "8.8",
                            "website": "http://www.dianakv.cz",
                            "social_media": "",
                            "price": "",
                            "menu": "",
                            "distance": 1314
                        },
                        {
                            "id": 4779,
                            "city_id": 498,
                            "name": "Tapas & Steak - Sabor Mediterraneo",
                            "latitude": 50.228661,
                            "longitude": 12.865968,
                            "photos": "https://fastly.4sqi.net/img/general/original/464003674_AkSNy_ap4TGbEbjLXbCxALZw-A8lMaAiDQ1C-qkmNHo.jpg",
                            "review_score": "8.5",
                            "website": "http://sabor.cz",
                            "social_media": "tapas_bar_kv",
                            "price": "2",
                            "menu": "",
                            "distance": 384
                        },
                        {
                            "id": 4780,
                            "city_id": 498,
                            "name": "Špunt & Knoflík",
                            "latitude": 50.229418,
                            "longitude": 12.866409,
                            "photos": "https://fastly.4sqi.net/img/general/original/71518136_MDcOXAuw29EqPVj97pCoxride8Ts-jTMgjULHdT7nJ8.jpg",
                            "review_score": "9.0",
                            "website": "http://www.spuntaknoflik.com",
                            "social_media": "spuntaknoflik",
                            "price": "",
                            "menu": "",
                            "distance": 277
                        },
                        {
                            "id": 4781,
                            "city_id": 498,
                            "name": "Lékárna by City Roasters",
                            "latitude": 50.230011,
                            "longitude": 12.868313,
                            "photos": "https://fastly.4sqi.net/img/general/original/64709762_d6piZyufjtHF5Otm6VEDaXQgyKX_LqS2wEVSO6SrMXY.jpg",
                            "review_score": "8.1",
                            "website": "http://www.cityroasters.eu",
                            "social_media": "lekarnacityroasters",
                            "price": "1",
                            "menu": "",
                            "distance": 154
                        }
                    ],
                    "schedules": [
                        {
                            "day": 1,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3180,
                                        "city_id": 498,
                                        "name": "Junák - český skaut, Přístav ORION Karlovy Vary, z.s.",
                                        "latitude": 50.21324,
                                        "longitude": 12.816045,
                                        "photos": "https://live.staticflickr.com/65535/53035304797_0338825d5f_o.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "http://www.pristavorion.cz",
                                        "hours_popular": "",
                                        "distance": "4304",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3177,
                                        "city_id": 498,
                                        "name": "Dětské Hřiště Varyáda",
                                        "latitude": 50.227551,
                                        "longitude": 12.842749,
                                        "photos": "https://fastly.4sqi.net/img/general/original/11204590_9ODm_gXg4w4fF2ugqxd6-TN31m1KQQYJjVYqIzwxrRM.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "1977",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 2,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3178,
                                        "city_id": 498,
                                        "name": "JK Karlovy Vary - St. Role",
                                        "latitude": 50.235002,
                                        "longitude": 12.826442,
                                        "photos": "https://live.staticflickr.com/65535/53035304797_0338825d5f_o.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "3150",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3175,
                                        "city_id": 498,
                                        "name": "SCHLECKER - KARLOVY VARY - Třída T. G. Masaryka 23",
                                        "latitude": 50.229686,
                                        "longitude": 12.870491,
                                        "photos": "https://fastly.4sqi.net/img/general/original/177841092_4PMsgaGxsmRDaqfjGeUxkbfL9WIMDUYgdlcK9tkmNCs.jpg",
                                        "review_score": "8.0",
                                        "description": "",
                                        "website": "http://www.schlecker.cz",
                                        "hours_popular": "[{'close': '2000', 'day': 1, 'open': '0900'}, {'close': '2000', 'day': 2, 'open': '1100'}, {'close': '1800', 'day': 3, 'open': '1000'}, {'close': '1800', 'day': 4, 'open': '1000'}, {'close': '2200', 'day': 5, 'open': '0900'}, {'close': '1900', 'day': 6, 'open': '1000'}, {'close': '1800', 'day': 7, 'open': '1000'}]",
                                        "distance": "121",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 3,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3176,
                                        "city_id": 498,
                                        "name": "Karlovy Vary",
                                        "latitude": 50.231847,
                                        "longitude": 12.871721,
                                        "photos": "https://live.staticflickr.com/4852/46803547661_d3d093fa47_o.jpg",
                                        "review_score": "0",
                                        "description": "Karlovy Vary is a spa city in the Karlovy Vary Region of the Czech Republic. It has about 49,000 inhabitants. It lies at the confluence of the rivers Ohře and Teplá. It is named after Charles IV, Holy Roman Emperor and the King of Bohemia, who founded the city.",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "176",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3181,
                                        "city_id": 498,
                                        "name": "Park - Interhotel Central",
                                        "latitude": 50.221751,
                                        "longitude": 12.882151,
                                        "photos": "https://fastly.4sqi.net/img/general/original/41809586__f38LD_e8wEzzo_IZm4E0HPEV_E9p6T8hihJHYmZy5U.jpg",
                                        "review_score": "0",
                                        "description": "square. The hotel opened as the Hotel Stadt Berlin, part of East Germany's Interhotel chain. It was a four-star hotel and mainly served for the accommodation",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "1303",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "city": "Kutna Hora",
                    "description": "A UNESCO World Heritage site with attractions like the Sedlec Ossuary and St. Barbara's Church.",
                    "restaurants": [
                        {
                            "id": 4834,
                            "city_id": 503,
                            "name": "Kafírnictví – Tvoje dílna",
                            "latitude": 49.949314,
                            "longitude": 15.269318,
                            "photos": "https://fastly.4sqi.net/img/general/original/89847204_DlJxVtjEB44rqtfSKCVki1IHo4LOU7B5ZNCQ7BvhNno.jpg",
                            "review_score": "8.5",
                            "website": "https://www.tvojedilna.com",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 99
                        },
                        {
                            "id": 4833,
                            "city_id": 503,
                            "name": "Turistka",
                            "latitude": 49.947342,
                            "longitude": 15.264634,
                            "photos": "https://fastly.4sqi.net/img/general/original/88169167_vSmEU1orA1dRWbpYjMevrMmYk6IaxwKAZ8Tu1y3RJhQ.jpg",
                            "review_score": "8.5",
                            "website": "",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 288
                        },
                        {
                            "id": 4832,
                            "city_id": 503,
                            "name": "Zmrzlinárna",
                            "latitude": 49.94882,
                            "longitude": 15.267634,
                            "photos": "https://fastly.4sqi.net/img/general/original/89847204_SZqU0YCZjvfXtKizpqD20TWGTzi1D4zor1PK6iE4EKk.jpg",
                            "review_score": "8.6",
                            "website": "http://www.zmrzlinarna.com",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 53
                        },
                        {
                            "id": 4835,
                            "city_id": 503,
                            "name": "Penzion a Restaurant Barbora",
                            "latitude": 49.945768,
                            "longitude": 15.262554,
                            "photos": "https://fastly.4sqi.net/img/general/original/8295932_jvIGpTCqF2vHZnVyr4xVYSdrBN9i-5fxV4ak-wdA1Jw.jpg",
                            "review_score": "8.1",
                            "website": "http://www.penzionbarbora.cz",
                            "social_media": "",
                            "price": "",
                            "menu": "",
                            "distance": 523
                        },
                        {
                            "id": 4836,
                            "city_id": 503,
                            "name": "Kavárna na Kozím plácku",
                            "latitude": 49.948357,
                            "longitude": 15.266651,
                            "photos": "https://fastly.4sqi.net/img/general/original/53793447_8ku5jo1ctR80PuIPvu1G7rY2zHFCkCKD1S7SrOdVQhU.jpg",
                            "review_score": "8.3",
                            "website": "http://www.koziplacek.cz",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 115
                        },
                        {
                            "id": 4837,
                            "city_id": 503,
                            "name": "Zmrzlina Karlov",
                            "latitude": 49.946382,
                            "longitude": 15.292709,
                            "photos": "https://fastly.4sqi.net/img/general/original/345896027_QO3zoFsy2LVsAT1s8U6NWuRrxdySXICBUdz3E38p7fw.jpg",
                            "review_score": "8.5",
                            "website": "",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 1776
                        },
                        {
                            "id": 4838,
                            "city_id": 503,
                            "name": "Café Havlíček Penzion",
                            "latitude": 49.948819,
                            "longitude": 15.268788,
                            "photos": "https://fastly.4sqi.net/img/general/original/212651274_z4HURCfE_hBFAiCU4p4JRPBAb4I9doSogYDQCfVeUvU.jpg",
                            "review_score": "7.7",
                            "website": "http://www.cafehavlicekpenzion.cz",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 52
                        },
                        {
                            "id": 4839,
                            "city_id": 503,
                            "name": "Restaurace Dačický",
                            "latitude": 49.948263,
                            "longitude": 15.264548,
                            "photos": "https://fastly.4sqi.net/img/general/original/37516637_lcXqvOsKfgGqlbeL162ACurXt7be2wxlU80c9QNVRVw.jpg",
                            "review_score": "8.4",
                            "website": "http://www.dacicky.com",
                            "social_media": "",
                            "price": "",
                            "menu": "http://www.dacicky.com/jidelni-listek/",
                            "distance": 241
                        },
                        {
                            "id": 4840,
                            "city_id": 503,
                            "name": "Factory",
                            "latitude": 49.94997,
                            "longitude": 15.265274,
                            "photos": "https://fastly.4sqi.net/img/general/original/1391496394_tUTO5y4qOup8myCaXMItxu3vyFGWdp_nwsXOiJ0j6Nk.jpg",
                            "review_score": "7.8",
                            "website": "http://www.factorybistro.cz",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 238
                        },
                        {
                            "id": 4841,
                            "city_id": 503,
                            "name": "V Ruthardce",
                            "latitude": 49.94809,
                            "longitude": 15.266513,
                            "photos": "https://fastly.4sqi.net/img/general/original/72800758_ah5PlUHL0rFjKbNmhvnid6plstY8b3LINFb9DJ901QQ.jpg",
                            "review_score": "8.1",
                            "website": "http://www.v-ruthardce.cz",
                            "social_media": "",
                            "price": "",
                            "menu": "",
                            "distance": 134
                        }
                    ],
                    "schedules": [
                        {
                            "day": 1,
                            "attractions": [
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 2,
                            "attractions": [
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 3,
                            "attractions": [
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "city": "Brno",
                    "description": "The second-largest city in Czech Republic with a rich history, cultural sites, and vibrant nightlife.",
                    "restaurants": [
                        {
                            "id": 4799,
                            "city_id": 500,
                            "name": "Gỗ",
                            "latitude": 49.19603,
                            "longitude": 16.609145,
                            "photos": "https://fastly.4sqi.net/img/general/original/58860187_LGNcJtaN-BnXM62pidtZ9icSZRBOxfxqVFenGgHMqqA.jpg",
                            "review_score": "9.0",
                            "website": "",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 434
                        },
                        {
                            "id": 4786,
                            "city_id": 500,
                            "name": "3f by Mori",
                            "latitude": 49.194586,
                            "longitude": 16.610278,
                            "photos": "https://fastly.4sqi.net/img/general/original/208228410_qtUho4oBcd3nqBGcoLD7S4sB9bftTbi3Ca_it_QWY2k.jpg",
                            "review_score": "8.9",
                            "website": "",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 260
                        },
                        {
                            "id": 4787,
                            "city_id": 500,
                            "name": "Monogram Espresso Bar",
                            "latitude": 49.191721,
                            "longitude": 16.610053,
                            "photos": "https://fastly.4sqi.net/img/general/original/582098030_Tt2-Z5rOXtu-Xn2qCPalBMsBoXmuVyAMErNFaSGtf7o.jpg",
                            "review_score": "9.1",
                            "website": "http://www.monogramespressobar.cz",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 129
                        },
                        {
                            "id": 4789,
                            "city_id": 500,
                            "name": "SKØG Urban Hub",
                            "latitude": 49.193905,
                            "longitude": 16.607257,
                            "photos": "https://fastly.4sqi.net/img/general/original/43399853_7UgPCr15wa6kKOzZMNOFrO5r_DjH8UML9VDXoc9RAlI.jpg",
                            "review_score": "9.1",
                            "website": "http://www.skog.cz",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 346
                        },
                        {
                            "id": 4790,
                            "city_id": 500,
                            "name": "Ještě jednu",
                            "latitude": 49.194275,
                            "longitude": 16.610665,
                            "photos": "https://fastly.4sqi.net/img/general/original/82819877_KDLVI0fBNVcd2yrsQWlw7tKPDt0-pPGoSwG-hA8CNR8.jpg",
                            "review_score": "9.1",
                            "website": "https://www.jestejednu.cz",
                            "social_media": "jeste_jednu",
                            "price": "1",
                            "menu": "",
                            "distance": 230
                        },
                        {
                            "id": 4792,
                            "city_id": 500,
                            "name": "Café Tungsram",
                            "latitude": 49.191698,
                            "longitude": 16.609357,
                            "photos": "https://fastly.4sqi.net/img/general/original/56571350_2mMg7urOueXYIjVYRTQfdeufDC3jmr-XiwapIvZN2SU.jpg",
                            "review_score": "8.7",
                            "website": "http://www.tungsram.cz",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 159
                        },
                        {
                            "id": 4794,
                            "city_id": 500,
                            "name": "4Pokoje",
                            "latitude": 49.1957508,
                            "longitude": 16.6118183,
                            "photos": "https://fastly.4sqi.net/img/general/original/161607316_4wSG14r_soGln_BarzEOHDLJmcnjpEOFX1W-9WOp7dw.jpg",
                            "review_score": "9.1",
                            "website": "https://www.miluju4pokoje.cz",
                            "social_media": "4pokojebrno",
                            "price": "2",
                            "menu": "",
                            "distance": 391
                        },
                        {
                            "id": 4796,
                            "city_id": 500,
                            "name": "Výčep Na stojáka",
                            "latitude": 49.196828,
                            "longitude": 16.609274,
                            "photos": "https://fastly.4sqi.net/img/general/original/40399550_cuysRhVfCfFej00xYRvu2RNsze-mEDhxGPc6VKnSjCA.jpg",
                            "review_score": "9.1",
                            "website": "http://www.vycepnastojaka.cz",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 526
                        },
                        {
                            "id": 4798,
                            "city_id": 500,
                            "name": "CAFÉ Momenta",
                            "latitude": 49.192506,
                            "longitude": 16.609784,
                            "photos": "https://fastly.4sqi.net/img/general/original/161607316_d5VXLd0oSUwbo67Gxph713u65Hi2hFieMy9dDERQXQA.jpg",
                            "review_score": "9.0",
                            "website": "http://www.kafevbrne.cz/2015/07/na-moment-v-cafe-momenta.html",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 122
                        },
                        {
                            "id": 4800,
                            "city_id": 500,
                            "name": "Výčep Na stojáka Pekanda",
                            "latitude": 49.192394,
                            "longitude": 16.604756,
                            "photos": "https://fastly.4sqi.net/img/general/original/8582949_CpOSjeFuvdfgpj36f8fbxfg4PR5kLhKgi59Q7EpfJEg.jpg",
                            "review_score": "9.0",
                            "website": "http://www.vycepnastojaka.cz",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 471
                        }
                    ],
                    "schedules": [
                        {
                            "day": 1,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3182,
                                        "city_id": 500,
                                        "name": "Diocesan Museum (Diecézní muzeum)",
                                        "latitude": 49.191422,
                                        "longitude": 16.607371,
                                        "photos": "https://fastly.4sqi.net/img/general/original/20503962_BUvnHI0hSi2OWc470HxmSeipvyEl1EOyVuJwHzXhQT0.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "https://www.dieceznimuzeum.cz",
                                        "hours_popular": "",
                                        "distance": "295",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3191,
                                        "city_id": 500,
                                        "name": "GE bankomat | Brno - Zelný trh",
                                        "latitude": 49.192621,
                                        "longitude": 16.608436,
                                        "photos": "https://live.staticflickr.com/65535/53046123362_19ac907a34_o.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "214",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 2,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3198,
                                        "city_id": 500,
                                        "name": "Brno Y Castillo Špilberk",
                                        "latitude": 49.194607,
                                        "longitude": 16.599026,
                                        "photos": "https://live.staticflickr.com/7201/7133261963_5b4d23d22a_o.jpg",
                                        "review_score": "0",
                                        "description": "fortifications are preserved Jablunkovské šance in Mosty u Jablunkova Hrad Špilberk, Brno, bastions of the city itself were dismantled Vyšehrad, Prague, large",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "931",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3184,
                                        "city_id": 500,
                                        "name": "Cyklistická stezka Brno-Vídeň",
                                        "latitude": 49.182966,
                                        "longitude": 16.604676,
                                        "photos": "https://fastly.4sqi.net/img/general/original/365387960_DMXs72OZDsPDOel6ZVdj0X1zztYSMXteTrEUImsEWD4.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "",
                                        "hours_popular": "[{'close': '0900', 'day': 1, 'open': '0700'}, {'close': '1200', 'day': 1, 'open': '1100'}, {'close': '2000', 'day': 1, 'open': '1400'}, {'close': '1200', 'day': 2, 'open': '0700'}, {'close': '2100', 'day': 2, 'open': '1500'}, {'close': '1100', 'day': 3, 'open': '0700'}, {'close': '2000', 'day': 3, 'open': '1300'}, {'close': '0900', 'day': 4, 'open': '0700'}, {'close': '1200', 'day': 4, 'open': '1100'}, {'close': '2000', 'day': 4, 'open': '1500'}, {'close': '1000', 'day': 5, 'open': '0700'}, {'close': '2000', 'day': 5, 'open': '1500'}, {'close': '0900', 'day': 6, 'open': '0800'}, {'close': '2000', 'day': 6, 'open': '1200'}, {'close': '2000', 'day': 7, 'open': '1100'}]",
                                        "distance": "1138",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 3,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3196,
                                        "city_id": 500,
                                        "name": "Vyhlídka na Brno",
                                        "latitude": 49.193871,
                                        "longitude": 16.592903,
                                        "photos": "https://fastly.4sqi.net/img/general/original/438335522_Ro3VluZ5EO7VI_oaO-BwHAx82BVY0QeXjobJcN_QWwA.jpg",
                                        "review_score": "0",
                                        "description": "conformity with EU standards. Mikulovská is located within the Breclav and Brno-venkov geopolitical districts of the South Moravian Region. Here the tail",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "1350",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3192,
                                        "city_id": 500,
                                        "name": "Brno autokino",
                                        "latitude": 49.190945,
                                        "longitude": 16.5747,
                                        "photos": "https://live.staticflickr.com/65535/53046123362_19ac907a34_o.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "http://www.brnoautokino.cz",
                                        "hours_popular": "",
                                        "distance": "2664",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 4,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3183,
                                        "city_id": 500,
                                        "name": "Inline trasa podél Svratky",
                                        "latitude": 49.171934,
                                        "longitude": 16.625976,
                                        "photos": "https://fastly.4sqi.net/img/general/original/30180048_vfIy4HKPJd6x8ZfSNH3qBQFix2FDa_4eYesEeXQkmoE.jpg",
                                        "review_score": "7.2",
                                        "description": "",
                                        "website": "",
                                        "hours_popular": "[{'close': '2100', 'day': 1, 'open': '1100'}, {'close': '2100', 'day': 2, 'open': '1000'}, {'close': '1200', 'day': 3, 'open': '0900'}, {'close': '2000', 'day': 3, 'open': '1600'}, {'close': '1400', 'day': 4, 'open': '1000'}, {'close': '2100', 'day': 4, 'open': '1600'}, {'close': '1400', 'day': 5, 'open': '1000'}, {'close': '2100', 'day': 5, 'open': '1600'}, {'close': '2000', 'day': 6, 'open': '1100'}, {'close': '2000', 'day': 7, 'open': '1100'}]",
                                        "distance": "2494",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3194,
                                        "city_id": 500,
                                        "name": "Brno Riviera",
                                        "latitude": 49.188203,
                                        "longitude": 16.569154,
                                        "photos": "https://fastly.4sqi.net/img/general/original/115686380__bDLb8GKcSjQEmmUpg1gCthJDVyPGJJTXJ8mMkVzQoE.jpg",
                                        "review_score": "7.9",
                                        "description": "results\" (PDF). MotoGP. Retrieved 2 July 2018. \"2010 San Marino and Rimini Riviera Grand Prix results\" (PDF). MotoGP. Retrieved 2 July 2018. \"2010 Japanese",
                                        "website": "http://www.rivec.cz",
                                        "hours_popular": "[{'close': '1900', 'day': 1, 'open': '1300'}, {'close': '2000', 'day': 2, 'open': '1500'}, {'close': '1900', 'day': 3, 'open': '1400'}, {'close': '2000', 'day': 4, 'open': '1400'}, {'close': '2000', 'day': 5, 'open': '1500'}, {'close': '2100', 'day': 6, 'open': '0800'}, {'close': '1900', 'day': 7, 'open': '1100'}]",
                                        "distance": "2917",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "city": "Olomouc",
                    "description": "A city known for its beautiful architecture, historical landmarks, and vibrant atmosphere.",
                    "restaurants": [
                        {
                            "id": 4782,
                            "city_id": 499,
                            "name": "Kafe Jak Lusk",
                            "latitude": 49.594931,
                            "longitude": 17.24696,
                            "photos": "https://fastly.4sqi.net/img/general/original/23353779_y_FHyTCQOzCflNKmma-eMH0-GPG_pgr-UIMDToZpJPs.jpg",
                            "review_score": "9.0",
                            "website": "http://www.kafejaklusk.cz",
                            "social_media": "kafejaklusk",
                            "price": "1",
                            "menu": "",
                            "distance": 313
                        },
                        {
                            "id": 4783,
                            "city_id": 499,
                            "name": "Café na cucky",
                            "latitude": 49.592489,
                            "longitude": 17.251967,
                            "photos": "https://fastly.4sqi.net/img/general/original/397473_F69mfsr4-i4JB0-Gh1LdkG1T_veFYCEDXJ4VzfF__xE.jpg",
                            "review_score": "8.9",
                            "website": "http://www.divadlonacucky.cz",
                            "social_media": "cafenacucky",
                            "price": "1",
                            "menu": "",
                            "distance": 197
                        },
                        {
                            "id": 4784,
                            "city_id": 499,
                            "name": "Café La Fée",
                            "latitude": 49.594821,
                            "longitude": 17.252529,
                            "photos": "https://fastly.4sqi.net/img/general/original/36360199_0BsippdzcJXDc1hNvxpiEdE_6dX4W4Cutpx-6ffvijw.jpg",
                            "review_score": "8.4",
                            "website": "http://www.lafee.cz",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 131
                        },
                        {
                            "id": 4785,
                            "city_id": 499,
                            "name": "Jazz Tibet Club",
                            "latitude": 49.596138,
                            "longitude": 17.252556,
                            "photos": "https://fastly.4sqi.net/img/general/original/51932104_4DOOoqk2x9mY7OWhIXYZeNwjCa8U1Muv32D7AzfJgIg.jpg",
                            "review_score": "8.7",
                            "website": "http://www.jazzclub.olomouc.com",
                            "social_media": "",
                            "price": "",
                            "menu": "",
                            "distance": 245
                        },
                        {
                            "id": 4788,
                            "city_id": 499,
                            "name": "Green Bar",
                            "latitude": 49.594246,
                            "longitude": 17.252689,
                            "photos": "https://fastly.4sqi.net/img/general/original/81717323_b65PqDD6DAeMVRgxxEqsd9LhKjMbRDBYUXAieGMP_vE.jpg",
                            "review_score": "8.3",
                            "website": "http://www.greenbar.cz",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 105
                        },
                        {
                            "id": 4791,
                            "city_id": 499,
                            "name": "The Kathmandu Nepali Restaurant",
                            "latitude": 49.592124,
                            "longitude": 17.252124,
                            "photos": "https://fastly.4sqi.net/img/general/original/13032922_Rim_4n6s_dChrkrohOU4nP7QcKZy6gJBL69oNzyb0MY.jpg",
                            "review_score": "8.6",
                            "website": "http://www.nepalirestaurant.cz",
                            "social_media": "",
                            "price": "",
                            "menu": "",
                            "distance": 232
                        },
                        {
                            "id": 4793,
                            "city_id": 499,
                            "name": "Restaurant U Mořice",
                            "latitude": 49.594688,
                            "longitude": 17.251528,
                            "photos": "https://fastly.4sqi.net/img/general/original/46981225_TorzdIzZOYw9FjV4YmUdjS5ZSQpWsNvJWAP-vC2zdBc.jpg",
                            "review_score": "8.7",
                            "website": "https://www.umorice.cz",
                            "social_media": "",
                            "price": "",
                            "menu": "",
                            "distance": 91
                        },
                        {
                            "id": 4795,
                            "city_id": 499,
                            "name": "Jazz Fresh Café",
                            "latitude": 49.596075,
                            "longitude": 17.252206,
                            "photos": "https://fastly.4sqi.net/img/general/original/146341077_Bcb_WAlZJxOsj4hGcd-CoK-2E-ulT2DXXIRDszVBtM0.jpg",
                            "review_score": "8.8",
                            "website": "http://www.jazzfreshcafe.cz",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 236
                        },
                        {
                            "id": 4797,
                            "city_id": 499,
                            "name": "CoffeeCat - kočičí kavárna",
                            "latitude": 49.58816,
                            "longitude": 17.253497,
                            "photos": "https://fastly.4sqi.net/img/general/original/61459891_k034WWUxwxFupIZ7dMvQueZ7fjq0m9bsu2G6ky8EyFc.jpg",
                            "review_score": "8.7",
                            "website": "http://coffeecat.cz",
                            "social_media": "coffeecat_kocici_kavarna",
                            "price": "",
                            "menu": "",
                            "distance": 673
                        },
                        {
                            "id": 4801,
                            "city_id": 499,
                            "name": "Long Story Short Eatery & Bakery",
                            "latitude": 49.597306,
                            "longitude": 17.258705,
                            "photos": "https://fastly.4sqi.net/img/general/original/536525374_crv9_1uoLXhKK9lccTMpc2O0tgojPQeqF4tk07ZoOos.jpg",
                            "review_score": "8.8",
                            "website": "http://www.longstoryshort.cz",
                            "social_media": "",
                            "price": "",
                            "menu": "",
                            "distance": 661
                        }
                    ],
                    "schedules": [
                        {
                            "day": 1,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3186,
                                        "city_id": 499,
                                        "name": "VITALAND Olomouc - Dolní nám",
                                        "latitude": 49.592144,
                                        "longitude": 17.252826,
                                        "photos": "https://live.staticflickr.com/65535/53030230969_50d7a0a024_o.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "http://www.vitaland.cz",
                                        "hours_popular": "",
                                        "distance": "244",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3189,
                                        "city_id": 499,
                                        "name": "Olomouc 1/2 Maraton",
                                        "latitude": 49.593154,
                                        "longitude": 17.251007,
                                        "photos": "https://fastly.4sqi.net/img/general/original/17339105__mWFMKfFclRy4X3LMz-kX5i2egcfyc1armyxILBHhUE.jpg",
                                        "review_score": "0",
                                        "description": "finishing 19th in the 20 km walk. He began race walking in 2003 at the UKS Maraton Korzeniowski club in Bieruń, Poland. He is coached by his father, Grzegorz",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "100",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3193,
                                        "city_id": 499,
                                        "name": "Olomouc City Hall",
                                        "latitude": 49.593803,
                                        "longitude": 17.251139,
                                        "photos": "https://live.staticflickr.com/65535/52683629537_ff7e5c7b4f_o.jpg",
                                        "review_score": "0",
                                        "description": "Olomouc (UK: /ˈɒləmoʊts/, US: /ˈoʊloʊ-/, Czech: [ˈolomouts] (listen); German: Olmütz; Polish: Ołomuniec) is a city in the Czech Republic. It has about",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "28",
                                        "real_price": "",
                                        "start_time": "16:00",
                                        "end_time": "19:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 2,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3188,
                                        "city_id": 499,
                                        "name": "Astronomical clock (Orloj)",
                                        "latitude": 49.59413,
                                        "longitude": 17.251279,
                                        "photos": "https://fastly.4sqi.net/img/general/original/147452462__wLb3tllNlBVC_3qA6KFCN_l-GMGcFqShO_ijbMdWqY.jpg",
                                        "review_score": "7.4",
                                        "description": "The Prague astronomical clock or Prague Orloj (Czech: Pražský orloj [praʃskiː orloj]) is a medieval astronomical clock attached to the Old Town Hall in",
                                        "website": "https://cs.wikipedia.org/wiki/olomoucký_orloj",
                                        "hours_popular": "[{'close': '0800', 'day': 1, 'open': '0600'}, {'close': '1300', 'day': 1, 'open': '1100'}, {'close': '1800', 'day': 1, 'open': '1500'}, {'close': '0900', 'day': 2, 'open': '0600'}, {'close': '1400', 'day': 2, 'open': '1100'}, {'close': '1800', 'day': 2, 'open': '1600'}, {'close': '0800', 'day': 3, 'open': '0600'}, {'close': '1800', 'day': 3, 'open': '1000'}, {'close': '0800', 'day': 4, 'open': '0600'}, {'close': '1300', 'day': 4, 'open': '1100'}, {'close': '1900', 'day': 4, 'open': '1500'}, {'close': '0800', 'day': 5, 'open': '0700'}, {'close': '1700', 'day': 5, 'open': '1000'}, {'close': '2000', 'day': 5, 'open': '1900'}, {'close': '2100', 'day': 6, 'open': '0900'}, {'close': '2000', 'day': 7, 'open': '1000'}]",
                                        "distance": "12",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3170,
                                        "city_id": 499,
                                        "name": "Model centra Olomouce",
                                        "latitude": 49.594177,
                                        "longitude": 17.251217,
                                        "photos": "https://fastly.4sqi.net/img/general/original/30562967_l01tHDgc8uiMmRuq2K-H6fUsSNE5So_-VKy34InSYk0.jpg",
                                        "review_score": "0",
                                        "description": "Bronzový model centra Olomouce je v měřítku 1:400.",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "14",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3197,
                                        "city_id": 499,
                                        "name": "Holy Trinity Column in",
                                        "latitude": 49.593908,
                                        "longitude": 17.250473,
                                        "photos": "https://live.staticflickr.com/7427/27194858482_17a32facdb_k.jpg",
                                        "review_score": "0",
                                        "description": "of the Holy Trinity columns was usually simply to celebrate the church and the faith, though the plague motif could sometimes play its role in their erection",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "51",
                                        "real_price": "",
                                        "start_time": "16:00",
                                        "end_time": "19:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 3,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3187,
                                        "city_id": 499,
                                        "name": "The Holy Trinity Column (Sloup Nejsvětější Trojice)",
                                        "latitude": 49.593978,
                                        "longitude": 17.250587,
                                        "photos": "https://fastly.4sqi.net/img/general/original/147452462_nqkQ0OG4Z3QWHDQ01c8imkllwMFTwRYMTr6Jd5RwDbo.jpg",
                                        "review_score": "7.9",
                                        "description": "Marian and Holy Trinity columns Pestsäule, Vienna Jemelková, Simona; Zápalková, Helena; Ondrušková, Markéta (2008). Sloup Nejsvětější Trojice Olomouc (in",
                                        "website": "http://tourism.olomouc.eu",
                                        "hours_popular": "[{'close': '0800', 'day': 1, 'open': '0700'}, {'close': '1800', 'day': 1, 'open': '1200'}, {'close': '0800', 'day': 2, 'open': '0700'}, {'close': '2000', 'day': 2, 'open': '1100'}, {'close': '0700', 'day': 3, 'open': '0600'}, {'close': '2000', 'day': 3, 'open': '1300'}, {'close': '1900', 'day': 4, 'open': '1000'}, {'close': '0800', 'day': 5, 'open': '0700'}, {'close': '2000', 'day': 5, 'open': '1000'}, {'close': '2000', 'day': 6, 'open': '0900'}, {'close': '1900', 'day': 7, 'open': '1000'}]",
                                        "distance": "22",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3190,
                                        "city_id": 499,
                                        "name": "Olomouc Museum of Art (Muzeum umění Olomouc)",
                                        "latitude": 49.596191,
                                        "longitude": 17.256417,
                                        "photos": "https://fastly.4sqi.net/img/general/original/110499992_Sw88fCXVNtUXYN9gxVqFjWVgVn4FAQlLyKD4Yakh7JE.jpg",
                                        "review_score": "7.7",
                                        "description": "last flowers of the middle ages: from the gothic to the renaissance in Moravia and Silesia. Olomouc/Brno, Moravian Galery, Muzeum umění Olomouc ISBN 9788085227406",
                                        "website": "http://www.olmuart.cz",
                                        "hours_popular": "[{'close': '1800', 'day': 2, 'open': '1100'}, {'close': '1900', 'day': 3, 'open': '1100'}, {'close': '1100', 'day': 4, 'open': '1000'}, {'close': '1900', 'day': 4, 'open': '1500'}, {'close': '1200', 'day': 5, 'open': '1100'}, {'close': '2200', 'day': 5, 'open': '1400'}, {'close': '1800', 'day': 6, 'open': '1000'}, {'close': '1800', 'day': 7, 'open': '1000'}]",
                                        "distance": "442",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3179,
                                        "city_id": 499,
                                        "name": "Vlastivědné muzeum v Olomouci",
                                        "latitude": 49.59683,
                                        "longitude": 17.256707,
                                        "photos": "https://fastly.4sqi.net/img/general/original/58709209_0r8EqBhBgyCTaOu77zjgW9wmc6YDntrizyBURd7DLOY.jpg",
                                        "review_score": "6.2",
                                        "description": "",
                                        "website": "http://www.vmo.cz",
                                        "hours_popular": "[{'close': '1400', 'day': 1, 'open': '1300'}, {'close': '1200', 'day': 2, 'open': '1100'}, {'close': '1800', 'day': 2, 'open': '1600'}, {'close': '2000', 'day': 3, 'open': '0900'}, {'close': '2000', 'day': 4, 'open': '1000'}, {'close': '2100', 'day': 5, 'open': '0900'}, {'close': '1900', 'day': 6, 'open': '0900'}, {'close': '1700', 'day': 7, 'open': '1000'}]",
                                        "distance": "515",
                                        "real_price": "",
                                        "start_time": "16:00",
                                        "end_time": "19:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "city": "Karlovy Vary",
                    "description": "Return to Karlovy Vary for relaxation and to experience more of its charm.",
                    "restaurants": [
                        {
                            "id": 4772,
                            "city_id": 498,
                            "name": "Čajovna Universal",
                            "latitude": 50.230636,
                            "longitude": 12.869115,
                            "photos": "https://fastly.4sqi.net/img/general/original/523347386_3N6Mh2xZEnTBSw_E-ZWb4t-KatnF_Q1YLQtC7dyEuzo.jpg",
                            "review_score": "9.1",
                            "website": "",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 79
                        },
                        {
                            "id": 4773,
                            "city_id": 498,
                            "name": "Café KAVA",
                            "latitude": 50.228729,
                            "longitude": 12.870166,
                            "photos": "https://fastly.4sqi.net/img/general/original/34091958_gus1xxPGNhH7dK3z6qt6YrK3QxKtLRsmrJFEuzU9muE.jpg",
                            "review_score": "8.8",
                            "website": "http://cafekava.cz",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 198
                        },
                        {
                            "id": 4774,
                            "city_id": 498,
                            "name": "Republica Coffee",
                            "latitude": 50.23007,
                            "longitude": 12.869209,
                            "photos": "https://fastly.4sqi.net/img/general/original/7596817_mQ6wplEjCo0kEm_8YG2KqNntBmumCQb-uMF_0tRlfTo.jpg",
                            "review_score": "8.6",
                            "website": "",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 101
                        },
                        {
                            "id": 4775,
                            "city_id": 498,
                            "name": "Rad's Baguettes",
                            "latitude": 50.229449,
                            "longitude": 12.869258,
                            "photos": "https://fastly.4sqi.net/img/general/original/31506981_H7c9oG_WZLY3FGOdvbxzzVn_7-XS9ywCaolaEL3mnXw.jpg",
                            "review_score": "8.1",
                            "website": "",
                            "social_media": "",
                            "price": "1",
                            "menu": "",
                            "distance": 159
                        },
                        {
                            "id": 4776,
                            "city_id": 498,
                            "name": "Becherplatz",
                            "latitude": 50.230326,
                            "longitude": 12.867118,
                            "photos": "https://fastly.4sqi.net/img/general/original/43829714_Jx2UnwlqQulpu7taCFWM4NnL1Z2vqFxafsKtfPUioOY.jpg",
                            "review_score": "8.3",
                            "website": "http://www.becherplatz.cz",
                            "social_media": "",
                            "price": "2",
                            "menu": "",
                            "distance": 213
                        },
                        {
                            "id": 4777,
                            "city_id": 498,
                            "name": "Bagel Lounge",
                            "latitude": 50.230047,
                            "longitude": 12.868061,
                            "photos": "https://fastly.4sqi.net/img/general/original/83219471_tqK12JqxSqs47xIthMr8HGyCly3vNVmHPY-jSL3EN_U.jpg",
                            "review_score": "8.6",
                            "website": "http://bagellounge.cz",
                            "social_media": "bagellounge_kv",
                            "price": "1",
                            "menu": "",
                            "distance": 149
                        },
                        {
                            "id": 4778,
                            "city_id": 498,
                            "name": "Rozhledna Diana",
                            "latitude": 50.218738,
                            "longitude": 12.871653,
                            "photos": "https://fastly.4sqi.net/img/general/original/115042_NrTWzBXXNnmGXLGrJw5ZTYVy3YTuqdaozw4fbqGZw4A.jpg",
                            "review_score": "8.8",
                            "website": "http://www.dianakv.cz",
                            "social_media": "",
                            "price": "",
                            "menu": "",
                            "distance": 1314
                        },
                        {
                            "id": 4779,
                            "city_id": 498,
                            "name": "Tapas & Steak - Sabor Mediterraneo",
                            "latitude": 50.228661,
                            "longitude": 12.865968,
                            "photos": "https://fastly.4sqi.net/img/general/original/464003674_AkSNy_ap4TGbEbjLXbCxALZw-A8lMaAiDQ1C-qkmNHo.jpg",
                            "review_score": "8.5",
                            "website": "http://sabor.cz",
                            "social_media": "tapas_bar_kv",
                            "price": "2",
                            "menu": "",
                            "distance": 384
                        },
                        {
                            "id": 4780,
                            "city_id": 498,
                            "name": "Špunt & Knoflík",
                            "latitude": 50.229418,
                            "longitude": 12.866409,
                            "photos": "https://fastly.4sqi.net/img/general/original/71518136_MDcOXAuw29EqPVj97pCoxride8Ts-jTMgjULHdT7nJ8.jpg",
                            "review_score": "9.0",
                            "website": "http://www.spuntaknoflik.com",
                            "social_media": "spuntaknoflik",
                            "price": "",
                            "menu": "",
                            "distance": 277
                        },
                        {
                            "id": 4781,
                            "city_id": 498,
                            "name": "Lékárna by City Roasters",
                            "latitude": 50.230011,
                            "longitude": 12.868313,
                            "photos": "https://fastly.4sqi.net/img/general/original/64709762_d6piZyufjtHF5Otm6VEDaXQgyKX_LqS2wEVSO6SrMXY.jpg",
                            "review_score": "8.1",
                            "website": "http://www.cityroasters.eu",
                            "social_media": "lekarnacityroasters",
                            "price": "1",
                            "menu": "",
                            "distance": 154
                        }
                    ],
                    "schedules": [
                        {
                            "day": 1,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3180,
                                        "city_id": 498,
                                        "name": "Junák - český skaut, Přístav ORION Karlovy Vary, z.s.",
                                        "latitude": 50.21324,
                                        "longitude": 12.816045,
                                        "photos": "https://live.staticflickr.com/65535/53035304797_0338825d5f_o.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "http://www.pristavorion.cz",
                                        "hours_popular": "",
                                        "distance": "4304",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3177,
                                        "city_id": 498,
                                        "name": "Dětské Hřiště Varyáda",
                                        "latitude": 50.227551,
                                        "longitude": 12.842749,
                                        "photos": "https://fastly.4sqi.net/img/general/original/11204590_9ODm_gXg4w4fF2ugqxd6-TN31m1KQQYJjVYqIzwxrRM.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "1977",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3178,
                                        "city_id": 498,
                                        "name": "JK Karlovy Vary - St. Role",
                                        "latitude": 50.235002,
                                        "longitude": 12.826442,
                                        "photos": "https://live.staticflickr.com/65535/53035304797_0338825d5f_o.jpg",
                                        "review_score": "0",
                                        "description": "",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "3150",
                                        "real_price": "",
                                        "start_time": "16:00",
                                        "end_time": "19:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        },
                        {
                            "day": 2,
                            "attractions": [
                                {
                                    "attraction": {
                                        "id": 3175,
                                        "city_id": 498,
                                        "name": "SCHLECKER - KARLOVY VARY - Třída T. G. Masaryka 23",
                                        "latitude": 50.229686,
                                        "longitude": 12.870491,
                                        "photos": "https://fastly.4sqi.net/img/general/original/177841092_4PMsgaGxsmRDaqfjGeUxkbfL9WIMDUYgdlcK9tkmNCs.jpg",
                                        "review_score": "8.0",
                                        "description": "",
                                        "website": "http://www.schlecker.cz",
                                        "hours_popular": "[{'close': '2000', 'day': 1, 'open': '0900'}, {'close': '2000', 'day': 2, 'open': '1100'}, {'close': '1800', 'day': 3, 'open': '1000'}, {'close': '1800', 'day': 4, 'open': '1000'}, {'close': '2200', 'day': 5, 'open': '0900'}, {'close': '1900', 'day': 6, 'open': '1000'}, {'close': '1800', 'day': 7, 'open': '1000'}]",
                                        "distance": "121",
                                        "real_price": "",
                                        "start_time": "08:00",
                                        "end_time": "11:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3176,
                                        "city_id": 498,
                                        "name": "Karlovy Vary",
                                        "latitude": 50.231847,
                                        "longitude": 12.871721,
                                        "photos": "https://live.staticflickr.com/4852/46803547661_d3d093fa47_o.jpg",
                                        "review_score": "0",
                                        "description": "Karlovy Vary is a spa city in the Karlovy Vary Region of the Czech Republic. It has about 49,000 inhabitants. It lies at the confluence of the rivers Ohře and Teplá. It is named after Charles IV, Holy Roman Emperor and the King of Bohemia, who founded the city.",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "176",
                                        "real_price": "",
                                        "start_time": "11:00",
                                        "end_time": "14:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "id": 3181,
                                        "city_id": 498,
                                        "name": "Park - Interhotel Central",
                                        "latitude": 50.221751,
                                        "longitude": 12.882151,
                                        "photos": "https://fastly.4sqi.net/img/general/original/41809586__f38LD_e8wEzzo_IZm4E0HPEV_E9p6T8hihJHYmZy5U.jpg",
                                        "review_score": "0",
                                        "description": "square. The hotel opened as the Hotel Stadt Berlin, part of East Germany's Interhotel chain. It was a four-star hotel and mainly served for the accommodation",
                                        "website": "",
                                        "hours_popular": "",
                                        "distance": "1303",
                                        "real_price": "",
                                        "start_time": "16:00",
                                        "end_time": "19:00"
                                    }
                                },
                                {
                                    "attraction": {
                                        "name": "Lunch Break",
                                        "start_time": "14:00",
                                        "end_time": "16:00"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        "itinerary_description": "Experience the best of Czech Republic starting from the vibrant capital, Prague. Explore the historical sites, enjoy the nightlife, and immerse yourself in the culture. Visit the charming town of Cesky Krumlov and marvel at its medieval castle. Relax in the famous spa town of Karlovy Vary and rejuvenate in its healing waters. Discover the UNESCO World Heritage site of Kutna Hora with its unique attractions. Explore the vibrant city of Brno and its cultural offerings. Visit Olomouc, known for its beauty and historical landmarks. Finally, return to Karlovy Vary for more relaxation before concluding your journey in Czech Republic."
    },
    {
        "request_left": 9
    }
]