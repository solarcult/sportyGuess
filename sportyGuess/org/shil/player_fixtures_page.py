import time
import random
from selenium import webdriver
from org.shil import utils

# https://www.whoscored.com/Players/39722/Fixtures

def process_player_fixtures(browser,url):
    
    print('process_player_fixtures : ' +url)
    browser.get(url)
    time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
    
    body = browser.find_element_by_tag_name('tbody')
    trs = body.find_elements_by_tag_name('tr')
    for tr in trs:
        tds = tr.find_elements_by_tag_name('td')
        a = tds[0].find_element_by_tag_name('a')
        tourament_name = a.get_attribute('title')
        tourament_link = a.get_attribute('href')
        sdate = tds[1].text #26-07-2018
        home_team_name = tds[2].find_element_by_tag_name('a').text
        home_team_id = utils.find_team_id_from_teamurl(tds[2].find_element_by_tag_name('a').get_attribute('href'))
        goalsvs = tds[3].find_element_by_tag_name('a').text
        match_id = utils.find_match_id_from_matchurl(tds[3].find_element_by_tag_name('a').get_attribute('href'))
        away_team_name = tds[4].find_element_by_tag_name('a').text
        away_team_id = utils.find_team_id_from_teamurl(tds[4].find_element_by_tag_name('a').get_attribute('href'))
        min = tds[7].text
        rating_in_match = tds[8].text
    
browser = webdriver.Chrome()
process_player_fixtures(browser, 'https://www.whoscored.com/Players/9446/Fixtures')