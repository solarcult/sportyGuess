import time
import random
from selenium import webdriver

sleepMin = 5;
sleepMax = 10;

# https://www.whoscored.com/Players/39722/Fixtures

def process_player_fixtures(browser,url):
    
    print('process_player_fixtures : ' +url)
    browser.get(url)
    time.sleep(random.randrange(sleepMin,sleepMax))
    
    body = browser.find_element_by_tag_name('tbody')
    trs = body.find_elements_by_tag_name('tr')
    for tr in trs:
        tds = tr.find_elements_by_tag_name('td')
        a = tds[0].find_element_by_tag_name('a')
        tourament_name = a.get_attribute('title')
        tourament_link = a.get_attribute('href')
        print(tourament_name)
        print(tourament_link)
        print(tds[1].text)
        print(tds[2].find_element_by_tag_name('a').text)
        print(tds[3].find_element_by_tag_name('a').text)
        print(tds[4].find_element_by_tag_name('a').text)
        print(tds[5].text) #noneed
        print(tds[6].text) #noneed
        print(tds[7].text) #min
        print(tds[8].text) #score
    
browser = webdriver.Chrome()
process_player_fixtures(browser, 'https://www.whoscored.com/Players/9446/Fixtures')