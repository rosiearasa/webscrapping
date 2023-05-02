from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from config import * 

headers = headers()
cookies = cookies()



response = requests.get('https://read.amazon.com/kindle-library', headers=headers, cookies=cookies)

# headless cms
option = webdriver.ChromeOptions()
option.headless = True

# starter setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
soup = BeautifulSoup(response.content, 'html.parser')

def list_all_books():
    div = soup.find(class_="_18oNBwLP1oBKNoOJzx5Qaw")
    
    for i in div:
        print(i)

list_all_books()
