import time
import random
from selenium import webdriver
from org.shil import utils

# https://www.whoscored.com/Teams/65/Fixtures/Spain-Barcelona

def process_team_fixtures(browser,url):
    print('process_team_fixtures : ' + url)
    browser.get(url)
    time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
    
    fixtures = browser.find_element_by_id('team-fixtures')
    elements = fixtures.find_elements_by_tag_name("tr")
    matchids = []
    for element in elements:
        match_id = element.get_attribute('data-id')
#         print(match_id) #match_id
#         print(element.find_elements_by_css_selector("td")[0].text) #nothing
        result = element.find_elements_by_css_selector("td")[1].text #WDL
        sed = element.find_elements_by_css_selector("td")[2]
        at = sed.find_element_by_tag_name('a')
        tournament_name = at.get_attribute('title') #tournament name
        tournament_link = at.get_attribute('href') #tournament link
        sdate = element.find_elements_by_css_selector("td")[3].text #date
#         print(element.find_elements_by_css_selector("td")[4].text) #nothing
        sed = element.find_elements_by_css_selector("td")[5]
        at = sed.find_element_by_tag_name('a')
        home_team_name = at.text #team_name
        home_team_id = utils.find_team_id_from_teamurl(at.get_attribute('href')) #team link
        full_time_goalsvs = element.find_elements_by_css_selector("td")[6].text # result *1:3*
        sed = element.find_elements_by_css_selector("td")[7]
        at = sed.find_element_by_tag_name('a')
        away_team_name = at.text #team_name
        away_team_id = utils.find_team_id_from_teamurl(at.get_attribute('href')) #team link
        match_report = element.find_elements_by_css_selector("td")[8]
#         print(match_report.text) #match report
        if(len(match_report.text) > 6):
            matchids.append(match_id)
    
    for matchid in matchids:
        print('https://www.whoscored.com/Matches/'+matchid+'/Preview')
        

# browser = webdriver.Chrome()
# process_team_fixtures(browser, 'https://www.whoscored.com/Teams/65/Fixtures')