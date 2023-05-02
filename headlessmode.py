from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# headless cms
option = webdriver.ChromeOptions()
option.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.get("https://www.rosiearasa.com")
print(driver.page_source)
driver.quit()




