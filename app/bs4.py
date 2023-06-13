import requests
from bs4 import BeautifulSoup

def google_search(query):
    # Format the query for the Google search URL
    query = query.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}"

    # Send a GET request to the Google search URL
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all div elements
    div_elements = soup.find_all('div')
    for div in div_elements: 
        span_elements = div.find_all('span', {'aria-hidden': 'true', 'class': 'oqSTJd'})
        for span in span_elements:
            # print(span)
            score_text = span.text.strip()
            review_score = score_text.split('/')[0] 
            print (review_score)
            if review_score is None:
                review_score = ""
            return {"review_score":review_score}


    return {"review_score": ""}
