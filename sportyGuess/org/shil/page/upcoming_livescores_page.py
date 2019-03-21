from org.shil import utils
from selenium import webdriver
from org.shil.db import fetch_url_repository

'''
get upcomming matches run this file everyday to fetch ontime preview match data snapshot
'''

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(utils.browser_implicitly_wait)
    browser.get('https://www.whoscored.com/LiveScores');
    
    livescores = browser.find_element_by_id('livescores')
    tbody = livescores.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    tournament_maps = {}
    team_links = []
    match_ids = []
    for tr in trs:
        try:
            id = tr.get_attribute('id')
            if(id.find('g')!= -1) :
    #             print("g : "+id)
                a = tr.find_elements_by_tag_name('a')[0]
                tournament_link = a.get_attribute('href')
                tournament_name = a.text
                params = [tournament_link,tournament_name]
                tournament_maps[tournament_name] = tournament_link
    #             fetch_url_repository.insert_fetch_url(tournament_link, fetch_url_repository.type_Tournament, params, fetch_url_repository.priority_High)
    #             print(tournament_name)
    #             print(tournament_link)
            elif(id.find('i') != -1 ):
    #             print('i : '+id)
                tds = tr.find_elements_by_tag_name('td')
                try:
                    preview = tds[9].find_elements_by_tag_name('a')[0].text
                    if(utils.getStr(preview) == 'Stream'):
                        print('Found Steam here , Ignore .')
                        continue
                except Exception as e:
                    print('Found Exception here , Ignore .')
                    print(e)
                    continue
                home_team_link = tds[5].find_element_by_tag_name('a').get_attribute('href')
                team_links.append(home_team_link)
    #             fetch_url_repository.insert_fetch_url(home_team_link, fetch_url_repository.type_TeamHome, home_team_link, fetch_url_repository.priority_High)
    #             print(home_team_link)
                match_id = utils.find_match_id_from_matchurl(tds[6].find_elements_by_tag_name('a')[0].get_attribute('href'))
    #             print(match_id)
                match_ids.append(match_id)
                away_team_link = tds[7].find_element_by_tag_name('a').get_attribute('href')
                team_links.append(away_team_link)
    #             fetch_url_repository.insert_fetch_url(away_team_link, fetch_url_repository.type_TeamHome, away_team_link, fetch_url_repository.priority_High)
    #             print(away_team_link)
            else:
                print('NNNNNNNNNNNNNNNNNNNNNNNNNever come here!')
                break
            
        except Exception as e:
            print("e , bye")
            pass
        
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
        
    print('start insert matches :')
    for match_id in match_ids:
        print(match_id)
        preview_match_url = 'https://www.whoscored.com/Matches/'+match_id+'/Preview'
        if(fetch_url_repository.update_url_priority(preview_match_url, fetch_url_repository.priority_High) < 0 ):
            fetch_url_repository.insert_fetch_url(preview_match_url, fetch_url_repository.type_MatchPreview, preview_match_url, fetch_url_repository.priority_High)

finally:
    browser.quit()