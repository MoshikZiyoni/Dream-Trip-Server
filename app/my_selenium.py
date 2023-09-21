# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By


# def perform_search(query):
#     query = query.replace(' ', '+')
    
#     chrome_options = Options()
#     chrome_options.add_argument("--lang=en-ca")

#     # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
    
#     driver = webdriver.Chrome(options=chrome_options)
    
#     try:
#         url = f"https://www.google.com/search?q={query}"
#         driver.get(url)
        
#         time.sleep(3)
        
#         span_elements=driver.find_element(By.CSS_SELECTOR,'span.z3HNkc').text
#         # span_elements = driver.find_element(By.CSS_SELECTOR, 'span.Aq14fc').text
        
#         if len(span_elements)<3:
#             return(span_elements)
#         else:
#             pass
#     except:
#         print ('not with google')
#     try:
#         new_query=f"foursquare {query}"
        
#         url = f"https://www.google.com/search?q={new_query}"
#         driver.get(url)
#         driver.find_element(By.CSS_SELECTOR,'div.yuRUbf:first-child').click()
#         time.sleep(2)
#         rating=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/span/span').text
#         if len(rating)<3:
#             return(rating)
#         else:
#             pass
#     except :
#         print ('not rating in foursquare')
#     try:
#         search_url = f'https://www.tripadvisor.com/Search?q={query}'
#         driver.get(search_url)
#         time.sleep(3)
#         element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]')

#         first_tab = driver.current_window_handle

#         # Find the element to click
#         element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]')

#         # Perform the click action
#         element.click()

#         # Switch to the new tab
#         for window_handle in driver.window_handles:
#             if window_handle != first_tab:
#                 driver.switch_to.window(window_handle)
#                 break
#         driver.switch_to.window(first_tab)
#         driver.close()

#         # Switch back to the new tab
#         driver.switch_to.window(driver.window_handles[-1])
#         # Close the first tab
#         time.sleep(5)
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
#         rating=driver.find_element(By.XPATH,'/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[9]/div/div/div/section/section/div[1]/div/div[3]/div[1]/div/div[1]/div[1]').text
#         if len(rating)<3:
#             return(rating)
#         else:
#             pass
#     except:
#         print ('not rating in trip advisor')
#     return None
    





# # import time
# # from selenium import webdriver
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.action_chains import ActionChains
# # from selenium.webdriver.common.keys import Keys
# # import re

# # import json

# # def GPT_search(country,city):
# #     max_retries = 3
# #     retries = 0

# #     while retries < max_retries:
# #         time.sleep(10)

