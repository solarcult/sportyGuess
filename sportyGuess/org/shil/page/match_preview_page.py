import time
import random
from selenium import webdriver 
from org.shil import utils
from org.shil.entity.match_preview_entity import match_preview_entity
from org.shil.db import match_preview_repository, fetch_url_repository
import json

# https://www.whoscored.com/Matches/1316424/Preview

'''
仔细比对了preview的数据：
第一，阵容是假想的，和真实情况有差异，这还是小事
最重要的是，数据都是最新的，不是当时的值，根本无法用于预测。只能通过每个player的历史数据反算吗?可以试试
应该只处理out的运动员,排序15个,算均值? 
怎样利用战前的数据统计与预测
'''

def process_match_preview(url):
    
    browser = webdriver.Chrome()
    print('process_match_preview : '+url)
    browser.get(url)
    time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
    
    mpe = match_preview_entity()
    errors=[]
    mpe.match_id = utils.find_match_id_from_matchurl(url)
    header = browser.find_element_by_class_name('pitch-formation-header')
    homet = header.find_element_by_class_name('home')
    homea = homet.find_element_by_tag_name('a')
    mpe.home_team_name = homea.text
    mpe.home_team_id = utils.find_team_id_from_teamurl(homea.get_attribute('href'))
    
    awayt = header.find_element_by_class_name('away')
    awaya = awayt.find_element_by_tag_name('a')
    mpe.away_team_name = awaya.text
    mpe.away_team_id = utils.find_team_id_from_teamurl(awaya.get_attribute('href'))
    
    pitch = browser.find_element_by_class_name('pitch')
    
    h_players = {}
    phome = pitch.find_element_by_class_name('home')
    uls = phome.find_elements_by_tag_name('ul')
    for ul in uls:
        try:
            h_player_id = ul.get_attribute("data-playerid")
            h_player_rate = ul.find_elements_by_tag_name('li')[1].text
            h_players[h_player_id] = h_player_rate
        except Exception as e:
            errors.append(h_player_id+"error : ")
            errors.append(e)
#     utils.print_map(home_players)
    mpe.home_players = json.dumps(h_players)
    
    a_players={}
    paway = pitch.find_element_by_class_name('away')
    uls = paway.find_elements_by_tag_name('ul')
    for ul in uls:
        try:
            a_player_id = ul.get_attribute("data-playerid")
            a_player_rate = ul.find_elements_by_tag_name('li')[1].text
            a_players[a_player_id] = a_player_rate
        except Exception as e:
            errors.append(h_player_id+" error:")
            errors.append(e)
#     utils.print_map(away_players)
    mpe.away_players = json.dumps(a_players)
    
#     print('data part')
    datapart = browser.find_element_by_id('probable-lineup-stats')
    stat_groups = datapart.find_elements_by_class_name('stat-group')
    stats = stat_groups[0].find_elements_by_class_name('stat')
    
    spans = stats[0].find_elements_by_tag_name('span')
    mpe.home_goals = spans[3].text
#     print(spans[4].text) # Goals
    mpe.away_goals = spans[5].text.split("(")[0].strip()

    spans = stats[1].find_elements_by_tag_name('span')
    mpe.home_assists = spans[3].text
#     print(spans[4].text) # Assists
    mpe.away_assists = spans[5].text.split("(")[0].strip()

    stats = stat_groups[1].find_elements_by_class_name('stat')
    spans = stats[0].find_elements_by_tag_name('span')
    mpe.home_average_ratings = spans[1].text.split(" ")[1]
#     print(spans[3].text) # Average Ratings
    mpe.away_average_ratings = spans[4].text.split(" ")[0]

    stats = stat_groups[2].find_elements_by_class_name('stat')
    spans = stats[0].find_elements_by_tag_name('span')
    mpe.home_shots_pg = spans[1].text.split(" ")[1]
#     print(spans[3].text) # Shots pg
    mpe.away_shots_pg = spans[4].text.split(" ")[0]
    
    spans = stats[1].find_elements_by_tag_name('span')
    mpe.home_aerial_duel_success = spans[1].text.split(" ")[1].strip("%")
#     print(spans[3].text) # Aerial Duel Success
    mpe.away_aerial_duel_success = spans[4].text.split(" ")[0].strip("%")
    
    spans = stats[2].find_elements_by_tag_name('span')
    mpe.home_dribbles_pg = spans[1].text.split(" ")[1]
#     print(spans[3].text) # Dribbles pg
    mpe.away_dribbles_pg = spans[4].text.split(" ")[0]
    
    spans = stats[3].find_elements_by_tag_name('span')
    mpe.home_tackles_pg = spans[1].text.split(" ")[1]
#     print(spans[3].text) #Tackles pg
    mpe.away_tackles_pg = spans[4].text.split(" ")[0]
    
    print("missing players part")
    missing_players = browser.find_element_by_id('missing-players')
    home_missing = missing_players.find_element_by_class_name('home')
    
    h_missing_players = {}
    try:
        hbody = home_missing.find_element_by_tag_name('tbody')
        trs = hbody.find_elements_by_tag_name('tr')
        for tr in trs:
            tds = tr.find_elements_by_tag_name('td')
#             player_name = tds[0].text
            h_m_p_id = utils.find_player_id_from_playerurl(tds[0].find_element_by_tag_name('a').get_attribute('href'))
            h_status= tds[2].text
#             rating = tds[3].text
            h_missing_players[h_m_p_id] = h_status
    except  Exception as e:
        print('home missing data no exist, ignore me please')
        print(e)
        errors.append('home missing data no exist, ignore me please:')
        errors.append(e)
    mpe.home_missing_players = json.dumps(h_missing_players)
    
    a_missing_players = {}
    try:
        away_missing = missing_players.find_element_by_class_name('away')
        abody = away_missing.find_element_by_tag_name('tbody')
        trs = abody.find_elements_by_tag_name('tr')
        for tr in trs:
            tds = tr.find_elements_by_tag_name('td')
#             player_name = tds[0].text
            a_m_p_id = utils.find_player_id_from_playerurl(tds[0].find_element_by_tag_name('a').get_attribute('href'))
            a_status = tds[2].text
#             rating = tds[3].text
            a_missing_players[a_m_p_id] = a_status
    except Exception as e:
        print('away missing data no exist, ignore me please')
        print(e)
        errors.append('away missing data no exist, ignore me please:')
        errors.append(e)
    mpe.away_missing_players = json.dumps(a_missing_players)
    
    browser.quit()
    
    match_preview_repository.insert_match_preview(mpe)
    fetch_url_repository.update_last_record_of_url_status(url, errors)
    
#     remove to team_page
#     for playerid in playerids :
#         print('https://www.whoscored.com/Players/'+playerid+'/Fixtures')

# 'https://www.whoscored.com/Matches/1316424/Preview'
# 'https://www.whoscored.com/Matches/1284927/Preview/England-Premier-League-2018-2019-Chelsea-Tottenham'

# process_match_preview('https://www.whoscored.com/Matches/1364706/Preview/Europe-UEFA-Europa-League-2018-2019-Chelsea-Dynamo-Kyiv')