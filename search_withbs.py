from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def get_all_name():
   
    url = 'https://www.nba.com/players'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    div = soup.find('table', class_= 'players-list')
    for li in div.find_all('div', class_='RosterRow_playerName__G28lg'):
        print(li.text)


option = webdriver.ChromeOptions()
option.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

get_all_name()

driver.quit()


#search with bootstrap and headless cms nba players list

