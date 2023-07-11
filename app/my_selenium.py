import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def perform_search(query):
    query = query.replace(' ', '+')
    
    chrome_options = Options()
    chrome_options.add_argument("--lang=en-ca")

    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        url = f"https://www.google.com/search?q={query}"
        driver.get(url)
        
        time.sleep(3)
        
        span_elements=driver.find_element(By.CSS_SELECTOR,'span.z3HNkc').text
        # span_elements = driver.find_element(By.CSS_SELECTOR, 'span.Aq14fc').text
        return(span_elements)
    except:
        print ('not with google')
    try:
        query=f"foursquare {query}"
        
        url = f"https://www.google.com/search?q={query}"
        driver.get(url)
        driver.find_element(By.CSS_SELECTOR,'div.yuRUbf:first-child').click()
        time.sleep(2)
        rating=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/span/span').text
        return(rating)
        

    except Exception as e:
        print ('not good',e)
        return None
    