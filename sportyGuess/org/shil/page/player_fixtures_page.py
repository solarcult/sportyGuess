import time
import random
from selenium import webdriver
from org.shil import utils
from org.shil.db import match_fixtures_repository,\
    player_match_behavior_repository, fetch_url_repository

# https://www.whoscored.com/Players/39722/Fixtures

def process_player_fixtures(url):
    
    print('process_player_fixtures : ' +url)
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
    
    errors=[]
    
    player_id = utils.find_player_id_from_playerurl(url)
    player_name = browser.find_element_by_class_name('header-name').text.strip()

    body = browser.find_element_by_tag_name('tbody')
    trs = body.find_elements_by_tag_name('tr')
    for tr in trs:
        try:
            tds = tr.find_elements_by_tag_name('td')
    #         a = tds[0].find_element_by_tag_name('a')
    #         tourament_name = a.get_attribute('title')
    #         tourament_link = a.get_attribute('href')
            sdate = tds[1].text #26-07-2018
    #         home_team_name = tds[2].find_element_by_tag_name('a').text
            home_team_id = utils.find_team_id_from_teamurl(tds[2].find_element_by_tag_name('a').get_attribute('href'))
    #         goalsvs = tds[3].find_element_by_tag_name('a').text
    #         match_id = utils.find_match_id_from_matchurl(tds[3].find_element_by_tag_name('a').get_attribute('href'))
    #         away_team_name = tds[4].find_element_by_tag_name('a').text
            away_team_id = utils.find_team_id_from_teamurl(tds[4].find_element_by_tag_name('a').get_attribute('href'))
            mins = tds[7].text.strip('\'')
            rating_in_this_match = utils.getStr(tds[8].text)
            
            match_id = match_fixtures_repository.query_match_id(home_team_id, away_team_id, sdate)
            if(match_id is None):
                errors.append("htid: "+ home_team_id+ "atid: " +away_team_id +"sd: " + sdate +" is missing.")
                continue
            
            player_match_behavior_repository.insert_player_match_behavior(match_id, player_id, player_name, mins, rating_in_this_match, sdate)

        except Exception as e:
            print("something wrong in here!"+e)
            errors.append(e)
    
    browser.quit()
    
    fetch_url_repository.update_last_record_of_url_status(url, errors)
        
# process_player_fixtures('https://www.whoscored.com/Players/9446/Fixtures')