import time
import random
from org.shil import team_page 

sleepMin = 5;
sleepMax = 10;

def process_tournament_page(browser,url):
	browser.get(url)
	time.sleep(random.randrange(sleepMin,sleepMax))
	
	tournament_teams = {}
	
	tbody = browser.find_element_by_class_name('standings')
	trs = tbody.find_elements_by_tag_name('tr')
	for tr in trs :
		team_id = tr.get_attribute('data-team-id')
		print(team_id)
		tds = tr.find_elements_by_tag_name('td')
		print(tds[0].text)
		a = tds[1].find_element_by_tag_name('a')
		print(a.text)
		team_link = a.get_attribute('href')
		print(team_link)
		tournament_teams[team_id] = team_link
		print(tds[2].text)
		print(tds[3].text)
		print(tds[4].text)
		print(tds[5].text)
		print(tds[6].text)
		print(tds[7].text)
		print(tds[8].text)
		print(tds[9].text)
		
	for key in tournament_teams.keys() :
		print(key+" : "+ tournament_teams[key])
		team_page.process_team_page(browser,tournament_teams[key])
		break
		
		
