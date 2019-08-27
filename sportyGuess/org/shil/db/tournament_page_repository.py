from datetime import datetime
from org.shil import utils

def insert_tournament_team(tournament,no,team_name,team_link,team_id,played,win,draw,loss,goals_for,goals_against,goals_difference,points):
    
    
    '''
    无论何时,有更新全更新,为了保持数据在取出时的一致性，
    比赛中,有可能有几个位置发生了变化,但某几个比如说7,没有变化,则不会被记录,造成取出时需要很多逻辑处理,比较麻烦,故每次都存
    
    exist = query_tournament_last_record_sdate(tournament,team_id)
    if played is not None:
        iplayed = int(played)
    else:
        iplayed = None

    if points is not None:
        ipoints = int(points)
    else:
        ipoints = None    
    insert_values = (iplayed,ipoints)
    
    if exist is not None \
        and exist == insert_values:
        
        # already exist this record, do not insert again
        print(tournament+" : " + team_id +" tournament nothing change, no need insert")
        return
    '''
    
    sdate = utils.date2sdate(datetime.now())
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
    query_last_data = "SELECT played , points FROM `tournament_teams` where tournament = %s and team_id = %s order by date desc limit 1"
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

# print(find_max_team_number_within_x_month('Italy - Serie A',6))

# xs = (list_latest_tournament_teams('Italy - Serie A', utils.beforeXmonth(3)))
# for x in xs:
#     print(x)

'''
now = sdate = utils.date2sdate(datetime.now())
ll = query_tournament_last_record_sdate('Liga NOS',298)
if ll is not None and \
    now == ll:
    print(ll)
else:
    print('none or not match')
xs = list_tournament_teams('Liga NOS',ll)
for x in xs:
    print(x)
'''  
