# from django.db.models import Count
# from django.db import transaction

# attractions = Attraction.objects.values('name').annotate(name_count=Count('name')).filter(name_count__gt=1)


    # for attraction in attractions:
    #     name = attraction['name']
    #     duplicates = Attraction.objects.filter(name=name).order_by('id')

    #     city_ids = set(duplicates.values_list('city_id', flat=True))

    #     with transaction.atomic():
    #         for city_id in city_ids:
    #             city_duplicates = duplicates.filter(city_id=city_id)

    #             # Print the duplicates in the same city
    #             delete_list = city_duplicates.exclude(id=city_duplicates.first().id)
    #             for duplicate in delete_list:
    #                 print(f"Deleting duplicate: {duplicate.name}, City ID: {duplicate.city_id}")

    #             # Delete all duplicates except the first one per city (on commit)
    #             delete_list.delete()
# # return 'ok'




# from django.db.models import Count
# from django.db import transaction
# def delete_duplicate_attractions():
#     attractions = Restaurant.objects.values('name').annotate(name_count=Count('name')).filter(name_count__gt=1)

    # for attraction in attractions:
    #     name = attraction['name']
    #     duplicates = Restaurant.objects.filter(name=name).order_by('id')

    #     city_ids = set(duplicates.values_list('city_id', flat=True))

    #     with transaction.atomic():
    #         for city_id in city_ids:
    #             city_duplicates = duplicates.filter(city_id=city_id)

    #             # Print the duplicates in the same city
    #             delete_list = city_duplicates.exclude(id=city_duplicates.first().id)
    #             for duplicate in delete_list:
    #                 print(f"Deleting duplicate: {duplicate.name}, City ID: {duplicate.city_id}")

    #             # Delete all duplicates except the first one per city (on commit)
    #             delete_list.delete()
# delete_duplicate_attractions()

# return 'ok'