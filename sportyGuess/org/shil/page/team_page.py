import time
import random
from org.shil import utils
from selenium import webdriver
from org.shil.db import team_statistics_repository, squad_statistics_repository,\
	fetch_url_repository

'''
run this file after : upcoming_livescores_page for tonight match or home_page for all data 
'''

# https://www.whoscored.com/Teams/65/Show/Spain-Barcelona

def process_team_page(url,priority=fetch_url_repository.priority_Normal):
	
	print('process_team_page : '+url)
	try:
		browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
		browser.implicitly_wait(utils.browser_implicitly_wait)
		browser.get(url);
		time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
		
		browser.find_element_by_id('qcCmpButtons').find_elements_by_tag_name('button')[1].click()
		
		time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
		
		errors = []
		
		team_id = utils.find_team_id_from_teamurl(url)
# 		print(team_id)
		team_name = browser.find_element_by_class_name('team-header-name').text
# 		print(team_name)
		
		if priority == fetch_url_repository.priority_Normal:
			print("Record Team " + team_name +" fixtures")
			try:
				fixtures_but = browser.find_element_by_id('sub-navigation').find_element_by_link_text("Fixtures")
				fixtures_url = fixtures_but.get_attribute('href')
				fetch_url_repository.insert_fetch_url(fixtures_url, fetch_url_repository.type_TeamFixtures, fixtures_url)
			except Exception as e:
				print(team_name +" fixture has error.")
				print(e)
				errors.append(team_name +" fixture:")
				errors.append(str(e))
		
		print("Team Statistics " + team_name)
		print("Summary - Overall")
		summary_overall_is_fine = True
		try:
			ttss = browser.find_element_by_id('top-team-stats-summary')
			trs = ttss.find_element_by_id("top-team-stats-summary-content")
			elements = trs.find_elements_by_tag_name("tr")
			for element in elements:
				try:
					tournament = (element.find_elements_by_css_selector("td")[0].text)
# 					print(tournament)
					apps = (element.find_elements_by_css_selector("td")[1].text)
# 					print(apps)
					goals = (element.find_elements_by_css_selector("td")[2].text)
# 					print(goals)
					shots_pg = utils.getStr(element.find_elements_by_css_selector("td")[3].text)
# 					print(shots_pg)
			# 	    discipline = (element.find_elements_by_css_selector("td")[4].text)
					possession = utils.getStr(element.find_elements_by_css_selector("td")[5].text)
# 					print(possession)
					apass = utils.getStr(element.find_elements_by_css_selector("td")[6].text)
# 					print(apass)
					aerials_won = utils.getStr(element.find_elements_by_css_selector("td")[7].text)
# 					print(aerials_won)
					rating = utils.getStr(element.find_elements_by_css_selector("td")[8].text)
