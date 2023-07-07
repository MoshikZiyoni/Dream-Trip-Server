
import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from collections import Counter
import time
import re

def google_search(query):
    print ('start google search')
    query = query.replace(' ', '+')
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
        'Accept-Language': 'en-US,en;q=0.5'
    }
    # Send a GET request to the Google search URL
    response = requests.get(f"https://www.google.com/search?q={query}&lr=lang_en", headers=headers)     
    soup = BeautifulSoup(response.text, 'html.parser')

    div_elements = soup.find_all('div')
    
    for div in div_elements:      
        span_elements = div.find_all('span', {'aria-hidden': 'true', 'class': 'oqSTJd'})
        for span in span_elements:
            score_text = span.text.strip()
            review_score = score_text.split('/')[0] 
            if review_score is None:
                print ('ots Noneeeeeeeeeeeeeeee')
                review_score = ""
            
            
            print ({"review_score":review_score})

            return {"review_score":review_score}

    
    return {"review_score": ""}
 
            