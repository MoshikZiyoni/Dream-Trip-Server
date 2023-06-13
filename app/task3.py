# import requests
# from bs4 import BeautifulSoup
# from lxml import etree

# def google_search(query):
#     # Format the query for the Google search URL
#     query = query.replace(' ', '+')
#     url = f"https://www.google.com/search?q={query}"

#     # Send a GET request to the Google search URL
#     response = requests.get(url)

#     soup = BeautifulSoup(response.text, 'html.parser')
#     # Find all div elements
#     div_elements = soup.find_all('div')
#     for div in div_elements:
#         span_elements1_for_description = div.find_all('span', {'dir': 'ltr'})
#         longest_line = ""
#         longest_length = 0

#         # Iterate over the span elements
#         for span in span_elements1_for_description:
#             line = span.text.strip()
#             line_length = len(line)

#             # Check if the current line has a larger length
#             if line_length > longest_length:
#                 longest_line = line
#                 longest_length = line_length

        
#         span_elements = div.find_all('span', {'aria-hidden': 'true', 'class': 'oqSTJd'})
#         # print(span_elements)
#         for span in span_elements:
#             # print(span)
#             score_text = span.text.strip()
#             review_score = score_text.split('/')[0] 
#             print (review_score)
#             # longest_line = longest_line.replace('\xa0', '...')
#             # if review_score is None:
#             #     review_score = ""
#             # if longest_line is None:
#             #     longest_line = ""
#             return {"review_score":review_score}
#             # return {"review_score":review_score,"description":longest_line}


#     return {"review_score": ""}

# google_search(query='Diptyque BHV Marais,paris,france')

# # queries = [
# # "Piazza della Repubblica, Rome, Italy",
# # "Terme di Diocleziano, Rome, Italy",
# # "Palazzo delle Esposizioni, Rome, Italy",
# # "Palazzo Barberini, Rome, Italy",
# # "Piazza del Quirinale, Rome, Italy",
# # "Trevi Fountain (Fontana di Trevi), Rome, Italy",
# # "Drink Kong, Rome, Italy",
# # "Trajan's Markets - Museum of Imperial Forums (Mercati di Traiano - Museo dei Fori Imperiali), Rome, Italy",
# # "Trajan's Column (Colonna Traiana), Rome, Italy",
# # "Spanish Steps (Scalinata di Trinità dei Monti), Rome, Italy,"

# # ]

# # Iterate over the list of queries
# # for query in queries:
# #     print(google_search(query))
# #     print()

# # soup = BeautifulSoup(response.content, "html.parser")
# #     # Find all the elements that contain the attraction links and ratings
# #     attractions = soup.find_all("div", class_="result-title")
# #     # Loop through each attraction element
# #     for attraction in attractions:
# #         # Get the name of the attraction from the text content
# #         name = attraction.text.strip()