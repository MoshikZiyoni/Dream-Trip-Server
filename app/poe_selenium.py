import threading
import random
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from rest_framework.decorators import api_view
from app.models import City
from django.http import JsonResponse
from webdriver_manager.chrome import ChromeDriverManager

random_time = random.uniform(5, 20)

@api_view(['POST'])
def poe(request):
    print('satrt')
    try:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"user-agent={user_agent}")
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Use ChromeDriverManager to install ChromeDriver if not present
        ChromeDriverManager().install()
        
        # Create Chrome WebDriver instance
        driver = webdriver.Chrome(options=chrome_options)
        page_title = driver.title
        print(page_title)

        # Close the WebDriver
        driver.quit()
        
        return JsonResponse({'Check Selenium': page_title}, safe=False)  
    except Exception as e:
        print('not good',e)
    
    # try:
    #     chrome_options = webdriver.ChromeOptions()

    #     driver = webdriver.Chrome( options=chrome_options)
        
    #         # Set up Chrome options
    #     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
        
    #     chrome_options.add_argument(f"user-agent={user_agent}")
    #     chrome_options.add_argument("--headless")  # Run in headless mode
    #     chrome_options.add_argument("--no-sandbox")
    #     chrome_options.add_argument("--disable-dev-shm-usage")

        

    #     # Navigate to the desired URL
    #     driver.get('https://poe.com/Claude-instant')
    #     time.sleep(5)
        
    #     # Print the page title
    #     page_title = driver.title
    #     print(page_title)

    #     # Close the WebDriver
    #     driver.quit()
        
    #     return JsonResponse({'Check Selenium': page_title}, safe=False)    
    # except Exception as e:
    #     return JsonResponse({'error': str(e)}, status=500)
    driver.maximize_window()
    time.sleep(random_time)
    driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/a').click()
    time.sleep(random_time)
    driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/form/input').send_keys('amnonking123@gmail.com',Keys.ENTER)
    time.sleep(100)
    count=3
    cities=[ 'Cape Town', 'Poznan', 'Christchurch','Las Vegas', 'New York city', 'Malmo', 'Beijing', 'Zurich', 'Milan','Sucre', 'Boston', 'Tilburg', 'Amadora', 'Stockholm', 'Pucon', 'Angkor Wat', 'Pacific Harbour', 'Mendoza', 'Lake Atitlán']

    for_question1='"city": "return the exactly city i provided","name": "","latitude": ,"longitude": ,"review_score": ,"description": "","website":"","hours": "","telephone:"","tips":"provide me 3 tips","distance": "","formatted address":"","real_price": "give me price in USD $ (avrage price) if its for free return Free"'
    
    for city1 in cities:
        question_restaurnt=f'proivde me exactly 15 the best restaurants in {city1} with this details ("city": "","name": "","latitude": ,"longitude": ,"review_score":  ,"website":"can be social media also","category":"breakfast ,lunch ,dinner","hours": "","telephone:"","formatted address":"","price_range": "from 1 to 5-1cheap, 5 most expensive","tips":"provide me 3 tips as a list", do your best to find me the data you have. return me with double quetos and also as a dictionary like that "city": "return the exactly city I provided","name": "","latitude": ,"longitude": ,"review_score": ,"website":"can be social media also","category":"breakfast ,lunch ,dinner","hours": "","telephone:"","formatted address":"","price_range": "from 1 to 5-1cheap, 5 most expensive","tips":"provide me 3 tips as a list" ,do it fast and do not forget to return exactly 15 restaurants and the price_range return only in numbers'
        # question=f'proivde me exactly 15 attractions in {city1} with this details ("city": "","name": "","latitude": ,"longitude": ,"review_score": ,"description": "","website":"","hours": "","telephone:"","tips":"provide me 3 tips","distance": "","formatted address":"","real_price": "" do your best to find me the best prices you have. return me with double quetos and also as a dictionary like that {for_question1},do it fast and do not forget to return exactly 15 attractions'
        time.sleep(random_time)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/footer/div/div/div[1]/textarea').send_keys(question_restaurnt, Keys.ENTER)
        time.sleep(3)
        random_time_interval = random.uniform(190, 200)
        time.sleep(random_time_interval)
        attractions=driver.find_element(By.XPATH,f"/html/body/div[1]/div[1]/main/div/div/div/div[2]/div[{count}]/div[2]/div[2]").text
        with open('attractions1.txt', 'a', encoding='utf-8') as f:
            f.write(attractions + '\n')
        count+=1
        print (count)


# def poe1():
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"

#     # Set up the Chrome WebDriver with User-Agent and headless mode
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument(f"user-agent={user_agent}")
#     # chrome_options.add_argument("--headless")  # Run in headless mode

