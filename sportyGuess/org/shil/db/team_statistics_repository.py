from datetime import datetime
from org.shil import utils

type_Summary = 'Summary'
type_Defensive = 'Defensive'
type_Offensive = 'Offensive'
view_Overall ='Overall'
view_Home = 'Home'
view_Away = 'Away'

def insert_team_statistics_summary(tournament,team_id,team_name,view,rating,apps,goals,shots_pg,possession, apass,aerials_won):
    
    sdate = (datetime.now().strftime('%d-%m-%Y'))
    exist = query_team_statistics_last_record_sdate(tournament, team_id, type_Summary, view)
    if exist is not None \
        and sdate == exist:
        # already exist this record, do not insert again
        print(tournament + "_" + team_id +"_" + team_name +"_" + type_Summary +"_" + view +" already exsit, no need insert")
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
        
    values =(team_id,team_name,datetime.now(),type_Summary,view,tournament,rating,apps,goals,shots_pg,possession,apass,aerials_won,sdate)
    
    cnx = utils.getMysqlConnector()
    cursor = cnx.cursor()
    cursor.execute(insert_sql,values)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid

def insert_team_statistics_defensive(tournament,team_id,team_name,view,rating,apps,shots_conceded_pg,tackles_pg,interceptions_pg,fouls_pg,offsides_pg):
    sdate = (datetime.now().strftime('%d-%m-%Y'))
    exist = query_team_statistics_last_record_sdate(tournament, team_id, type_Defensive, view)
    if exist is not None \
        and sdate == exist:
        # already exist this record, do not insert again
        print(tournament + "_" + team_id +"_" + team_name +"_" + type_Defensive +"_" + view +" already exsit, no need insert")
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
        `shots_conceded_pg`,\
        `tackles_pg`,\
        `interceptions_pg`,\
        `fouls_pg`,\
        `offsides_pg`,\
        `sdate`)\
    VALUES \
        ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    values =(team_id,team_name,datetime.now(),type_Defensive,view,tournament,rating,apps,shots_conceded_pg,tackles_pg,interceptions_pg,fouls_pg,offsides_pg,sdate)

    cnx = utils.getMysqlConnector()
    cursor = cnx.cursor()
    cursor.execute(insert_sql,values)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid

def insert_team_statistics_offensive(tournament,team_id,team_name,view,rating,apps,shots_pg,shots_ot_pg,dribbles_pg,fouled_pg):
    sdate = (datetime.now().strftime('%d-%m-%Y'))
    exist = query_team_statistics_last_record_sdate(tournament, team_id, type_Offensive, view)
    if exist is not None \
        and sdate == exist:
        # already exist this record, do not insert again
        print(tournament + "_" + team_id +"_" + team_name +"_" + type_Offensive +"_" + view +" already exsit, no need insert")
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
        `shots_pg`,\
        `shots_ot_pg`,\
        `dribbles_pg`,\
        `fouled_pg`,\
        `sdate`)\
    VALUES \
        ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    values =(team_id,team_name,datetime.now(),type_Offensive,view,tournament,rating,apps,shots_pg,shots_ot_pg,dribbles_pg,fouled_pg,sdate)
    
    cnx = utils.getMysqlConnector()
    cursor = cnx.cursor()
    cursor.execute(insert_sql,values)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid
    
    
def query_team_statistics_last_record_sdate(tournament,team_id,atype,view):
    query_last_date = "SELECT sdate FROM `team_statistics` where tournament = %s and team_id = %s and type = %s and view = %s order by date desc limit 1"
    cnx = utils.getMysqlConnector()
    cursor = cnx.cursor()
    cursor.execute(query_last_date,(tournament,team_id,atype,view))
    sdates = cursor.fetchone()
    if sdates is not None :
        return sdates[0]
    else:
        return None

