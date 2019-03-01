import time
import random
from org.shil import utils
from selenium import webdriver

# https://www.whoscored.com/Regions/206/Tournaments/4/Spain-La-Liga

def process_tournament_page(browser,url):
	
	print('process_tournament_page : '+url)
	
	browser.get(url)
	time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
	
	tournament_teams = {}
	
	tbody = browser.find_element_by_class_name('standings')
	trs = tbody.find_elements_by_tag_name('tr')
	for tr in trs :
		team_id = tr.get_attribute('data-team-id')
		tds = tr.find_elements_by_tag_name('td')
		no = tds[0].text
		a = tds[1].find_element_by_tag_name('a')
		team_name = a.text
		team_link = a.get_attribute('href')
		tournament_teams[team_id] = team_link
		played = tds[2].text
		win = tds[3].text
		draw = tds[4].text
		loss = tds[5].text
		goal_for = tds[6].text
		goals_against = tds[7].text
		goals_difference = tds[8].text
		points = tds[9].text
		
	for key in tournament_teams.keys() :
		print(key+" : "+ tournament_teams[key])
# 		team_page.process_team_page(browser,tournament_teams[key])
		break
		
		
browser = webdriver.Chrome()
process_tournament_page(browser, 'https://www.whoscored.com/Regions/206/Tournaments/4/Spain-La-Liga')