#     # Create a Chrome WebDriver instance
#     # service_path = "C:/Users/moshi/Downloads/chromedriver.exe"
#     # service = Service(service_path)
#     driver = webdriver.Chrome( options=chrome_options)
#     # driver.get('https://poe.com/Claude-2-100k')
#     # driver.get('https://poe.com/Claude-instant-100k')
#     driver.get('https://poe.com/Claude-instant')

#     driver.maximize_window()
#     time.sleep(random_time)
#     driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/a').click()
#     time.sleep(random_time)
#     driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/form/input').send_keys('amnontheking1234@gmail.com',Keys.ENTER)
#     time.sleep(100)
#     cities=[  'Helsinki','Konya', 'Queenstown', 'Espoo', 'Vlore', 'Amalfi', 'Uyuni', 'Hamburg',  'Montego Bay','Joao Pessoa', 'Liverpool', 'Bruges', 'San Sebastian', 'Nantes', 'Klagenfurt', 'Rotterdam', 'Szczecin', 'Nagoya', 'Belize City']
#     count=3
#     # for_question='"city": "return the exactly city i provided","name": "","latitude": ,"longitude": ,"review_score": ,"description": "","website":"","hours": "","telephone:"","tips":"provide me 3 tips","distance": "","formatted address":"","real_price": "give me price in USD (avrage price) if its for free return Free"'
#     for city in cities:
#         question_restaurnt=f'proivde me exactly 15 the best restaurants in {city} with this details ("city": "","name": "","latitude": ,"longitude": ,"review_score":  ,"website":"can be social media also","category":"breakfast ,lunch ,dinner","hours": "","telephone:"","formatted address":"","price_range": "from 1 to 5-1cheap, 5 most expensive","tips":"provide me 3 tips as a list", do your best to find me the data you have. return me with double quetos and also as a dictionary like that "city": "return the exactly city I provided","name": "","latitude": ,"longitude": ,"review_score": ,"website":"can be social media also","category":"breakfast ,lunch ,dinner","hours": "","telephone:"","formatted address":"","price_range": "from 1 to 5-1cheap, 5 most expensive","tips":"provide me 3 tips as a list" ,do it fast and do not forget to return exactly 15 restaurants and the price_range return only in numbers'
#         # question=f'proivde me exactly 15 attractions in {city} with this details ("city": "","name": "","latitude": ,"longitude": ,"review_score": ,"description": "","website":"","hours": "","telephone:"","tips":"provide me 3 tips","distance": "","formatted address":"","real_price": "" do your best to find me the best prices you have. return me with double quetos and also as a dictionary like that {for_question},do it fast and do not forget to return exactly 15 attractions'
#         time.sleep(random_time)
#         driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/footer/div/div/div[1]/textarea').send_keys(question_restaurnt, Keys.ENTER)
#         time.sleep(3)
#         random_time_interval = random.uniform(190, 200)
#         time.sleep(random_time_interval)
#         attractions=driver.find_element(By.XPATH,f"/html/body/div[1]/div[1]/main/div/div/div/div[2]/div[{count}]/div[2]/div[2]").text
#         with open('attractions1.txt', 'a', encoding='utf-8') as f:
#             f.write(attractions + '\n')
#         count+=1
#         print (count)


# def poe2():
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"

#     # Set up the Chrome WebDriver with User-Agent and headless mode
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument(f"user-agent={user_agent}")
#     # chrome_options.add_argument("--headless")  # Run in headless mode

#     # Create a Chrome WebDriver instance
#     # service_path = "C:/Users/moshi/Downloads/chromedriver.exe"
#     # service = Service(service_path)
#     driver = webdriver.Chrome( options=chrome_options)
#     # driver.get('https://poe.com/Claude-2-100k')
#     # driver.get('https://poe.com/Claude-instant-100k')
#     driver.get('https://poe.com/Claude-instant')
#     driver.maximize_window()
#     time.sleep(random_time)
#     driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/a').click()
#     time.sleep(random_time)
#     driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/form/input').send_keys('amnontheking12345@gmail.com',Keys.ENTER)
#     time.sleep(100)
    
