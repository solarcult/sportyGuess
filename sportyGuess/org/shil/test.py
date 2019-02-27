import mysql.connector
from org.shil.db import team_statistics


for i in range(0,8):
    print(i)

"""
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