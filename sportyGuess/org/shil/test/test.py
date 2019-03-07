import mysql.connector
from org.shil.db import team_statistics_temp
from org.shil.entity.match_fixture_entity import match_fixture_entity
from org.shil import utils
from datetime import datetime
import json


errors = []
try:
    print(43+"abc")
except Exception as e:
    errors.append("abc")
    errors.append(e)

print(errors)


"""

print(float('4.55'))



date = datetime.strptime('07-03-2018','%d-%m-%Y')
print(date)
print(datetime.now())



a = '3 : 0'

print(a.split(':')[0].strip())
print(a.split(':')[1].strip())




a = match_fixture_entity()
a.match_id = 23
a.result = 'w'

b = match_fixture_entity()
b.match_id=23

print((b))

a.print_self()

print(a == b)




print(utils.getStr('                           '))


b = " a "
print(b.isspace())
print(b.strip())
print(len(b))

c="*4:3*"

print(c)
print(c.strip('*'))

list = ['abc',12.5]

print(list)

jstr = json.dumps(list)

print(jstr)

ret = json.loads(jstr)

print(ret)



print(utils.isStrNone('N/A'))

if utils.isStrNone('N/Aa'):
    print('thisisit')
else :
    print('no')
    


print(datetime.now())

print(datetime.now().strftime('%d-%m-%Y'))

print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))


ds ={
    'tournament_name' : '3',
    'date' : '3223'
    }
    
utils.print_map(ds)

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