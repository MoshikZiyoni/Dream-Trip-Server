def get_next_dinner_restaurant(dinner_list, rest_of_restaurants, breakfast_restaurant, lunch_restaurant):
    next_dinner = None

    while next_dinner is None and (dinner_list or rest_of_restaurants):
        if dinner_list:
            candidate_dinner = dinner_list[0]  # Get the first restaurant from the dinner list
            if (
                candidate_dinner != breakfast_restaurant
                and candidate_dinner != lunch_restaurant
            ):
                next_dinner = dinner_list.pop(0)  # Choose it if it meets the criteria
            else:
                dinner_list.pop(0)  # Remove the restaurant that doesn't meet the criteria
        else:
            next_dinner = rest_of_restaurants.pop(0)  # Choose from rest_of_restaurants

    return next_dinner



def get_next_lunch_restaurant(breakfast_list, rest_of_restaurants, breakfast_restaurant):
    next_lunch = None

    while next_lunch is None and (breakfast_list or rest_of_restaurants):
        if breakfast_list:
            candidate_lunch = breakfast_list[0]  # Get the first restaurant from the breakfast list
            if candidate_lunch != breakfast_restaurant:
                next_lunch = breakfast_list.pop(0)  # Choose it if it's not the same as breakfast
            else:
                breakfast_list.pop(0)  # Remove the duplicate from breakfast_list
        else:
            next_lunch = rest_of_restaurants.pop(0)  # Choose from rest_of_restaurants

    return next_lunch


def get_next_breakfast_restaurant(breakfast_list, rest_of_restaurants, dinner_restaurant):
    next_breakfast = None

    while next_breakfast is None and (breakfast_list or rest_of_restaurants):
        if breakfast_list:
            candidate_breakfast = breakfast_list[0]  # Get the first restaurant from the breakfast list
            if (
                candidate_breakfast != dinner_restaurant
                and all(candidate_breakfast != restaurant for restaurant in breakfast_list)
            ):
                next_breakfast = breakfast_list.pop(0)  # Choose it if it meets the criteria
            else:
                breakfast_list.pop(0)  # Remove the restaurant that doesn't meet the criteria
        else:
            next_breakfast = rest_of_restaurants.pop(0)  # Choose from rest_of_restaurants

    return next_breakfast