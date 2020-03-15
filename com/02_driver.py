from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path="../WebDriver/chromedriver"
)
url = "https://www.instagram.com/explore/tags/xpro3/"
driver.get(url) # input address and enter
time.sleep(5) #sleep.
pageString = driver.page_source
print(pageString)
driver.close()