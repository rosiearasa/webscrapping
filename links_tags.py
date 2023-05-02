from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# headless cms
option = webdriver.ChromeOptions()
option.headless = True


# starter setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
url = 'https://rosiearasa.com'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

def find_text():
    p = soup.find_all('p')
    for text in p:
        
        print(text)
        
    
def find_tags():
    l_tags = soup.find_all('a')
    for a in l_tags:
        print(a['href'])
        
        

# find all tags
# find_tags()
find_text()
driver.quit()