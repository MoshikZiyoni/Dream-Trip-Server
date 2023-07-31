# def generate_opening_hours_summary(hours_popular):
#         days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#         if isinstance(hours_popular, str):
#             try:
#                 hours_popular = ast.literal_eval(hours_popular)
#             except (ValueError, SyntaxError):
#                 # Handle the case when the string cannot be safely evaluated as a list
#                 return "Invalid opening hours format."

#         # Now, `hours_popular` should be a list
#         summary = " ".join(f"{days_of_week[entry['day'] - 1]} {entry['open']}-{entry['close']}" for entry in hours_popular)
#         return summary
#     attractions = Attraction.objects.filter(hours_popular__isnull=False).exclude(hours_popular="")
#     for attraction in attractions:
        
#         hours_popular = attraction.hours_popular
#         # Check if the hours_popular is a list or a string that starts with any item in start_with_list
#         if (hours_popular.startswith('[')):
#             input_text = generate_opening_hours_summary(hours_popular)
#             # Load the BART summarization pipeline
#             print('OLD',hours_popular)
#             print ('NEW',input_text)
#             print ()
            
            
#     return 'ok'