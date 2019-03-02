import MySQLdb

sleepMin = 5
sleepMax = 10
TeamMark = 'Teams/'
PlayerMark = 'Players/'
MatchMark = 'Matches/'


def find_xxx_id_from_url(url,xxx):
    mark = url.find(xxx)
    start =mark+len(xxx)
    end = url.find('/',start)
    xxx_id = url[start:end]
    return xxx_id

# 'https://www.whoscored.com/Teams/65/Show/Spain-Barcelona'
def find_team_id_from_teamurl(url):
    return find_xxx_id_from_url(url, TeamMark)

# https://www.whoscored.com/Players/39722/Fixtures
def find_player_id_from_playerurl(url):
    return find_xxx_id_from_url(url, PlayerMark)

# https://www.whoscored.com/Matches/1284939/Preview/England-Premier-League-2018-2019-Liverpool-Watford
def find_match_id_from_matchurl(url):
    return find_xxx_id_from_url(url, MatchMark)


def print_map(amap):
    for key in amap.keys():
        print(key + " : " + amap[key])

def getMysqlConnector():
    return MySQLdb.connect(user='shil',password='sl134120',host='127.0.0.1',database = 'sporty')

def isStrNone(strs):
    if strs == 'N/A':
        return True
    if strs == '-':
        return True
    return False