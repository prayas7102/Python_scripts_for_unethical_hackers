''' WEB MONITORING: python algo to find out any text on a dynamic website 
    in evry interval of given time example: to check if a product is 
    availabe on Amazon at a particular price after sometime '''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
username = "prayas7102"
url =f"https://github.com/{username}"
class_to_search = "wb-break-all"
required_ans = "password"
driver.refresh()
driver.get(url+"?tab=repositories")
extracted_text = driver.find_elements(By.CLASS_NAME, class_to_search)
links = []
for i in extracted_text:
    repo_name = i.text[:-7]
    links.append(f"{url}/{repo_name}")
print(links)
driver.quit()
