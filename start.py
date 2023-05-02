from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# headless cms
option = webdriver.ChromeOptions()
option.headless = True

# starter setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.get("https://www.rosiearasa.com")
driver.quit()

#this file contains complete starter code for all the projects in this folder