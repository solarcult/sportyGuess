import time
import random
from selenium import webdriver
from org.shil import utils
from org.shil.entity.match_fixture_entity import match_fixture_entity
from org.shil.db import match_fixtures_repository, fetch_url_repository

# https://www.whoscored.com/Teams/65/Fixtures/Spain-Barcelona

def process_team_fixtures(url):
    print('process_team_fixtures : ' + url)
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
    
    fixtures = browser.find_element_by_id('team-fixtures')
    elements = fixtures.find_elements_by_tag_name("tr")
    matchids = []
    errors=[]
    for element in elements:
        try:
            mfe = match_fixture_entity()
            mfe.match_id = element.get_attribute('data-id')
    #         print(match_id) #match_id
    #         print(element.find_elements_by_css_selector("td")[0].text) #nothing
            mfe.result = element.find_elements_by_css_selector("td")[1].text #WDL
            if(utils.getStr(mfe.result) is None):
                continue
            sed = element.find_elements_by_css_selector("td")[2]
            at = sed.find_element_by_tag_name('a')
            mfe.tournament = at.get_attribute('title') #tournament name
    #         tournament_link = at.get_attribute('href') #tournament link
            mfe.sdate = element.find_elements_by_css_selector("td")[3].text #date
    #         print(element.find_elements_by_css_selector("td")[4].text) #nothing
            sed = element.find_elements_by_css_selector("td")[5]
            at = sed.find_element_by_tag_name('a')
            mfe.home_team_name = at.text #team_name
            mfe.home_team_id = utils.find_team_id_from_teamurl(at.get_attribute('href')) #team link
            gs = element.find_elements_by_css_selector("td")[6].text # result *1:3*
            full_time_goalsvs = gs.strip('*')
            mfe.full_time_home_goals = full_time_goalsvs.split(':')[0].strip()
            mfe.full_time_away_goals = full_time_goalsvs.split(':')[1].strip()
            sed = element.find_elements_by_css_selector("td")[7]
            at = sed.find_element_by_tag_name('a')
            mfe.away_team_name = at.text #team_name
            mfe.away_team_id = utils.find_team_id_from_teamurl(at.get_attribute('href')) #team link
            match_report = element.find_elements_by_css_selector("td")[8]
    #         print(match_report.text) #match report
            if(len(match_report.text) > 6):
                matchids.append(mfe.match_id)
            
            mfe.date = utils.sdate2date(mfe.sdate)
            
            match_fixtures_repository.insert_match_fixture(mfe)
            
        except Exception as e:
            print('something wrong is here:!'+e)
            errors.append(mfe.match_id + ":" + e)
    
    browser.quit()
    
    for matchid in matchids:
        preview_link = 'https://www.whoscored.com/Matches/'+matchid+'/Preview'
        fetch_url_repository.insert_fetch_url(preview_link, fetch_url_repository.type_MatchPreview, preview_link)
    
    fetch_url_repository.update_last_record_of_url_status(url, errors)
    

# process_team_fixtures('https://www.whoscored.com/Teams/58/Fixtures/Spain-Real-Valladolid')