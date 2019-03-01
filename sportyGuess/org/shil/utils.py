
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


def print_map(map):
    for key in map.keys():
        print(key + " : " + map[key])
