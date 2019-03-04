import time
import random
from selenium import webdriver 
from org.shil import utils

# https://www.whoscored.com/Matches/1316424/Preview

'''
仔细比对了preview的数据：
第一，阵容是假想的，和真实情况有差异，这还是小事
最重要的是，数据都是最新的，不是当时的值，根本无法用于预测。只能通过每个player的历史数据反算吗?可以试试
应该只处理out的运动员,排序14个,算均值? 
怎样利用战前的数据统计与预测
'''

def process_match_preview(url):
    
    browser = webdriver.Chrome()
    print('process_match_preview : '+url)
    browser.get(url)
    time.sleep(random.randrange(utils.sleepMin,utils.sleepMax))
    
    header = browser.find_element_by_class_name('pitch-formation-header')
    homet = header.find_element_by_class_name('home')
    homea = homet.find_element_by_tag_name('a')
    home_team_name = homea.text
    home_team_id = utils.find_team_id_from_teamurl(homea.get_attribute('href'))
    
    awayt = header.find_element_by_class_name('away')
    awaya = awayt.find_element_by_tag_name('a')
    away_team_name = awaya.text
    away_team_id = utils.find_team_id_from_teamurl(awaya.get_attribute('href'))
    
    pitch = browser.find_element_by_class_name('pitch')
    
    home_players = {}
    phome = pitch.find_element_by_class_name('home')
    uls = phome.find_elements_by_tag_name('ul')
    for ul in uls:
        h_player_id = ul.get_attribute("data-playerid")
#         print(h_player_id)
#         player_name = ul.get_attribute("title")
        h_player_rate = ul.find_elements_by_tag_name('li')[1].text
        home_players[h_player_id] = h_player_rate
    
    away_players={}
    paway = pitch.find_element_by_class_name('away')
    uls = paway.find_elements_by_tag_name('ul')
    for ul in uls:
        a_player_id = ul.get_attribute("data-playerid")
#         print(a_player_id)
#         player_name = ul.get_attribute("title")
        a_player_rate = ul.find_elements_by_tag_name('li')[1].text
        away_players[a_player_id] = a_player_rate
    
    print("----------------------------------------")
    
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
                
    except :
        print('home missing ignore me please')
    
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
                
    except :
        print('away missing ignore me please')
    
    print('home missing:')
    utils.print_map(h_missing_players)
    print('away missing:')
    utils.print_map(a_missing_players)
    
    browser.quit()
    
#     remove to team_page
#     for playerid in playerids :
#         print('https://www.whoscored.com/Players/'+playerid+'/Fixtures')

# 'https://www.whoscored.com/Matches/1316424/Preview'
# 'https://www.whoscored.com/Matches/1284927/Preview/England-Premier-League-2018-2019-Chelsea-Tottenham'

process_match_preview('https://www.whoscored.com/Matches/1284927/Preview')