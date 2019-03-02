
'''
Created on 2019-Feb-27

@author: shil

'''
from selenium import webdriver
import time
import random
from org.shil import tournament_page
from org.shil import utils

browser = webdriver.Chrome()

url = 'https://www.whoscored.com/'
browser.get(url)
time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))

touraments = {}

uls = browser.find_element_by_id('popular-tournaments-list')
lis = uls.find_elements_by_tag_name('li')
for li in lis :
    tourament_name = li.text
    link = li.find_element_by_tag_name('a').get_attribute('href')
    print(tourament_name)
    print(link)
    touraments[tourament_name] = link


for key in touraments.keys() :
    print(key+" : "+ touraments[key])
    tournament_page.process_tournament_page(browser, touraments[key],key)

browser.quit()

