# Python 3.6.5
# Logins an example of logging into a website using selenium and configparser.

import confiparser
import time
from selenium import webdriver


config = configparser.ConfigParser()
config.read('config.ini')  # <-- Where your user/pass is stored.
user = config.get('WebsiteName', 'username')
password = config.get('WebsiteName', 'password')

driver = webdriver.Firefox()
driver.get('Example_website.com')

# Find input fields. Look at website source code to find ID or path.
user_form = driver.find_element_by_xpath('//*[@name="USERID"]')
pass_form = driver.find_element_by_xpath('//*[@name="PASSWORD"]')

# Login using data stored in config.ini
user_form.send_keys(user)
pass_form.send_keys(password)

# Again, replace with relevant CSS information. This just clicks "Login".
driver.find_element_by_xpath('//*[@value="Login"]').click()