# 					print(rating)
				
					team_statistics_repository.insert_team_statistics_summary(tournament, team_id, team_name, team_statistics_repository.view_Overall, rating, apps, goals, shots_pg, possession, apass, aerials_won)
				except Exception as e:
					print(" for in name: "+tournament +" has error.")
					print(e)
		except Exception as e:
			print("Summary - Overall is a error ")
			print(e)
			errors.append("Summary - Overall:")
			errors.append(str(e))
			summary_overall_is_fine = False
			print("summary_overall_is_NOT_fine")
		
		if(summary_overall_is_fine):
			print("Summary - Home")
			try:
				listbox = ttss.find_element_by_id('field')
				dds = listbox.find_elements_by_tag_name('dd')
				for dd in dds:
					a = dd.find_element_by_tag_name('a')
					if(a.text == team_statistics_repository.view_Home):
						a.click()
						break
			
				time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
				
				ttss = browser.find_element_by_id('top-team-stats-summary')
				trs = ttss.find_element_by_id("top-team-stats-summary-content")
				elements = trs.find_elements_by_tag_name("tr")
				for element in elements:
					tournament = (element.find_elements_by_css_selector("td")[0].text)
					apps = (element.find_elements_by_css_selector("td")[1].text)
					goals = (element.find_elements_by_css_selector("td")[2].text)
					shots_pg = utils.getStr(element.find_elements_by_css_selector("td")[3].text)
			# 	    discipline = (element.find_elements_by_css_selector("td")[4].text)
					possession = utils.getStr(element.find_elements_by_css_selector("td")[5].text)
					apass = utils.getStr(element.find_elements_by_css_selector("td")[6].text)
					aerials_won = utils.getStr(element.find_elements_by_css_selector("td")[7].text)
					rating = utils.getStr(element.find_elements_by_css_selector("td")[8].text)
					
					team_statistics_repository.insert_team_statistics_summary(tournament, team_id, team_name, team_statistics_repository.view_Home, rating, apps, goals, shots_pg, possession, apass, aerials_won)
			except Exception as e:
				print("Summary - Home is a error ")
				print(e)
				errors.append('Summary-Home:')
				errors.append(str(e))
				
			print("Summary - Away")
			try:
				listbox = ttss.find_element_by_id('field')
				dds = listbox.find_elements_by_tag_name('dd')
				for dd in dds:
					a = dd.find_element_by_tag_name('a')
					if(a.text == team_statistics_repository.view_Away):
						a.click()
						break
				
				time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
				
				ttss = browser.find_element_by_id('top-team-stats-summary')
				trs = ttss.find_element_by_id("top-team-stats-summary-content")
				elements = trs.find_elements_by_tag_name("tr")
				for element in elements:
					tournament = (element.find_elements_by_css_selector("td")[0].text)
					apps = (element.find_elements_by_css_selector("td")[1].text)
					goals = (element.find_elements_by_css_selector("td")[2].text)
					shots_pg = utils.getStr(element.find_elements_by_css_selector("td")[3].text)
			# 	    discipline = (element.find_elements_by_css_selector("td")[4].text)
					possession = utils.getStr(element.find_elements_by_css_selector("td")[5].text)
					apass = utils.getStr(element.find_elements_by_css_selector("td")[6].text)
					aerials_won = utils.getStr(element.find_elements_by_css_selector("td")[7].text)
					rating = utils.getStr(element.find_elements_by_css_selector("td")[8].text)
					
					team_statistics_repository.insert_team_statistics_summary(tournament, team_id, team_name, team_statistics_repository.view_Away, rating, apps, goals, shots_pg, possession, apass, aerials_won)
			except Exception as e:
				print("Summary - Away is a error ")
				print(e)
				errors.append("Summary-Away:")
				errors.append(str(e))
				
			print("Defensive - Overall")
			try:
				defensive = browser.find_element_by_link_text(team_statistics_repository.type_Defensive);
				defensive.click()
				
				time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
				
				ttss = browser.find_element_by_id('top-team-stats-defensive')
				trs = ttss.find_element_by_id("top-team-stats-summary-content")
				elements = trs.find_elements_by_tag_name("tr")
				for element in elements:
					tournament = (element.find_elements_by_css_selector("td")[0].text)
					apps = (element.find_elements_by_css_selector("td")[1].text)
					shots_conceded_pg = utils.getStr(element.find_elements_by_css_selector("td")[2].text)
					tackles_pg = utils.getStr(element.find_elements_by_css_selector("td")[3].text)
					interceptions_pg = utils.getStr(element.find_elements_by_css_selector("td")[4].text)
					fouls_pg = utils.getStr(element.find_elements_by_css_selector("td")[5].text)
					offsides_pg = utils.getStr(element.find_elements_by_css_selector("td")[6].text)
					rating = utils.getStr(element.find_elements_by_css_selector("td")[7].text)
					
					team_statistics_repository.insert_team_statistics_defensive(tournament, team_id, team_name, team_statistics_repository.view_Overall, rating, apps, shots_conceded_pg, tackles_pg, interceptions_pg, fouls_pg, offsides_pg)
			except Exception as e:
				print("Defensive - Overall is a error.")
				print(e)
				errors.append('Defensive-Overall:')
				errors.append(str(e))
				
			print("Defensive - Home")
			try:
				listbox = ttss.find_element_by_id('field')
				dds = listbox.find_elements_by_tag_name('dd')
				for dd in dds:
					a = dd.find_element_by_tag_name('a')
					if(a.text == team_statistics_repository.view_Home):
						a.click()
						break
			
				time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
				
				ttss = browser.find_element_by_id('top-team-stats-defensive')
				trs = ttss.find_element_by_id("top-team-stats-summary-content")
				elements = trs.find_elements_by_tag_name("tr")
				for element in elements:
					tournament = (element.find_elements_by_css_selector("td")[0].text)
					apps = (element.find_elements_by_css_selector("td")[1].text)
					shots_conceded_pg = utils.getStr(element.find_elements_by_css_selector("td")[2].text)
					tackles_pg = utils.getStr(element.find_elements_by_css_selector("td")[3].text)
					interceptions_pg = utils.getStr(element.find_elements_by_css_selector("td")[4].text)
					fouls_pg = utils.getStr(element.find_elements_by_css_selector("td")[5].text)
					offsides_pg = utils.getStr(element.find_elements_by_css_selector("td")[6].text)
					rating = utils.getStr(element.find_elements_by_css_selector("td")[7].text)
					
					team_statistics_repository.insert_team_statistics_defensive(tournament, team_id, team_name, team_statistics_repository.view_Home, rating, apps, shots_conceded_pg, tackles_pg, interceptions_pg, fouls_pg, offsides_pg)
			except Exception as e:
				print("Defensive - Home is a error:")
				print(e)
				errors.append('Defensive-Home:')
				errors.append(str(e))
				
			print("Defensive - Away")
			try:
				listbox = ttss.find_element_by_id('field')
				dds = listbox.find_elements_by_tag_name('dd')
				for dd in dds:
					a = dd.find_element_by_tag_name('a')
					if(a.text == team_statistics_repository.view_Away):
						a.click()
						break
				
				time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
			
				ttss = browser.find_element_by_id('top-team-stats-defensive')
				trs = ttss.find_element_by_id("top-team-stats-summary-content")
				elements = trs.find_elements_by_tag_name("tr")
				for element in elements:
					tournament = (element.find_elements_by_css_selector("td")[0].text)
					apps = (element.find_elements_by_css_selector("td")[1].text)
					shots_conceded_pg = utils.getStr(element.find_elements_by_css_selector("td")[2].text)
					tackles_pg = utils.getStr(element.find_elements_by_css_selector("td")[3].text)
					interceptions_pg = utils.getStr(element.find_elements_by_css_selector("td")[4].text)
					fouls_pg = utils.getStr(element.find_elements_by_css_selector("td")[5].text)
					offsides_pg = utils.getStr(element.find_elements_by_css_selector("td")[6].text)
					rating = utils.getStr(element.find_elements_by_css_selector("td")[7].text)
					
					team_statistics_repository.insert_team_statistics_defensive(tournament, team_id, team_name, team_statistics_repository.view_Away, rating, apps, shots_conceded_pg, tackles_pg, interceptions_pg, fouls_pg, offsides_pg)
			except Exception as e:
				print("Defensive - Away is a error:")
				print(e)
				errors.append('Defensive-Away:')
				errors.append(str(e))
			
			print("Offensive - Overall")
			try:
			
				offensive = browser.find_element_by_link_text(team_statistics_repository.type_Offensive);
				offensive.click()
				
				time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
				
				ttss = browser.find_element_by_id('top-team-stats-offensive')
				trs = ttss.find_element_by_id("top-team-stats-summary-content")
				elements = trs.find_elements_by_tag_name("tr")
				for element in elements:
					tournament = (element.find_elements_by_css_selector("td")[0].text)
					apps = (element.find_elements_by_css_selector("td")[1].text)
					shots_pg = utils.getStr(element.find_elements_by_css_selector("td")[2].text)
					shots_ot_pg = utils.getStr(element.find_elements_by_css_selector("td")[3].text)
					dribbles_pg = utils.getStr(element.find_elements_by_css_selector("td")[4].text)
					fouled_pg = utils.getStr(element.find_elements_by_css_selector("td")[5].text)
					rating = utils.getStr(element.find_elements_by_css_selector("td")[6].text)
					
					team_statistics_repository.insert_team_statistics_offensive(tournament, team_id, team_name, team_statistics_repository.view_Overall, rating, apps, shots_pg, shots_ot_pg, dribbles_pg, fouled_pg)
			except Exception as e:
				print("Offensive - Overall is a error ")
				print(e)
				errors.append('Offensive-Overall:')
				errors.append(str(e))
			
			print("Offensive - Home")
			
			try:
				listbox = ttss.find_element_by_id('field')
				dds = listbox.find_elements_by_tag_name('dd')
				for dd in dds:
					a = dd.find_element_by_tag_name('a')
					if(a.text == team_statistics_repository.view_Home):
						a.click()
						break
					
				time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
				
				ttss = browser.find_element_by_id('top-team-stats-offensive')
				trs = ttss.find_element_by_id("top-team-stats-summary-content")
				elements = trs.find_elements_by_tag_name("tr")
				for element in elements:
					tournament = (element.find_elements_by_css_selector("td")[0].text)
					apps = (element.find_elements_by_css_selector("td")[1].text)
					shots_pg = utils.getStr(element.find_elements_by_css_selector("td")[2].text)
					shots_ot_pg = utils.getStr(element.find_elements_by_css_selector("td")[3].text)
					dribbles_pg = utils.getStr(element.find_elements_by_css_selector("td")[4].text)
					fouled_pg = utils.getStr(element.find_elements_by_css_selector("td")[5].text)
					rating = utils.getStr(element.find_elements_by_css_selector("td")[6].text)
				
					team_statistics_repository.insert_team_statistics_offensive(tournament, team_id, team_name, team_statistics_repository.view_Home, rating, apps, shots_pg, shots_ot_pg, dribbles_pg, fouled_pg)
			except Exception as e:
				print("Offensive - Home is a error.")
				print(e)
				errors.append('Offensive-Home:')
				errors.append(str(e))
			
			print("Offensive - Away")
			try:
				listbox = ttss.find_element_by_id('field')
				dds = listbox.find_elements_by_tag_name('dd')
				for dd in dds:
					a = dd.find_element_by_tag_name('a')
					if(a.text == team_statistics_repository.view_Away):
						a.click()
						break
				
				time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
			
				ttss = browser.find_element_by_id('top-team-stats-offensive')
				trs = ttss.find_element_by_id("top-team-stats-summary-content")
				elements = trs.find_elements_by_tag_name("tr")
				for element in elements:
					tournament = (element.find_elements_by_css_selector("td")[0].text)
					apps = (element.find_elements_by_css_selector("td")[1].text)
					shots_pg = utils.getStr(element.find_elements_by_css_selector("td")[2].text)
					shots_ot_pg = utils.getStr(element.find_elements_by_css_selector("td")[3].text)
					dribbles_pg = utils.getStr(element.find_elements_by_css_selector("td")[4].text)
					fouled_pg = utils.getStr(element.find_elements_by_css_selector("td")[5].text)
					rating = utils.getStr(element.find_elements_by_css_selector("td")[6].text)
					
					team_statistics_repository.insert_team_statistics_offensive(tournament, team_id, team_name, team_statistics_repository.view_Away, rating, apps, shots_pg, shots_ot_pg, dribbles_pg, fouled_pg)
			except Exception as e:
				print("Offensive - Away is a error.")
				print(e)
				errors.append('Offensive-Away:')
				errors.append(str(e))
		else:
			print(" * ! summary_overall_is_NOT_fine !")
			
		print('Team Squad')
		length = 0
		try:
			tss = browser.find_element_by_id('team-squad-stats')
			option = tss.find_element_by_id('tournamentOptions')
			ass = option.find_elements_by_tag_name('a')
			i=0
			length = len(ass)
		except Exception as e:
			print('Team Squad is missing')
			print(e)
			errors.append('Team Squad is missing')
			errors.append(str(e))
		
		for i in range(0,length):
			try:
				tss = browser.find_element_by_id('team-squad-stats')
				option = tss.find_element_by_id('tournamentOptions')
				ass = option.find_elements_by_tag_name('a')
				a = ass[i]
				tournament = a.text
				print(tournament + ' Overall')
				a.click()
				time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
				
				tss = browser.find_element_by_id('team-squad-stats')
				o = tss.find_element_by_link_text(team_statistics_repository.view_Overall)
				o.click()
				time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
				ptsb = tss.find_element_by_id('player-table-statistics-body')
				trs = ptsb.find_elements_by_tag_name('tr')
				for tr in trs:
					tds = tr.find_elements_by_tag_name("td")
					a = tds[2].find_element_by_tag_name('a')
					player_id = utils.find_player_id_from_playerurl(a.get_attribute('href'))
					player_name = a.text
					cm = (tds[3].text)
					apps = (tds[5].text)
					mins = (tds[6].text)
					goals = utils.getStr(tds[7].text)
					assists = utils.getStr(tds[8].text)
					shots_pg = utils.getStr(tds[11].text)
					apass = utils.getStr(tds[12].text)
					aerials_won = utils.getStr(tds[13].text)
					man_ot_match = utils.getStr(tds[14].text)
					rating = utils.getStr(tds[15].text)
					
					squad_statistics_repository.insert_squad_statistics_summary(tournament,team_id, team_statistics_repository.view_Overall, player_id, player_name, rating, cm, apps, mins, goals, assists, shots_pg, apass, aerials_won, man_ot_match)
					if priority == fetch_url_repository.priority_Normal:
						print('Record Player ' + player_name +' Fixtures')
						player_fixtures_url = 'https://www.whoscored.com/Players/'+player_id+'/Fixtures'
						fetch_url_repository.insert_fetch_url(player_fixtures_url, fetch_url_repository.type_PlayerFixtures, player_fixtures_url)
			except Exception as e:
				print("Team Squad " + tournament + " Overall has error!")
				print(e)
				errors.append("Team Squad " + tournament + " Overall:")
				errors.append(str(e))
			
			print(tournament + ' Home')
			try:
				h = tss.find_element_by_link_text(team_statistics_repository.view_Home)
				h.click()
				time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
				tss = browser.find_element_by_id('team-squad-stats')
				ptsb = tss.find_element_by_id('player-table-statistics-body')
				trs = ptsb.find_elements_by_tag_name('tr')
				for tr in trs:
					tds = tr.find_elements_by_tag_name("td")
					a = tds[2].find_element_by_tag_name('a')
					player_id = utils.find_player_id_from_playerurl(a.get_attribute('href'))
					player_name = a.text
					cm = (tds[3].text)
					apps = (tds[5].text)
					mins = (tds[6].text)
					goals = utils.getStr(tds[7].text)
					assists = utils.getStr(tds[8].text)
					shots_pg = utils.getStr(tds[11].text)
					apass = utils.getStr(tds[12].text)
					aerials_won = utils.getStr(tds[13].text)
					man_ot_match = utils.getStr(tds[14].text)
					rating = utils.getStr(tds[15].text)
					
					squad_statistics_repository.insert_squad_statistics_summary(tournament,team_id, team_statistics_repository.view_Home, player_id, player_name, rating, cm, apps, mins, goals, assists, shots_pg, apass, aerials_won, man_ot_match)
			except Exception as e:
				print("Team Squad " + tournament + " Home has error.")
				print(e)
				errors.append("Team Squad " + tournament + " Home!")
				errors.append(str(e))
				
			print(tournament + ' Away')
			try:
				w = tss.find_element_by_link_text(team_statistics_repository.view_Away)
				w.click()
				time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
				tss = browser.find_element_by_id('team-squad-stats')
				ptsb = tss.find_element_by_id('player-table-statistics-body')
				trs = ptsb.find_elements_by_tag_name('tr')
				for tr in trs:
					tds = tr.find_elements_by_tag_name("td")
					a = tds[2].find_element_by_tag_name('a')
					player_id = utils.find_player_id_from_playerurl(a.get_attribute('href'))
					player_name = a.text
					cm = (tds[3].text)
					apps = (tds[5].text)
					mins = (tds[6].text)
					goals = utils.getStr(tds[7].text)
					assists = utils.getStr(tds[8].text)
					shots_pg = utils.getStr(tds[11].text)
					apass = utils.getStr(tds[12].text)
					aerials_won = utils.getStr(tds[13].text)
					man_ot_match = utils.getStr(tds[14].text)
					rating = utils.getStr(tds[15].text)
					
					squad_statistics_repository.insert_squad_statistics_summary(tournament,team_id, team_statistics_repository.view_Away, player_id, player_name, rating, cm, apps, mins, goals, assists, shots_pg, apass, aerials_won, man_ot_match)
			except Exception as e:
				print("Team Squad " + tournament + " Away has error.")
				print(e)
				errors.append("Team Squad " + tournament + " Away:")
				errors.append(str(e))
		
		fetch_url_repository.update_last_record_of_url_status(url, errors)
	
	finally:
		browser.quit()

#   process team squad
# 	playerids = []
# 	for playerid in playerids :
# 		print()


# https://www.whoscored.com/Teams/65/Show/Spain-Barcelona
# browser = webdriver.Chrome()
# process_team_page('https://www.whoscored.com/Teams/65/Show/Spain-Barcelona')
