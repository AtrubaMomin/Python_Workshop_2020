from bs4 import BeautifulSoup
import requests
import pandas as pd
for i in range(1 , 15):
    url_page=f"https://www.healthline.com/health/fitness-exercise/best-videos-dance-workout#{i}"
    respone=requests.get(url_page).text
    print(respone)