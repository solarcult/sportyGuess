import time
import random
from selenium import webdriver

sleepMin = 5;
sleepMax = 10;

# https://www.whoscored.com/Matches/1316424/Preview

'''
仔细比对了preview的数据：
第一，阵容是假想的，和真实情况有差异，这还是小事
最重要的是，数据都是最新的，不是当时的值，根本无法用于预测。只能通过每个player的历史数据反算吗?可以试试
应该只处理out的运动员,排序14个,算均值? 
怎样利用战前的数据统计与预测
'''

def process_match_preview(browser,url):
    
    print('process_match_preview : '+url)
    browser.get(url)
    time.sleep(random.randrange(sleepMin,sleepMax))
    
    playerids=[]
    
    header = browser.find_element_by_class_name('pitch-formation-header')
    homet = header.find_element_by_class_name('home')
    homea = homet.find_element_by_tag_name('a')
    print(homea.text)
    print(homea.get_attribute('href'))
    
    awayt = header.find_element_by_class_name('away')
    awaya = awayt.find_element_by_tag_name('a')
    print(awaya.text)
    print(awaya.get_attribute('href'))
    
    pitch = browser.find_element_by_class_name('pitch')
    phome = pitch.find_element_by_class_name('home')
    uls = phome.find_elements_by_tag_name('ul')
    for ul in uls:
        h_player_id = ul.get_attribute("data-playerid")
        print(h_player_id)
        print(ul.get_attribute("title"))
        print(ul.find_elements_by_tag_name('li')[1].text)
        playerids.append(h_player_id)
    
    paway = pitch.find_element_by_class_name('away')
    uls = paway.find_elements_by_tag_name('ul')
    for ul in uls:
        a_player_id = ul.get_attribute("data-playerid")
        print(a_player_id)
        print(ul.get_attribute("title"))
        print(ul.find_elements_by_tag_name('li')[1].text)
        playerids.append(a_player_id)
    
    
    
    
    
    
    
    
#     remove to team_page
#     for playerid in playerids :
#         print('https://www.whoscored.com/Players/'+playerid+'/Fixtures')


browser = webdriver.Chrome()
process_match_preview(browser,'https://www.whoscored.com/Matches/1316424/Preview')