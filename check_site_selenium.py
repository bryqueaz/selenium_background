# coding: utf-8
'''
Develop: Bryan Quesada Azofeifa | bryan@gridshield.net
Date: Thu Apr  4 17:05:16 CST 2019
Version: 1.0
Usage:

'''

import codecs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
##https://selenium-python.readthedocs.io/locating-elements.html
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome('/opt/selenium_webdriver_chrome/chromedriver', chrome_options=options) # change path chromedriver
print ("Headless Chrome Initialized")
driver.get("https://www.gridshield.com/")
page = driver.page_source
file_r = codecs.open('page.html', 'w', encoding='utf8')
file_r.write(page)
file_r.close()
