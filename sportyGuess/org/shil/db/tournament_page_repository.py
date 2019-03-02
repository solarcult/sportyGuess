from datetime import datetime
from org.shil import utils

def insert_tournament_team(tournament,no,team_name,team_link,team_id,played,win,draw,loss,goals_for,goals_against,goals_difference,points):
    
    exist = query_tournament_last_record_date(tournament,team_id)
    if exist is not None:
        # already exist this record, do not insert again
        print(tournament+" : " + team_id +" already exsit, no need insert")
        return
    
    insert_sql = "\
    INSERT INTO `tournament_teams`(\
        `tournament`,\
        `date`,\
        `no`,\
        `team_name`,\
        `team_link`,\
        `team_id`,\
        `played`,\
        `win`,\
        `draw`,\
        `loss`,\
        `goals_for`,\
        `goals_against`,\
        `goals_difference`,\
        `points`,\
        `sdate`)\
    VALUES \
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    cnx = utils.getMysqlConnector()
    cursor = cnx.cursor()
    
    sdate = (datetime.now().strftime('%d-%m-%Y'))
    values = (tournament,datetime.now(),no,team_name,team_link,team_id,played,win,draw,loss,goals_for,goals_against,goals_difference,points,sdate)
    
    cursor.execute(insert_sql,values)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid

def query_tournament_last_record_date(tournament,team_id):
    query_last_date = "SELECT date FROM `tournament_teams` where tournament = %s and team_id = %s order by date desc limit 1"
    cnx = utils.getMysqlConnector()
    cursor = cnx.cursor()
    cursor.execute(query_last_date,(tournament,team_id))
    return cursor.fetchone()[0]

def list_tournament_teams(tournament_name,query_date):
    cnx = utils.getMysqlConnector()
    cursor = cnx.cursor()
    list_tournament_teams_sql = "SELECT * FROM `tournament_teams` where tournament = %s and date= %s order by no "
    ps = (tournament_name,query_date)
    
    cursor.execute(list_tournament_teams_sql,ps)
    return cursor.fetchall()

ll = query_tournament_last_record_date('Liga NOS',298)
if ll is not None:
    print(ll)
else:
    print('ok')
xs = list_tournament_teams('Liga NOS',ll)
for x in xs:
    print(x)
    
