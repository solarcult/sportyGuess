import time
import random
from org.shil.db import team_statistics
from org.shil import team_fixtures_page

sleepMin = 5;
sleepMax = 10;

# https://www.whoscored.com/Teams/65/Show/Spain-Barcelona

def process_team_page(browser,url):
	
	print('process_team_page : '+url)
	
	browser.get(url);
	time.sleep(random.randrange(sleepMin,sleepMax))
	print("Team Statistics")
	print("Summary - Overall")
	ttss = browser.find_element_by_id('top-team-stats-summary')
	trs = ttss.find_element_by_id("top-team-stats-summary-content")
	elements = trs.find_elements_by_tag_name("tr")
	for element in elements:
	    print(element.find_elements_by_css_selector("td")[0].text)
	    print(element.find_elements_by_css_selector("td")[1].text)
	    print(element.find_elements_by_css_selector("td")[2].text)
	    print(element.find_elements_by_css_selector("td")[3].text)
	    print(element.find_elements_by_css_selector("td")[4].text)
	    print(element.find_elements_by_css_selector("td")[5].text)
	    print(element.find_elements_by_css_selector("td")[6].text)
	    print(element.find_elements_by_css_selector("td")[7].text)
	    print(element.find_elements_by_css_selector("td")[8].text)
	    
	
	print("Summary - Home")
	
	listbox = ttss.find_element_by_id('field')
	dds = listbox.find_elements_by_tag_name('dd')
	for dd in dds:
	    a = dd.find_element_by_tag_name('a')
	    if(a.text == team_statistics.view_Home):
	        a.click()
	        break

	time.sleep(random.randrange(sleepMin,sleepMax))
	
	ttss = browser.find_element_by_id('top-team-stats-summary')
	trs = ttss.find_element_by_id("top-team-stats-summary-content")
	elements = trs.find_elements_by_tag_name("tr")
	for element in elements:
	    print(element.find_elements_by_css_selector("td")[0].text)
	    print(element.find_elements_by_css_selector("td")[1].text)
	    print(element.find_elements_by_css_selector("td")[2].text)
	    print(element.find_elements_by_css_selector("td")[3].text)
	    print(element.find_elements_by_css_selector("td")[4].text)
	    print(element.find_elements_by_css_selector("td")[5].text)
	    print(element.find_elements_by_css_selector("td")[6].text)
	    print(element.find_elements_by_css_selector("td")[7].text)
	    print(element.find_elements_by_css_selector("td")[8].text)
	
	print("Summary - Away")
	
	listbox = ttss.find_element_by_id('field')
	dds = listbox.find_elements_by_tag_name('dd')
	for dd in dds:
	    a = dd.find_element_by_tag_name('a')
	    if(a.text == team_statistics.view_Away):
	        a.click()
	        break
	
	time.sleep(random.randrange(sleepMin,sleepMax))
	
	ttss = browser.find_element_by_id('top-team-stats-summary')
	trs = ttss.find_element_by_id("top-team-stats-summary-content")
	elements = trs.find_elements_by_tag_name("tr")
	for element in elements:
	    print(element.find_elements_by_css_selector("td")[0].text)
	    print(element.find_elements_by_css_selector("td")[1].text)
	    print(element.find_elements_by_css_selector("td")[2].text)
	    print(element.find_elements_by_css_selector("td")[3].text)
	    print(element.find_elements_by_css_selector("td")[4].text)
	    print(element.find_elements_by_css_selector("td")[5].text)
	    print(element.find_elements_by_css_selector("td")[6].text)
	    print(element.find_elements_by_css_selector("td")[7].text)
	    print(element.find_elements_by_css_selector("td")[8].text)
	    
	
	print("Defensive - Overall")
	
	defensive = browser.find_element_by_link_text(team_statistics.type_Defensive);
	defensive.click()
	
	time.sleep(random.randrange(sleepMin,sleepMax))
	
	ttss = browser.find_element_by_id('top-team-stats-defensive')
	trs = ttss.find_element_by_id("top-team-stats-summary-content")
	elements = trs.find_elements_by_tag_name("tr")
	for element in elements:
	    print(element.find_elements_by_css_selector("td")[0].text)
	    print(element.find_elements_by_css_selector("td")[1].text)
	    print(element.find_elements_by_css_selector("td")[2].text)
	    print(element.find_elements_by_css_selector("td")[3].text)
	    print(element.find_elements_by_css_selector("td")[4].text)
	    print(element.find_elements_by_css_selector("td")[5].text)
	    print(element.find_elements_by_css_selector("td")[6].text)
	    print(element.find_elements_by_css_selector("td")[7].text)
	
	
	print("Defensive - Home")
	
	listbox = ttss.find_element_by_id('field')
	dds = listbox.find_elements_by_tag_name('dd')
	for dd in dds:
	    a = dd.find_element_by_tag_name('a')
	    if(a.text == team_statistics.view_Home):
	        a.click()
	        break
	    
	time.sleep(random.randrange(sleepMin,sleepMax))
	
	ttss = browser.find_element_by_id('top-team-stats-defensive')
	trs = ttss.find_element_by_id("top-team-stats-summary-content")
	elements = trs.find_elements_by_tag_name("tr")
	for element in elements:
	    print(element.find_elements_by_css_selector("td")[0].text)
	    print(element.find_elements_by_css_selector("td")[1].text)
	    print(element.find_elements_by_css_selector("td")[2].text)
	    print(element.find_elements_by_css_selector("td")[3].text)
	    print(element.find_elements_by_css_selector("td")[4].text)
	    print(element.find_elements_by_css_selector("td")[5].text)
	    print(element.find_elements_by_css_selector("td")[6].text)
	    print(element.find_elements_by_css_selector("td")[7].text)
	
	print("Defensive - Away")
	
	listbox = ttss.find_element_by_id('field')
	dds = listbox.find_elements_by_tag_name('dd')
	for dd in dds:
	    a = dd.find_element_by_tag_name('a')
	    if(a.text == team_statistics.view_Away):
	        a.click()
	        break
	
	time.sleep(random.randrange(sleepMin,sleepMax))
	    
	ttss = browser.find_element_by_id('top-team-stats-defensive')
	trs = ttss.find_element_by_id("top-team-stats-summary-content")
	elements = trs.find_elements_by_tag_name("tr")
	for element in elements:
	    print(element.find_elements_by_css_selector("td")[0].text)
	    print(element.find_elements_by_css_selector("td")[1].text)
	    print(element.find_elements_by_css_selector("td")[2].text)
	    print(element.find_elements_by_css_selector("td")[3].text)
	    print(element.find_elements_by_css_selector("td")[4].text)
	    print(element.find_elements_by_css_selector("td")[5].text)
	    print(element.find_elements_by_css_selector("td")[6].text)
	    print(element.find_elements_by_css_selector("td")[7].text)
	
	
	print("Offensive - Overall")
	
	offensive = browser.find_element_by_link_text(team_statistics.type_Offensive);
	offensive.click()
	
	time.sleep(random.randrange(sleepMin,sleepMax))
	
	ttss = browser.find_element_by_id('top-team-stats-offensive')
	trs = ttss.find_element_by_id("top-team-stats-summary-content")
	elements = trs.find_elements_by_tag_name("tr")
	for element in elements:
	    print(element.find_elements_by_css_selector("td")[0].text)
	    print(element.find_elements_by_css_selector("td")[1].text)
	    print(element.find_elements_by_css_selector("td")[2].text)
	    print(element.find_elements_by_css_selector("td")[3].text)
	    print(element.find_elements_by_css_selector("td")[4].text)
	    print(element.find_elements_by_css_selector("td")[5].text)
	    print(element.find_elements_by_css_selector("td")[6].text)
	
	
	print("Offensive - Home")
	
	listbox = ttss.find_element_by_id('field')
	dds = listbox.find_elements_by_tag_name('dd')
	for dd in dds:
	    a = dd.find_element_by_tag_name('a')
	    if(a.text == team_statistics.view_Home):
	        a.click()
	        break
	    
	time.sleep(random.randrange(sleepMin,sleepMax))
	
	ttss = browser.find_element_by_id('top-team-stats-offensive')
	trs = ttss.find_element_by_id("top-team-stats-summary-content")
	elements = trs.find_elements_by_tag_name("tr")
	for element in elements:
	    print(element.find_elements_by_css_selector("td")[0].text)
	    print(element.find_elements_by_css_selector("td")[1].text)
	    print(element.find_elements_by_css_selector("td")[2].text)
	    print(element.find_elements_by_css_selector("td")[3].text)
	    print(element.find_elements_by_css_selector("td")[4].text)
	    print(element.find_elements_by_css_selector("td")[5].text)
	    print(element.find_elements_by_css_selector("td")[6].text)
	
	print("Offensive - Away")
	
	listbox = ttss.find_element_by_id('field')
	dds = listbox.find_elements_by_tag_name('dd')
	for dd in dds:
	    a = dd.find_element_by_tag_name('a')
	    if(a.text == team_statistics.view_Away):
	        a.click()
	        break
	
	time.sleep(random.randrange(sleepMin,sleepMax))
	    
	ttss = browser.find_element_by_id('top-team-stats-offensive')
	trs = ttss.find_element_by_id("top-team-stats-summary-content")
	elements = trs.find_elements_by_tag_name("tr")
	for element in elements:
	    print(element.find_elements_by_css_selector("td")[0].text)
	    print(element.find_elements_by_css_selector("td")[1].text)
	    print(element.find_elements_by_css_selector("td")[2].text)
	    print(element.find_elements_by_css_selector("td")[3].text)
	    print(element.find_elements_by_css_selector("td")[4].text)
	    print(element.find_elements_by_css_selector("td")[5].text)
	    print(element.find_elements_by_css_selector("td")[6].text)
	    
	    
	print('Team Squad')

	tss = browser.find_element_by_id('team-squad-stats')
	option = tss.find_element_by_id('tournamentOptions')
	ass = option.find_elements_by_tag_name('a')
	i=0
	length = len(ass)
	print(length)
	
	for i in range(0,length):
	    a = ass[i]
	    print(a.text + ' Overall')
	    a.click()
	    time.sleep(random.randrange(sleepMin,sleepMax))
	    o = tss.find_element_by_link_text(team_statistics.view_Overall)
	    o.click()
	    time.sleep(random.randrange(sleepMin,sleepMax))
	    tss = browser.find_element_by_id('team-squad-stats')
	    ptsb = tss.find_element_by_id('player-table-statistics-body')
	    trs = ptsb.find_elements_by_tag_name('tr')
	    for tr in trs:
	        tds = tr.find_elements_by_tag_name("td")
	        print(tds[0].text)
	        print(tds[1].text)
	        print(tds[2].text)
	        print(tds[3].text)
	        print(tds[4].text)
	        print(tds[5].text)
	        print(tds[6].text)
	        print(tds[7].text)
	        print(tds[8].text)
	        print(tds[9].text)
	        print(tds[10].text)
	        print(tds[11].text)
	        print(tds[12].text)
	        print(tds[13].text)
	        print(tds[14].text)
	        print(tds[15].text)
	        
	    print('this is Home')
	    h = tss.find_element_by_link_text(team_statistics.view_Home)
	    h.click()
	    time.sleep(random.randrange(sleepMin,sleepMax))
	    tss = browser.find_element_by_id('team-squad-stats')
	    ptsb = tss.find_element_by_id('player-table-statistics-body')
	    trs = ptsb.find_elements_by_tag_name('tr')
	    for tr in trs:
	        tds = tr.find_elements_by_tag_name("td")
	        print(tds[0].text)
	        print(tds[1].text)
	        print(tds[2].text)
	        print(tds[3].text)
	        print(tds[4].text)
	        print(tds[5].text)
	        print(tds[6].text)
	        print(tds[7].text)
	        print(tds[8].text)
	        print(tds[9].text)
	        print(tds[10].text)
	        print(tds[11].text)
	        print(tds[12].text)
	        print(tds[13].text)
	        print(tds[14].text)
	        print(tds[15].text)
	    
	    print('this is Away')
	    w = tss.find_element_by_link_text(team_statistics.view_Away)
	    w.click()
	    time.sleep(random.randrange(sleepMin,sleepMax))
	    tss = browser.find_element_by_id('team-squad-stats')
	    ptsb = tss.find_element_by_id('player-table-statistics-body')
	    trs = ptsb.find_elements_by_tag_name('tr')
	    for tr in trs:
	        tds = tr.find_elements_by_tag_name("td")
	        print(tds[0].text)
	        print(tds[1].text)
	        print(tds[2].text)
	        print(tds[3].text)
	        print(tds[4].text)
	        print(tds[5].text)
	        print(tds[6].text)
	        print(tds[7].text)
	        print(tds[8].text)
	        print(tds[9].text)
	        print(tds[10].text)
	        print(tds[11].text)
	        print(tds[12].text)
	        print(tds[13].text)
	        print(tds[14].text)
	        print(tds[15].text)
	
	
# 	process team history match
	fixtures_but = browser.find_element_by_id('sub-navigation').find_element_by_link_text("Fixtures")
   	fixtures_url = fixtures_but.get_attribute('href')
   	team_fixtures_page.process_team_fixtures(browser, fixtures_url)
   	
#   process team squad
	playerids = []
	for playerid in playerids :
		print('https://www.whoscored.com/Players/'+playerid+'/Fixtures')
