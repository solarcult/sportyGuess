import time
import random
from selenium import webdriver

sleepMin = 5;
sleepMax = 10;

# https://www.whoscored.com/Teams/65/Fixtures/Spain-Barcelona

def process_team_fixtures(browser,url):
    print('process_team_fixtures : ' + url)
    browser.get(url)
    time.sleep(random.randrange(sleepMin,sleepMax))
    
    fixtures = browser.find_element_by_id('team-fixtures')
    elements = fixtures.find_elements_by_tag_name("tr")
    matchids = []
    for element in elements:
        match_id = element.get_attribute('data-id')
        print(match_id) #match_id
        print(element.find_elements_by_css_selector("td")[0].text) #nothing
        print(element.find_elements_by_css_selector("td")[1].text) #WDL
        sed = element.find_elements_by_css_selector("td")[2]
        at = sed.find_element_by_tag_name('a')
        print(at.get_attribute('title')) #tournament name
        print(at.get_property('href')) #tournament link
        print(element.find_elements_by_css_selector("td")[3].text) #date
        print(element.find_elements_by_css_selector("td")[4].text) #nothing
        sed = element.find_elements_by_css_selector("td")[5]
        at = sed.find_element_by_tag_name('a')
        print(at.text) #team_name
        print(at.get_property('href')) #team link
        print(element.find_elements_by_css_selector("td")[6].text) # result
        sed = element.find_elements_by_css_selector("td")[7]
        at = sed.find_element_by_tag_name('a')
        print(at.text) #team name
        print(at.get_property('href')) #team link
        matchlink = element.find_elements_by_css_selector("td")[8]
        print(matchlink.text) #match report
        if(len(matchlink.text) > 6):
            print(matchlink.get_property('href'))
            matchids.append(match_id)
    
    for matchid in matchids:
        print('https://www.whoscored.com/Matches/'+matchid+'/Preview')
        

browser = webdriver.Chrome()
process_team_fixtures(browser, 'https://www.whoscored.com/Teams/65/Fixtures/Spain-Barcelona')