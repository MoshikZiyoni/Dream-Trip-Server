
import bs4
import requests
import re
def find_official_website(attraction):
  cleaned_query = re.sub(r"[\u0590-\u05FF()]+", "", attraction)
  # Send a GET request to the web page that contains the attraction information
  response = requests.get(f"https://en.wikipedia.org/wiki/{cleaned_query}")
  # Create a BeautifulSoup object from the response text
  soup = bs4.BeautifulSoup(response.text, "html.parser")
  # Find the link element that has the text "Official website"
  link = soup.find("a", string="Official website")
  # If there is such a link, get its href attribute value
  if link:
    url = link["href"]
    return {'website':url}
  # Otherwise, return None
  else:
    return {'website':''}
