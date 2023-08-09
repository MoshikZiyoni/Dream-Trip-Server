# # attractions_without_description = Attraction.objects.filter(description__isnull=True) | Attraction.objects.filter(description='')
#     # for attraction in attractions_without_description:
#     #     # city=City.objects.get(attraction.city).first()
#     #     print(attraction.name,"----",attraction.city.city)  
#     # return 'ok'  

#     def excract_descrption(attractions_listt):
#         for attrac in attractions_listt:
#             name= (attrac['name'])
#             description=attrac['description']
#             print(description)
#             try:
#                 attrac=Attraction.objects.get(name=name)
#                 print (attrac.id,attrac.description)
#                 attrac.description=description
#                 attrac.save()
#                 print ('save success')
#                 attraction = Attraction.objects.get(pk=attrac.id)
#                 print(attraction.description) 
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
#                     attrac.description = description
#                     attrac.save()
#     excract_descrption(attractions_listt=[

# ])
   
#     return 'kk'
