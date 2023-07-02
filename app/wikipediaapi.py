import requests
import threading
import re
from bs4 import BeautifulSoup

def get_wikipedia_description(query):
    # Wikipedia API endpoint
    success = False

    endpoint = "https://en.wikipedia.org/api/rest_v1/page/summary/{}".format(query)
    try:
        # Send a GET request to the API endpoint
        response = requests.get(endpoint)
        data = response.json()
        # Extract the description from the API response
        # print (data)
        description = data["extract"]
        
        if description:
            success = True
            return description
    except:
        # Handle request errors
        pass
        # print ('no des')

    if not success:
        # print ('no')
        endpoint = "https://en.wikipedia.org/w/api.php"
        # Set the parameters for the API request
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": query,
            "srprop": "snippet|url",
            "srlimit": 1,
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        results = data["query"]["search"]
        try:
          for result in results:
            title = result["title"]
            snippet = result["snippet"]
            soup = BeautifulSoup(snippet, "html.parser")
            snippet_text = soup.get_text()
            # url = "https://en.wikipedia.org/wiki/" + title.replace(" ", "_")
            # print("URL:", url)
            # print("Title:", title)
            # print("Snippet:", snippet_text)
            # print("------------------")
            return (snippet_text)
        except:
            pass
            # print('No description')

        return None

        

def process_query(query):
    # Remove Hebrew strings and parentheses from the attraction name
    cleaned_query = re.sub(r"[\u0590-\u05FF()]+", "", query)
    
    # Call the function to retrieve the description
    description = get_wikipedia_description(cleaned_query)
    if description:
      return(description)
    else:
        return({'description':''})
