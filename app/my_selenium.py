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
        
        if len(span_elements)<3:
            return(span_elements)
        else:
            pass
    except:
        print ('not with google')
    try:
        new_query=f"foursquare {query}"
        
        url = f"https://www.google.com/search?q={new_query}"
        driver.get(url)
        driver.find_element(By.CSS_SELECTOR,'div.yuRUbf:first-child').click()
        time.sleep(2)
        rating=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/span/span').text
        if len(rating)<3:
            return(rating)
        else:
            pass
    except :
        print ('not rating in foursquare')
    try:
        search_url = f'https://www.tripadvisor.com/Search?q={query}'
        driver.get(search_url)
        time.sleep(3)
        element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]')

        first_tab = driver.current_window_handle

        # Find the element to click
        element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]')

        # Perform the click action
        element.click()

        # Switch to the new tab
        for window_handle in driver.window_handles:
            if window_handle != first_tab:
                driver.switch_to.window(window_handle)
                break
        driver.switch_to.window(first_tab)
        driver.close()

        # Switch back to the new tab
        driver.switch_to.window(driver.window_handles[-1])
        # Close the first tab
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        rating=driver.find_element(By.XPATH,'/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[9]/div/div/div/section/section/div[1]/div/div[3]/div[1]/div/div[1]/div[1]').text
        if len(rating)<3:
            return(rating)
        else:
            pass
    except:
        print ('not rating in trip advisor')
    return None
    