#     count=3
#     cities=[ 'Miskolc', 'Cusco', 'Bath','Krabi', 'Antigua', 'Frankfurt', 'Encamp', 'Yekaterinburg', 'Kampot', 'Merida', 'Terelj National Park', 'Galle', 'Caracas', 'Moscow', 'San Juan', 'Tlemcen', 'Tampere', 'Bursa', 'Ulaanbaatar']
#     # for_question2='"city": "return the exactly city i provided","name": "","latitude": ,"longitude": ,"review_score": ,"description": "","website":"","hours": "","telephone:"","tips":"provide me 3 tips","distance": "","formatted address":"","real_price": "give me price in USD $ (avrage price) if its for free return Free"'
#     for city2 in cities:
#         question_restaurnt=f'proivde me exactly 15 the best restaurants in {city2} with this details ("city": "","name": "","latitude": ,"longitude": ,"review_score":  ,"website":"can be social media also","category":"breakfast ,lunch ,dinner","hours": "","telephone:"","formatted address":"","price_range": "from 1 to 5-1cheap, 5 most expensive","tips":"provide me 3 tips as a list", do your best to find me the data you have. return me with double quetos and also as a dictionary like that "city": "return the exactly city I provided","name": "","latitude": ,"longitude": ,"review_score": ,"website":"can be social media also","category":"breakfast ,lunch ,dinner","hours": "","telephone:"","formatted address":"","price_range": "from 1 to 5-1cheap, 5 most expensive","tips":"provide me 3 tips as a list" ,do it fast and do not forget to return exactly 15 restaurants and the price_range return only in numbers'

#         # question=f'proivde me exactly 15 attractions in {city2} with this details ("city": "","name": "","latitude": ,"longitude": ,"review_score": ,"description": "","website":"","hours": "","telephone:"","tips":"provide me 3 tips","distance": "","formatted address":"","real_price": "" do your best to find me the best prices you have. return me with double quetos and also as a dictionary like that {for_question2},do it fast and do not forget to return exactly 15 attractions'
#         time.sleep(random_time)
#         driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/footer/div/div/div[1]/textarea').send_keys(question_restaurnt, Keys.ENTER)
#         time.sleep(3)
#         random_time_interval = random.uniform(190, 200)
#         time.sleep(random_time_interval)
#         attractions=driver.find_element(By.XPATH,f"/html/body/div[1]/div[1]/main/div/div/div/div[2]/div[{count}]/div[2]/div[2]").text
#         with open('attractions1.txt', 'a', encoding='utf-8') as f:
#             f.write(attractions + '\n')
#         count+=1
#         print (count)
# def poe3():
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"

#     # Set up the Chrome WebDriver with User-Agent and headless mode
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument(f"user-agent={user_agent}")
#     # chrome_options.add_argument("--headless")  # Run in headless mode

#     # Create a Chrome WebDriver instance
#     # service_path = "C:/Users/moshi/Downloads/chromedriver.exe"
#     # service = Service(service_path)
#     driver = webdriver.Chrome( options=chrome_options)
#     # driver.get('https://poe.com/Claude-2-100k')
#     # driver.get('https://poe.com/Claude-instant-100k')
#     driver.get('https://poe.com/Claude-instant')
#     driver.maximize_window()
#     time.sleep(random_time)
#     driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/a').click()
#     time.sleep(3)
#     driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/form/input').send_keys('amnontheking123456@gmail.com',Keys.ENTER)
#     time.sleep(100)
    
#     count=3
#     cities=[  'Chicago', 'Colombo', 'Valparaíso', 'Philadelphia', 'Fredrikstad',  'Singapore', 'Esbjerg', 'Leeds', 'Amsterdam', 'Cartagena', 'Glasgow', 'Pilsen',  'Karlovy Vary', 'Toronto',  'Phuket', 'Ulsan', 'Puerto Varas', 'Funchal']
#     # for_question2='"city": "return the exactly city i provided","name": "","latitude": ,"longitude": ,"review_score": ,"description": "","website":"","hours": "","telephone:"","tips":"provide me 3 tips","distance": "","formatted address":"","real_price": "give me price in USD $ (avrage price) if its for free return Free"'
#     for city2 in cities:
#         question_restaurnt=f'proivde me exactly 15 the best restaurants in {city2} with this details ("city": "","name": "","latitude": ,"longitude": ,"review_score":  ,"website":"can be social media also","category":"breakfast ,lunch ,dinner","hours": "","telephone:"","formatted address":"","price_range": "from 1 to 5-1cheap, 5 most expensive","tips":"provide me 3 tips as a list", do your best to find me the data you have. return me with double quetos and also as a dictionary like that "city": "return the exactly city I provided","name": "","latitude": ,"longitude": ,"review_score": ,"website":"can be social media also","category":"breakfast ,lunch ,dinner","hours": "","telephone:"","formatted address":"","price_range": "from 1 to 5-1cheap, 5 most expensive","tips":"provide me 3 tips as a list" ,do it fast and do not forget to return exactly 15 restaurants and the price_range return only in numbers'

