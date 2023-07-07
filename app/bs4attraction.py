
import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from collections import Counter
import time
import re
def LoadUpProxies():
    url = 'https://sslproxies.org/'
    header = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
	}
    response = requests.get(url,headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    divss = soup.find_all('div', class_='modal-body')
    proxy_list1 = []
    proxy_list= []
    for div in divss:
        proxy_list1.append(div.text)
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"  # Regular expression pattern to match IP addresses
    
    proxy_string = " ".join(proxy_list1)  # Convert the list to a single string
    
    ips = re.findall(ip_pattern, proxy_string)
    for ip in ips:
        # Perform operations on each IP address
        proxy_list.append(ip)
    return proxy_list

def google_search_attraction(query,max_retries=1):
    print ('start google search_attractionnnnnnn')
    retries = 0
    use_proxy = False
    for i in range (2):
        try:
            query = query.replace(' ', '+')
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
                'Accept-Language': 'en-US,en;q=0.5'
            }
            
            # Send a GET request to the Google search URL
            response = requests.get(f"https://www.google.com/search?q={query}&lr=lang_en", headers=headers)
            # soup1 = BeautifulSoup(response.text, 'html.parser')
            # print (soup1)
            
            if use_proxy:
                print('Start with proxy:', proxy)
                proxies_list = LoadUpProxies()  # Retrieve the list of proxies
                proxy_index = 0
                while proxy_index < len(proxies_list):
                    time.sleep(1)
                    proxy = proxies_list[proxy_index]  # Select the next proxy from the list
                    proxy_index += 1
                    
                    
                    
                    try:
                        # Set the proxy in the requests session
                        session = requests.Session()
                        session.proxies = {'http': f"http://{proxy}"}
                        
                        # Send a GET request to the Google search URL using the proxy
                        response = session.get(f"https://www.google.com/search?q={query}&lr=lang_en", headers=headers)
                        response.raise_for_status()
                        
                        if response.status_code == 200:
                            print('Response: status 200!!!!!!', )
                            break  # Exit the loop if a valid response is received using the proxy
                    
                    except requests.exceptions.RequestException as e:
                        print(f"Failed to connect using proxy: {proxy}")
                        print(f"Error: {e}")
                        
                    except requests.exceptions.HTTPError as e:
                        print(f"HTTP error occurred: {e}")
                    
                    except requests.exceptions.ConnectionError as e:
                        print(f"Error connecting to the proxy: {e}")
                    
                    except requests.exceptions.Timeout as e:
                        print(f"Timeout error occurred: {e}")
                    
                    except requests.exceptions.TooManyRedirects as e:
                        print(f"Too many redirects: {e}")

                # Fallback mechanism
                if proxy_index == len(proxies_list):
                    print("All proxies have been used without success. Implement a fallback mechanism here.")
                    
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(soup)
            prices = []
            href_list = []
            div_elements = soup.find_all('div')
            url_counter = Counter()  # Initialize a counter to count domain occurrences
            
            for div in div_elements:
                link = div.find('a')
                if link:
                    try:
                        if 'official' in div.text.lower() or 'website' in div.text.lower():
                            if 'google' in link['href'] or 'pdf' in link['href'] or '.html' in link['href'] or 'viator' in link['href']:
                                continue
                            if link['href'].startswith('http'):
                                # print(link['href'])
                                url_counter[link['href']] += 1  # Increment the counter for the URL
                            else:
                                continue
                    except:
                        continue
            if url_counter:
                # Find the most common URL and its count
                most_common_url, count = url_counter.most_common(1)[0]
                print('most_common_url: ',most_common_url)  # Print the most common URL
            else:
                print('not url')
            div_elements = soup.find_all('div')
    
            for div in div_elements:      
                span_elements = div.find_all('span', {'aria-hidden': 'true', 'class': 'oqSTJd'})
                for span in span_elements:
                    score_text = span.text.strip()
                    review_score = score_text.split('/')[0]
                    if review_score is None:
                        review_score = ""

                    print({"review_score": review_score})
                    if href_list:
                        print ("review_score:", review_score, "url:", most_common_url,'for attractionnnnn')
                        return {"review_score": review_score, "url": most_common_url}
                        
                    else:
                        return {"review_score": review_score,"url": ""}
        except Exception as e:
            print(f"An error occurred: {e}")
            retries += 1
            print(f"Retrying ({retries}/{max_retries})...")
            time.sleep(1)  # Add a delay before retrying
            if not use_proxy and retries < max_retries:
                use_proxy = True