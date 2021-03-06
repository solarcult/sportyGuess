
'''
Created on 2019-Feb-27

@author: shil

'''
from selenium import webdriver
import time
import random
from org.shil import utils
from org.shil.db import fetch_url_repository

'''
get all tournament in home page ,one of entrance of this data starter
'''


try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.implicitly_wait(utils.browser_implicitly_wait)
    url = 'https://www.whoscored.com/'
    browser.get(url)
    time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
    
    browser.find_element_by_id('qcCmpButtons').find_elements_by_tag_name('button')[1].click()

    time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
    
    touraments = {}
    
    uls = browser.find_element_by_id('popular-tournaments-list')
    lis = uls.find_elements_by_tag_name('li')
    for li in lis :
        tourament_name = li.text
        link = li.find_element_by_tag_name('a').get_attribute('href')
        touraments[tourament_name] = link
    
    for key in touraments.keys() :
        print(key+" : "+ touraments[key])
        params = [touraments[key],key]
        fetch_url_repository.insert_fetch_url(touraments[key], fetch_url_repository.type_Tournament, params)
    
finally:
    browser.quit()
