# from django.db.models import Count
# from django.db import transaction

# attractions = Attraction.objects.values('name').annotate(name_count=Count('name')).filter(name_count__gt=1)

# for attraction in attractions:
#     name = attraction['name']
#     duplicates = Attraction.objects.filter(name=name).order_by('id')

#     with transaction.atomic():
#         # Keep the first instance
#         first_instance = duplicates.first()
        
#         # Delete the duplicates
#         duplicates.exclude(id=first_instance.id).delete()
# # return 'ok'