from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path='./chromedriver'
)

driver.get("http://www.tutorialsninja.com/demo/")

elem = driver.find_element('name', 'search')
elem.send_keys('iphone')
elem.send_keys(Keys.RETURN)
add_to_cart_button = driver.find_element('xpath', '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
add_to_cart_button.click()
shopping_cart_link = driver.find_element(By.LINK_TEXT, 'Shopping Cart')
shopping_cart_link.click()
assert 'product 11' in driver.page_source
driver.close()

# import time
# driver.get('http://www.google.com/')
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element('name', 'q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()

pass