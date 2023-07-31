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

# [{"city":"Vienna","name":"Steirereck","latitude":48.22417,"longitude":16.34306,"photos":[],"review_score":4.8,"website":"https://www.steirereck.at","social\_media":"","price":5,"menu":"Modern Austrian fine dining","distance":""},

# {"city":"Vienna","name":"Plachutta","latitude":48.20056,"longitude":16.3725,"photos":[],"review_score":4.6,"website":"https://www.plachutta.at","social\_media":"","price":4,"menu":"Traditional Viennese cuisine","distance":""},

# {"city":"Vienna","name":"Fabios","latitude":48.20667,"longitude":16.358333,"photos":[],"review_score":4.5,"website":"http://fabios.at","social\_media":"","price":2,"menu":"Pizza, pasta","distance":""},

# {"city":"Vienna","name":"Griechenbeisl","latitude":48.20833,"longitude":16.368333,"photos":[],"review_score":4.4,"website":"https://www.griechenbeisl.at","social\_media":"","price":3,"menu":"Viennese cuisine in historic setting","distance":""},

# {"city":"Vienna","name":"Meinl's Restaurant","latitude":48.2075,"longitude":16.358,"photos":[],"review_score":4.3,"website":"https://www.meinlamgraben.at","social\_media":"","price":3,"menu":"International cuisine","distance":""},

# {"city":"Vienna","name":"Figlmüller","latitude":48.20833,"longitude":16.372222,"photos":[],"review_score":4.5,"website":"https://www.figlmueller.at","social\_media":"","price":3,"menu":"Schnitzel, Austrian cuisine","distance":""},

# {"city":"Vienna","name":"Restaurant Konstantin Filippou","latitude":48.19611,"longitude":16.3225,"photos":[],"review_score":4.8,"website":"http://www.konstantinfilippou.com","social\_media":"","price":4,"menu":"Inventive modern cuisine","distance":""},

# {"city":"Vienna","name":"ef16","latitude":48.21417,"longitude":16.36556,"photos":[],"review_score":4.6,"website":"https://www.ef16.net","social\_media":"","price":3,"menu":"Seasonal Austrian cuisine","distance":""},

# {"city":"Vienna","name":"Das LOFT","latitude":48.21472,"longitude":16.34611,"photos":[],"review_score":4.3,"website":"http://www.dasloftwien.at","social\_media":"","price":3,"menu":"International cuisine with view","distance":""},

# {"city":"Vienna","name":"Le Burger","latitude":48.2075,"longitude":16.358056,"photos":[],"review_score":4.4,"website":"http://www.leburger.at","social\_media":"","price":2,"menu":"Gourmet burgers","distance":""},

# {"city":"Vienna","name":"Motto am Fluss","latitude":48.233333,"longitude":16.433333,"photos":[],"review_score":4.2,"website":"http://www.motto.at","social\_media":"","price":3,"menu":"Pan-Asian cuisine with river view","distance":""},

# {"city":"Vienna","name":"Wrenkh","latitude":48.20472,"longitude":16.38194,"photos":[],"review_score":4.6,"website":"https://www.wrenkh-wien.at","social\_media":"","price":3,"menu":"Austrian cuisine in romantic setting","distance":""},

# {"city":"Vienna","name":"Tian Restaurant","latitude":48.20833,"longitude":16.372222,"photos":[],"review_score":4.5,"website":"https://www.tian-restaurant.com","social\_media":"","price":4,"menu":"Vegetarian fine dining","distance":""},

# {"city":"Vienna","name":"Restaurant Vestibül","latitude":48.21028,"longitude":16.3625,"photos":[],"review_score":4.3,"website":"https://www.vestibuel.at","social\_media":"","price":4,"menu":"Upscale Austrian cuisine","distance":""},

# {"city":"Vienna","name":"Glacis Beisl","latitude":48.201389,"longitude":16.358333,"photos":[],"review_score":4.3,"website":"https://www.glacisbeisl.at","social\_media":"","price":2,"menu":"Austrian comfort food","distance":""},

# {"city":"Vienna","name":"Flein","latitude":48.23194,"longitude":16.35389,"photos":[],"review_score":4.2,"website":"http://www.flein.at","social\_media":"","price":2,"menu":"Viennese wine tavern","distance":""},

# {"city":"Vienna","name":"MUMOK Restaurant","latitude":48.19944,"longitude":16.37417,"photos":[],"review_score":4.1,"website":"https://restaurantmumok.com","social\_media":"","price":3,"menu":"International cuisine in modern setting","distance":""},

# {"city":"Vienna","name":"Umar","latitude":48.20556,"longitude":16.373,"photos":[],"review_score":4.5,"website":"https://www.umarfish.at","social\_media":"","price":3,"menu":"High-end seafood","distance":""},

# {"city":"Vienna","name":"Pizza Mari'",latitude":48.21417,"longitude":16.34778,"photos":[],"review_score":4.3,"website":"http://www.pizzamari.at","social\_media":"","price":2,"menu":"Pizza, Italian dishes","distance":""},

# {"city":"Vienna","name":"Yohm","latitude":48.20833,"longitude":16.372222,"photos":[],"review_score":4.1,"website":"https://yohm.at","social\_media":"","price":3,"menu":"Japanese cuisine, sushi","distance":""}]