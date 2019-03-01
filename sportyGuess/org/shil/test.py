import mysql.connector
from org.shil.db import team_statistics
from org.shil import utils

s = 'https://www.whoscored.com/Teams/65/Show/Spain-Barcelona'

print(utils.find_team_id_from_teamurl(s))

# start = s.find('Teams/')
# print(start)
# end = s.find('/',start)
# here = s[start:end]

p = 'https://www.whoscored.com/Players/39722/Fixtures'

print(utils.find_player_id_from_playerurl(p))

m ='https://www.whoscored.com/Matches/1284939/Preview/England-Premier-League-2018-2019-Liverpool-Watford'
print(utils.find_match_id_from_matchurl(m))

"""

for i in range(0,8):
    print(i)

cnx = mysql.connector.connect(user='shil',password='sl134120',host='127.0.0.1',database = 'sporty')

x = cnx.cursor()

z = type(x)
print(z)


v = x.execute("select count(1) from team_statistics")

for r in x :
    print(r)

cnx.close()


class abc:
    def __init__(self):
        print("this is it")
        
    def printself(self):
        for x in self.__dict__.items():
            print(x)

ok = abc()

ok.a =23
ok.b=32
setattr(ok, team_statistics.team_id, 'bsdteam')

ok.printself()

print(getattr(ok, team_statistics.team_id))
"""