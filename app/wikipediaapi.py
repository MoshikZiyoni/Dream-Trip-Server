import requests
import re
from bs4 import BeautifulSoup
from collections import Counter

def get_wikipedia_description(query):
    # Wikipedia API endpoint
    success = False

    endpoint = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
    try:
        # Send a GET request to the API endpoint
        response = requests.get(endpoint,timeout=5)
        data = response.json()
        # Extract the description from the API response
        description = data["extract"]
        try:
            response = requests.get(f"https://en.wikipedia.org/wiki/{query}",timeout=5)
            # Create a BeautifulSoup object from the response text
            soup = BeautifulSoup(response.text, "html.parser")
            # Find the link element that has the text "Official website"
            link = soup.find("a", string="Official website")
            # If there is such a link, get its href attribute value
            if link:
                url = link["href"]

            if description:
                success = True
                print ('successsuccesssuccesssuccesssuccesssuccess',url)
                return description,url
        except:
            pass
        content_urls = data.get('content_urls', {})
        mobile_url = content_urls.get('mobile', {}).get('page', '')
        if description:
            success = True
            return description,mobile_url
    except:
        # Handle request errors
        pass
        # print ('no des')

    if not success:
        endpoint = "https://en.wikipedia.org/w/api.php"
        # Set the parameters for the API request
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": query,
            "srprop": "snippet",
            "srlimit": 1,
        }
        response = requests.get(endpoint, params=params,timeout=5)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        results = data["query"]["search"]
        try:
          for result in results:
            title = result["title"]
            snippet = result["snippet"]
            page_id=result['pageid']
            soup = BeautifulSoup(snippet, "html.parser")
            snippet_text = soup.get_text()
            endpoint = "https://en.wikipedia.org/w/api.php"
            params = {
                "action": "query",
                "format": "json",
                "prop": "extlinks",
                "pageids": page_id,}
            response = requests.get(endpoint, params=params,timeout=5)
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()
            
            # Extract the extlinks for the attraction
            page_id = list(data["query"]["pages"].keys())[0]
            extlinks = data["query"]["pages"][page_id].get("extlinks", [])
            # Extract the URLs and count their occurrences by domain
            urls = [link["*"] for link in extlinks]
            domain_counts = Counter([url.split("//")[1].split("/")[0] for url in urls])

            # Find the most common domain
            most_common_domain = domain_counts.most_common(1)[0][0]

            # Filter the URLs based on the most common domain
            filtered_urls = [url for url in urls if most_common_domain in url]

            # Return the shortest URL among the filtered URLs
            shortest_url = min(filtered_urls, key=len)
            
            return (snippet_text,shortest_url)
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
      description,url=(description)
      return(description,url)
    else:
        return({'description':'No description'})
