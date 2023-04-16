from django.test import TestCase
import json
import re

our_answer = {
   "country":"Brazil",
   "cities":[
      {
         "city":"Rio de Janeiro",
         "description":"Experience Brazil's vibrant culture in one of its most iconic cities, known for its spectacular beaches, lively nightlife, and famous landmarks such as Sugarloaf Mountain and Christ the Redeemer statue.",
         "attractions":[
            {
               "name":"Sugarloaf Mountain",
               "description":"A granite peak rising above Rio de Janeiro, featuring stunning views of Guanabara Bay and the city skyline."
            },
            {
               "name":"Christ the Redeemer",
               "description":"A world-famous Art Deco statue of Jesus Christ, located atop Corcovado Mountain and offering panoramic views of the city below."
            },
            {
               "name":"Copacabana Beach",
               "description":"A vibrant beachfront neighborhood, featuring a stunning stretch of white sand beach with plenty of bars, restaurants, and shops."
            }
         ],
         "travelDay":1
      },
      {
         "city":"Sao Paulo",
         "description":"Explore the cultural and financial capital of Brazil, known for its museums, galleries, and lively music scene.",
         "attractions":[
            {
               "name":"Museu de Arte de Sao Paulo",
               "description":"One of the most important art museums in the southern hemisphere, featuring works by renowned artists such as Van Gogh, Picasso, and Rembrandt."
            },
            {
               "name":"Sao Paulo Cathedral",
               "description":"A neo-Gothic cathedral in the heart of the city, featuring stunning stained glass windows and a soaring interior."
            },
            {
               "name":"Ibirapuera Park",
               "description":"A sprawling park in the heart of the city, featuring walking trails, bike paths, and several museums and cultural attractions."
            }
         ],
         "travelDay":4
      },
      {
         "city":"Salvador",
         "description":"Experience the rich Afro-Brazilian culture of Salvador, known for its vibrant music and arts scene, historic landmarks, and delicious cuisine.",
         "attractions":[
            {
               "name":"Pelourinho",
               "description":"A UNESCO World Heritage Site, featuring colorful architecture, cobblestone streets, and lively music and dance performances."
            },
            {
               "name":"Igreja de Sao Francisco",
               "description":"A Baroque-style church with stunning ornate interiors, including gold-covered walls and intricate woodcarvings."
            },
            {
               "name":"Mercado Modelo",
               "description":"A lively and colorful marketplace selling everything from local handicrafts to fresh seafood and spices."
            }
         ],
         "travelDay":7
      }
   ]
}


# our_answer_dict=json.loads(our_answer)
cities=our_answer['cities']
country=our_answer['country']

city_dict={}
for city in cities:
    city_dict[city['city']]=city['description']
    print (city_dict)
# attractions=our_answer['attractions']


