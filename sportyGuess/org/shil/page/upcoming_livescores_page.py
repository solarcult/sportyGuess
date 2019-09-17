import time
import random
from org.shil import utils
from selenium import webdriver
from org.shil.db import fetch_url_repository

'''
get upcomming matches run this file everyday to fetch ontime preview match data snapshot
'''

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.implicitly_wait(utils.browser_implicitly_wait)
    browser.get('https://www.whoscored.com/LiveScores');
    
    time.sleep(1)
    browser.find_element_by_id('qcCmpButtons').find_elements_by_tag_name('button')[1].click()
    time.sleep(1)
    
    livescores = browser.find_element_by_id('livescores')
    tbody = livescores.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    tournament_maps = {}
    team_links = []
    match_ids = []
    for tr in trs:
        try:
            id = tr.get_attribute('id')
            print('process id:'+id)
            if(id.find('g')!= -1) :
                a = tr.find_elements_by_tag_name('a')[0]
                tournament_link = a.get_attribute('href')
                tournament_name = a.text
                params = [tournament_link,tournament_name]
                tournament_maps[tournament_name] = tournament_link
            elif(id.find('i') != -1 ):
                tds = tr.find_elements_by_tag_name('td')
                try:
#                     print(tds[9].text)
                    if len(tds[9].text) < 1:
                        print(tds[9].text)
                        continue
                    a = tds[9].find_elements_by_tag_name('a')
                    preview = a[0].text
                    print(preview)
                    if(utils.getStr(preview).find('Preview') == -1
                       and utils.getStr(preview).find('Match') == -1 ):
                        print('        not preview')
#                         print('3. Not Found Preview or Match Report here , Ignore .')
                    else:
                        match_id = utils.find_match_id_from_matchurl(tds[6].find_elements_by_tag_name('a')[0].get_attribute('href'))
                        match_ids.append(match_id)
                        print('* Found the match:'+match_id)
                    
                    home_team_link = tds[5].find_element_by_tag_name('a').get_attribute('href')
                    team_links.append(home_team_link)
                    
                    away_team_link = tds[7].find_element_by_tag_name('a').get_attribute('href')
                    team_links.append(away_team_link)
                    
                except Exception as e:
                    print('Found Exception here , Ignore .')
                    print(e)
                    continue
            else:
                print('NNNNNNNNNNNNNNNNNNNNNNNNNever come here!')
                break
            
        except Exception:
            print("tr, e , bye")
            pass

    print('start insert matches :')
    for match_id in match_ids:
        print(match_id)
        preview_match_url = 'https://www.whoscored.com/Matches/'+match_id+'/Preview'
        if(fetch_url_repository.update_url_priority(preview_match_url, fetch_url_repository.priority_High) < 0 ):
            fetch_url_repository.insert_fetch_url(preview_match_url, fetch_url_repository.type_MatchPreview, preview_match_url, fetch_url_repository.priority_High)


    print('start insert tournaments:')
    for key in tournament_maps.keys() :
        print(key+" : "+ tournament_maps[key])
        params = [tournament_maps[key],key]
        if(fetch_url_repository.update_url_priority(tournament_maps[key], fetch_url_repository.priority_High) < 0 ):
            fetch_url_repository.insert_fetch_url(tournament_maps[key], fetch_url_repository.type_Tournament, params,fetch_url_repository.priority_High)
        
    print('start insert teams link:')
    for team_link in team_links:
        print(team_link)
        if(fetch_url_repository.update_url_priority(team_link, fetch_url_repository.priority_High) < 0 ):
            fetch_url_repository.insert_fetch_url(team_link, fetch_url_repository.type_TeamHome, team_link, fetch_url_repository.priority_High)


finally:
    browser.quit()