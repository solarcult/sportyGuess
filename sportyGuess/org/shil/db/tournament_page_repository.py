from datetime import datetime
from org.shil import utils

def insert_tournament_team(tournament,no,team_name,team_link,team_id,played,win,draw,loss,goals_for,goals_against,goals_difference,points):
    
    sdate = utils.date2sdate(datetime.now())
    exist = query_tournament_last_record_sdate(tournament,team_id)
    
    if exist is not None \
        and exist[0] == sdate:
        # already exist this record, do not insert again
        print(tournament+" : " + team_id +" tournament has been inserted today, no need insert")
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
    
    values = (tournament,datetime.now(),no,team_name,team_link,team_id,played,win,draw,loss,goals_for,goals_against,goals_difference,points,sdate)
    
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(insert_sql,values)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid

def query_tournament_last_record_sdate(tournament,team_id):
    query_last_data = "SELECT sdate FROM `tournament_teams` where tournament = %s and team_id = %s order by date desc limit 1"
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(query_last_data,(tournament,team_id))
    last_data = cursor.fetchone()
    if last_data is not None :
        return last_data
    else:
        return None

'''
def list_tournament_teams(tournament_name,query_sdate):
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    list_tournament_teams_sql = "SELECT * FROM `tournament_teams` where tournament = %s and sdate= %s order by no "
    ps = (tournament_name,query_sdate)
    
    cursor.execute(list_tournament_teams_sql,ps)
    return cursor.fetchall()
'''
   
def find_max_team_number_within_x_month(tournament_name, x=3):
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    max_team_no = "SELECT no FROM `tournament_teams` where tournament = %s and date >= %s order by no desc limit 1"
    ps = (tournament_name,utils.beforeXmonth(x))
    
    cursor.execute(max_team_no,ps)
    return cursor.fetchone()[0]

#查询出这个时间点最近的tournament中的所有组信息
def list_latest_tournament_teams(tournament_name,query_date):
    limit = find_max_team_number_within_x_month(tournament_name)
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    list_tournament_teams_sql = "SELECT * FROM `tournament_teams` where tournament = %s and date <= %s order by date desc , no asc limit "+ str(limit);
    ps = (tournament_name,query_date)
    
    cursor.execute(list_tournament_teams_sql,ps)
    return cursor.fetchall()

def find_latest_date_before_date(tournament_name,query_date):
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    list_tournament_teams_sql = "SELECT date FROM `tournament_teams` where tournament = %s and date <= %s order by date desc , no asc limit 1";
    ps = (tournament_name,query_date)
    
    cursor.execute(list_tournament_teams_sql,ps)
    return cursor.fetchone()

def list_latest_special_date_tournament_teams(tournament_name,special_date):
    query_date = find_latest_date_before_date(tournament_name,special_date)
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    list_tournament_teams_sql = "SELECT \
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
        `sdate`\
     FROM `tournament_teams` where tournament = %s and date = %s order by points desc ";
    ps = (tournament_name,query_date)
    
    cursor.execute(list_tournament_teams_sql,ps)
    return cursor.fetchall()



# xs = list_latest_special_date_tournament_teams('Italy - Serie A', utils.beforeXmonth(3))
# for x in xs:
#     print(x)
# print(find_latest_date_before_date('Italy - Serie A', utils.beforeXmonth(3)))

# print(find_max_team_number_within_x_month('Italy - Serie A',6))
# xs = (list_latest_tournament_teams('Italy - Serie A', utils.beforeXmonth(3)))
# for x in xs:
#     print(x)

# now = utils.date2sdate(datetime.now())
# ll = query_tournament_last_record_sdate('Liga NOS',298)
# print(ll[0])
# if ll is not None and \
#     now == ll[0]:
#     print(ll)
# else:
#     print('none or not match')
# xs = list_tournament_teams('Liga NOS',ll)
# for x in xs:
#     print(x)  
