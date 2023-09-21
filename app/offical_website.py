
# import bs4
# import requests
# import re
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

# def find_official_website(attraction):
#   try:
#     cleaned_query = re.sub(r"[\u0590-\u05FF()]+", "", attraction)
#     # Send a GET request to the web page that contains the attraction information
#     response = requests.get(f"https://en.wikipedia.org/wiki/{cleaned_query}")
#     # Create a BeautifulSoup object from the response text
#     soup = bs4.BeautifulSoup(response.text, "html.parser")
#     # Find the link element that has the text "Official website"
#     link = soup.find("a", string="Official website")
#     # If there is such a link, get its href attribute value
#     if link:
#       url = link["href"]
#       return {'website':url}
#     # Otherwise, return None
#     else:
#       return {'website':''}
#   except:
#     print ('not succuess with wikipedia')
#   try:
#     chrome_options = Options()
#     chrome_options.add_argument("--lang=en-ca")

#     # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
    
#     driver = webdriver.Chrome(options=chrome_options)
#     query=f"{cleaned_query},Offical website"
#     url = f"https://www.google.com/search?q={query}"
#     driver.get(url)
    
#     time.sleep(50)
    
#     # span_elements=driver.find_element(By.CSS_SELECTOR,'span.z3HNkc').text
#   except:
#     print ('not success with google')

# print(find_official_website('eiffel tower'))