#         # question=f'proivde me exactly 15 attractions in {city2} with this details ("city": "","name": "","latitude": ,"longitude": ,"review_score": ,"description": "","website":"","hours": "","telephone:"","tips":"provide me 3 tips","distance": "","formatted address":"","real_price": "" do your best to find me the best prices you have. return me with double quetos and also as a dictionary like that {for_question2},do it fast and do not forget to return exactly 15 attractions'
#         time.sleep(random_time)
#         driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/footer/div/div/div[1]/textarea').send_keys(question_restaurnt, Keys.ENTER)
#         time.sleep(3)
#         random_time_interval = random.uniform(190, 200)
#         time.sleep(random_time_interval)
#         attractions=driver.find_element(By.XPATH,f"/html/body/div[1]/div[1]/main/div/div/div/div[2]/div[{count}]/div[2]/div[2]").text
#         with open('attractions1.txt', 'a', encoding='utf-8') as f:
#             f.write(attractions + '\n')
#         count+=1
#         print (count)
# def poe4():
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"

#     # Set up the Chrome WebDriver with User-Agent and headless mode
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument(f"user-agent={user_agent}")
#     # chrome_options.add_argument("--headless")  # Run in headless mode

#     # Create a Chrome WebDriver instance
#     # service_path = "C:/Users/moshi/Downloads/chromedriver.exe"
#     # service = Service(service_path)
#     driver = webdriver.Chrome( options=chrome_options)
#     # driver.get('https://poe.com/Claude-2-100k')
#     # driver.get('https://poe.com/Claude-instant-100k')
#     driver.get('https://poe.com/Claude-instant')
#     driver.maximize_window()
#     time.sleep(random_time)
#     driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/a').click()
#     time.sleep(random_time)
#     driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/form/input').send_keys('amnontheking1234567@gmail.com',Keys.ENTER)
#     time.sleep(100)
    
#     count=3
#     cities=[  'Monteverde','Gothenburg', 'Nairobi', 'Cali', 'Dubrovnik', 'Kampala', 'Barcelona', 'Prague', 'Mykonos', 'Heraklion', 'Manila', 'Seattle', 'Maceio', 'Paris', 'Curitiba', 'Phnom Penh', 'Manchester', 'Canillo', 'Kharkhorin']
#     # for_question2='"city": "return the exactly city i provided","name": "","latitude": ,"longitude": ,"review_score": ,"description": "","website":"","hours": "","telephone:"","tips":"provide me 3 tips","distance": "","formatted address":"","real_price": "give me price in USD $ (avrage price) if its for free return Free"'
#     for city2 in cities:
#         question_restaurnt=f'proivde me exactly 15 the best restaurants in {city2} with this details ("city": "","name": "","latitude": ,"longitude": ,"review_score":  ,"website":"can be social media also","category":"breakfast ,lunch ,dinner","hours": "","telephone:"","formatted address":"","price_range": "from 1 to 5-1cheap, 5 most expensive","tips":"provide me 3 tips as a list", do your best to find me the data you have. return me with double quetos and also as a dictionary like that "city": "return the exactly city I provided","name": "","latitude": ,"longitude": ,"review_score": ,"website":"can be social media also","category":"breakfast ,lunch ,dinner","hours": "","telephone:"","formatted address":"","price_range": "from 1 to 5-1cheap, 5 most expensive","tips":"provide me 3 tips as a list" ,do it fast and do not forget to return exactly 15 restaurants and the price_range return only in numbers'

#         # question=f'proivde me exactly 15 attractions in {city2} with this details ("city": "","name": "","latitude": ,"longitude": ,"review_score": ,"description": "","website":"","hours": "","telephone:"","tips":"provide me 3 tips","distance": "","formatted address":"","real_price": "" do your best to find me the best prices you have. return me with double quetos and also as a dictionary like that {for_question2},do it fast and do not forget to return exactly 15 attractions'
#         time.sleep(random_time)
#         driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/footer/div/div/div[1]/textarea').send_keys(question_restaurnt, Keys.ENTER)
#         time.sleep(3)
#         random_time_interval = random.uniform(190, 200)
#         time.sleep(random_time_interval)
#         attractions=driver.find_element(By.XPATH,f"/html/body/div[1]/div[1]/main/div/div/div/div[2]/div[{count}]/div[2]/div[2]").text
#         with open('attractions1.txt', 'a', encoding='utf-8') as f:
#             f.write(attractions + '\n')
#         count+=1
#         print (count)

# thread_poe = threading.Thread(target=poe)
# thread_poe1 = threading.Thread(target=poe1)
# thread_poe2 = threading.Thread(target=poe2)
# thread_poe3 = threading.Thread(target=poe3)
# thread_poe4 = threading.Thread(target=poe4)
# # Start the threads
# thread_poe.start()
# thread_poe1.start()
# thread_poe2.start()
# thread_poe3.start()
# thread_poe4.start()
# # Wait for both threads to complete
# thread_poe.join()
# thread_poe1.join()
# thread_poe2.join()
# thread_poe3.join()
# thread_poe4.join()

# print("Both threads have completed.")