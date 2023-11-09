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
url = "https://stackoverflow.com/questions/76550506/typeerror-webdriver-init-got-an-unexpected-keyword-argument-executable-p"
class_to_search = "fs-headline1"
required_ans = "TypeError: WebDriver.__init__() got an unexpected keyword argument 'executable_path' in Selenium Python"
while True:
    driver.refresh()
    time.sleep(5)
    driver.get(url)
    extracted_text = driver.find_element(By.CLASS_NAME, class_to_search)
    ans = extracted_text.text
    if(ans == required_ans):
        print("ans found: ", ans)
        break
driver.quit()
