from datetime import datetime
from org.shil import utils

type_Summary = 'Summary'
type_Defensive = 'Defensive'
type_Offensive = 'Offensive'
view_Overall ='Overall'
view_Home = 'Home'
view_Away = 'Away'

def insert_team_statistics_summary(tournament,team_id,team_name,view,rating,apps,goals,shots_pg,possession, apass,aerials_won):
    
    exist = query_team_statistics_last_record_date(tournament, team_id, type_Summary, view)
    if exist is not None:
        # already exist this record, do not insert again
        print(tournament + "_" + team_id +"_" + type_Summary +"_" + view +" already exsit, no need insert")
        return
    
    insert_sql ="\
    INSERT INTO `team_statistics` (\
        `team_id`,\
        `team_name`,\
        `date`,\
        `type`,\
        `view`,\
        `tournament`,\
        `rating`,\
        `apps`,\
        `goals`,\
        `shots_pg`,\
        `possession`,\
        `pass`,\
        `aerials_won`,\
        `sdate`)\
    VALUES \
        ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
    sdate = (datetime.now().strftime('%d-%m-%Y'))
        
def query_team_statistics_last_record_date(tournament,team_id,atype,view):
    query_last_date = "SELECT date FROM `team_statistics` where tournament = %s and team_id = %s and type = %s and view = %s order by date desc limit 1"
    cnx = utils.getMysqlConnector()
    cursor = cnx.cursor()
    cursor.execute(query_last_date,(tournament,team_id,atype,view))
    return cursor.fetchone()[0]


