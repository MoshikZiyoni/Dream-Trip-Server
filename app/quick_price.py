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