# #         token="eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Iw4Wh7Q88m8aAp7-.SH40YDD_uuNgCho_OKUiI8Y30XHNqjXkUiPXtDLyBSKleaJSWm4Sk6CpHvwZ5pj6_IbUdqWUjppcIcb651qmkR1O_rYVP_v4nR6az208xx6cDKRH66wpyntVmf3l7N2ooLLSD_DDiHjWRQH5fOPZ7uBpewTvE-fAif4VtWdgfZg5JocnGmYmIxbOISAHQuIHTITYSz_TOODVCbvazJ2V0M-C63M4XMEaUmvbZnsujZ1HTv2bSDt-TGMH0T8IRk2-eBEGupniAaPnGrV1V_m-yuD6JgyInPRx8i2V2HQkK70H_57lmA59QqUzTC2OjD1WWOvjsCi-AgLNOY-B2AXPspc4NmeQzs9hvICRgqaxvvvgPS6XYUWUCxknj3KVAJvAhoRcoBLoRNvBFozruRzCEX23tnmIsxGf5b6-y70ALLa9cKtPEX-v7yXddQHMhckMVOIDQoj882uFJjEcoLoSLBDR1WhIEp61oDxJnLBwQqmQFra_PmI7mYbawao_cEc2D3TzpC79oZI4RtwvgvCr1dh3kjHbuMMA9V1QSfpcBfKy5RAJ_mpIPm2v9wu74OMRX0_bbnS-e8W4Z_2s0z5PRn1EPbp5E7hPWvnHltZRPB0cd_Ercx0cP_k5Xow9cs4cOd9xHBuLrn6JrT_s_1jaXRsJK0zdrVagZjFXJcMOo3VOTfhWz7zoDddh9D_OTwSWuqcGNelpaxpRYJxY0NXh78GvptRAKVGOIvyG4mzQDjoICmIrZOPWwfmQCzGKJRjd81RQyDrAr0BcdVftpGT5UfqtQADvt96rKE9YcL6VD5X53aOl1bpHxMeuYDkrBTrXMizblS3QL_2J4kIR_nPhrMCnWuvmxn5cKWsmpbbrAtFku2CAVvHI-pa4v7C4VuS-y5RRUIhJtoqq99zsZ1orxDJp8ZWCyex5_UwbsxZFV3UB768GYnDzsot11Hgjjom3SPZ_n_0bEQN_mColRi7_YpMjo5Ehovp8r6tx7yr_I3rjEwqDPtiHhywbOCFGX11GYATWPz0SssxIRJoz4DSFBlXpIyWpGga-orxq6yY_FOetCNewLjtUAdo5988dmOTsBynFHYrQpBKled2KF5wQb5u_9foVoCvYqUuo6x7sviZMnXWvfz2cosDkusWalQBgYsBdp9kySofgbpdVa9-02O8fELN48wqBqf35WN_h3rR78oDxKXTQsdp9w0KN0jlJbsxhyIK_p6_HEcoYeosvAY-zrCRSZUJz_jiFPTnSzhCXLk8DkCvCkaHl6qRrvetDbvSuFyzGy9pm_vnxU_MJvTkFjGZsGqgn9rcbqadGOU1JOaFC-ltyDqLTln1F10yLiIkWx1L-qK2qtSBLrNgc3j8QmHDuVcP4yBNk4BtNae0uIf8fyPQyUWyB_X74yCx2hccNFlFLucYZR2Ufizi7yk6eMsBqlzII2zHe7Q4yC7pfNVkVdz7wiOW_ZgFWq7wS5JhaRCuv7-kC4Sl_Z-3I5VOogMR0yn714KFBut-iB2TScyPVtNTRwu-hQkwVwUXS_BTUrjk8w58wPB_Eoi_sDKOEByPVJKodSQ4Ic4mSFYwMzl3IXMMKb9r7uSjDSocT7hGqe2UatHjZQP5phHRPoyNWF0vKp19I7n8uEhAY30hpTS_uPEngVELxCd5nYnt3OuTLzJNEOzXytvh95m0aIK_jBukN885gpE9giSA0VZnM77lqo_8-jizk1nZEBRA8fQsJLf9jamD5cHEbteB1gmPfPu-yH2KgoThwnmyXWf2kPsX7ravEdDqGqNFDIhZhPFioeT37a_nwehckZSFehxhVxKOv--ou9e_o2PTShrKsIY4xwLS3b7F-YLH1JGdIhxA9u-i5sd2e2LtlFaILaRhOgyb1ZQjfuQ9QEtRMPnUNSm0DnBWJt3P73ON0a52TXfr7GYV0ZfjzsqOtO_3ZZUY2ckRR4Gc6kSv2yfPqjX-y0f-W_9AgFxal0sUjpM1AmEGiRXnSHh-fSjIT_-La0psSgDConG7_CDMRUPDnDPAxOc0DDtKLV4i1fZAzhmmDQD4t6r5lz712oXxCnEfjLoc7nU8SDEo6feCkYUHJAoW3Qtbrpg_mWPBzvyU8LIcDrQ5tHr2Rp5ynC2LGNpvYBIi00ef3yFBFqmqqM4efyB1TNQopPJiuT0GgoF3Y3Zg-BjaB8pXCC5yM8jDLfhJ0rPXaCprM86spUgY1oLaml6PKmHW_sWOm70UdQvFZ0xX3U5-haY0SDE4D61exz3TuU6seN1Nn6XeQOx3UggLYViF8QkPfpQy80GpAwcoLIj7F2rrNWsVb8w8IRq53fQvxjSQetBdRcWWzU4PaEMekfuMxByO_1hHtvPf5nCAsf1OB6IWAFT6LW-VsryszZBGCftidjHT1_MdKsCcmuiDfilZMLV0MtOPwNktH4MvdVqu7c9S9VAJQRG7LDP5miVX8jnMnoC6vHHwjS-P0Tmgx1wG2ElNGWYDDBtJw0fNbwwjSPXXClMkFipZ40OHe5IBJ4lzaXDiUxrzmIgkuRhSYDsNX9ABET2RGq1UbxscJikGDxiyWHA.xtJpSPzjMYCpwpCgLabRdw"
# #         api=ChatGPT(token)
        
# #         time.sleep(5)    
# #         try:
# #             api.driver(Keys.ENTER)
# #             time.sleep(0.5)
# #             api.driver(Keys.ENTER)
# #             time.sleep(0.5)
# #             api.driver(Keys.ENTER)
# #         except:
# #             pass
        
# #         try:
# #             api.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div[1]/div[2]/button').click()
# #             time.sleep(0.5)
# #             api.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div[1]/div[2]/button[2]').click()
# #             time.sleep(0.5)
# #             api.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div[1]/div[2]/button[2]').click()
# #             time.sleep(0.5)
# #         except:
# #             pass
        
# #         api.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/main/div[3]/form/div/div/textarea').send_keys(f'let’s work this out be sure we have the right answer,can you provide a 5 attractions to do in {country} {city} with this details ("city": "", "name": "", "latitude": , "longitude": , "review_score": "", "description": "", "website": "", "hours_popular": "", "distance": "", "real_price": "") return me as JSON format only between ` ` and in the end ` `. example of answer [{"city": "Prague", "name": "Prague Castle", "latitude": 50.0934, "longitude": 14.3968, "review_score": 4.5, "description": "....", "hours_popular": "9am-5pm", "distance": "1.9 km from Old Town Square", "real_price": "350 CZK"},]')
# #         api.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/main/div[3]/form/div/div[1]/button').click()
# #         time.sleep(50)
# #         response = api.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/main/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div').text

# #         match = re.search(r'\[.*?\]', response)
# #         if match:
# #             attractions = match.group()

# #             # Return extracted attractions as JSON format
# #             print (attractions)
# #             return attractions
# #         retries += 1
# #         time.sleep(2)  # Wait before retrying
        
# #     return None  # Return None if all retries failed