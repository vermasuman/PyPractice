from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
search = driver.find_element(By.XPATH, '//textarea[@name="q"]')
search.clear()
search.send_keys("James Bond Movies")
search.send_keys(Keys.ENTER)

print(driver.current_url)
print(driver.title)
driver.close()
driver.quit()

