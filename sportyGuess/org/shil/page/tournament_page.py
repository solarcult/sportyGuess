import time
import random
from selenium import webdriver
from org.shil import utils
from org.shil.db import tournament_page_repository, fetch_url_repository

# https://www.whoscored.com/Regions/206/Tournaments/4/Spain-La-Liga

def process_tournament_page(url,tournament_name):
	
	print('process_tournament_page : '+url)
	browser = webdriver.Chrome()
	
	browser.get(url)
	time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
	
	tournament_teams = {}
	errors = []
	tbody = browser.find_element_by_class_name('standings')
	trs = tbody.find_elements_by_tag_name('tr')
	for tr in trs :
		try:
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
			goals_for = tds[6].text
			goals_against = tds[7].text
			goals_difference = tds[8].text
			points = tds[9].text
			tournament_page_repository.insert_tournament_team(tournament_name, no, team_name, team_link, team_id, played, win, draw, loss, goals_for, goals_against, goals_difference, points)
		except:
			print("something wrong here!")
			errors.append("something wrong here!")
			
	browser.quit()
	
	for key in tournament_teams.keys() :
		print(key+" : "+ tournament_teams[key])
		fetch_url_repository.insert_fetch_url(tournament_teams[key], fetch_url_repository.type_TeamHome, tournament_teams[key])
	
	fetch_url_repository.update_last_record_of_url_status(url, errors)
	

process_tournament_page('https://www.whoscored.com/Regions/206/Tournaments/4/Spain-La-Liga', "La Liga")