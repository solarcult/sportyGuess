from datetime import datetime
from org.shil import utils
from org.shil.db import team_statistics_repository

def insert_squad_statistics_summary(tournament,team_id,view,player_id,player_name,rating,cm,apps,mins,goals,assists,shots_pg,apass,aerials_won,man_ot_match):
    
    sdate = utils.date2sdate(datetime.now())
    exist = query_squad_statistics_last_record_sdate(tournament, team_id, player_id, team_statistics_repository.type_Summary, view)
    
    if exist is not None \
        and sdate == exist:
        # already exist this record, do not insert again
        print(sdate +"_" + tournament + "_"+ team_id+ "_" + player_id +"_" + player_name +"_" + team_statistics_repository.type_Summary +"_" + view +" squad has been inserted today, no need insert")
        return
    
    insert_sql ="\
    INSERT INTO `squad_statistics` (\
        `tournament`,\
        `team_id`,\
        `type`,\
        `view`,\
        `player_id`,\
        `player_name`,\
        `date`,\
        `rating`,\
        `cm`,\
        `apps`,\
        `mins`,\
        `goals`,\
        `assists`,\
        `shots_pg`,\
        `pass`,\
        `aerials_won`,\
        `man_ot_match`,\
        `sdate`) \
    VALUES \
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
    values=(tournament,team_id,team_statistics_repository.type_Summary,view,player_id,player_name,datetime.now(),rating,cm,apps,mins,goals,assists,shots_pg,apass,aerials_won,man_ot_match,sdate)
    
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(insert_sql,values)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid
    
    
def query_squad_statistics_last_record_sdate(tournament,team_id,player_id,atype,view,before_date = datetime.now()):
    query_last_data = "SELECT sdate FROM `squad_statistics` where tournament = %s and team_id = %s and player_id = %s and type = %s and view = %s and date <= %s order by date desc limit 1"
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(query_last_data,(tournament,team_id,player_id,atype,view,before_date))
    last_date = cursor.fetchone()
    if last_date is not None :
        return last_date[0]
    else:
        return None

def query_team_squad_last_record_sdate(tournament,team_id,atype,view,before_date = datetime.now()):
    query_last_data = "SELECT sdate FROM `squad_statistics` where tournament = %s and team_id = %s and type = %s and view = %s and date <= %s order by date desc limit 1"
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(query_last_data,(tournament,team_id,atype,view,before_date))
    last_date = cursor.fetchone()
    if last_date is not None :
        return last_date[0]
    else:
        return None
    
def list_team_squad_statistics_latest_sepcial_date(tournament,team_id,atype,view,sepcial_date):
    sepcial_sdate = query_team_squad_last_record_sdate(tournament,team_id,atype,view,sepcial_date)
    query_datas = "SELECT\
        `player_id`,\
        `player_name`,\
        `date`,\
        `rating`,\
        `cm`,\
        `apps`,\
        `mins`,\
        `goals`,\
        `assists`,\
        `shots_pg`,\
        `pass`,\
        `aerials_won`,\
        `man_ot_match`,\
        FROM `squad_statistics` where tournament = %s and team_id = %s and type = %s and view = %s and sdate = %s order by rating desc"
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(query_datas,(tournament,team_id,atype,view,sepcial_sdate))
    return cursor.fetchall()

# sdate = query_team_squad_last_record_sdate('La Liga',62,team_statistics_repository.type_Summary,team_statistics_repository.view_Overall,utils.beforeXmonth(4))
# print(sdate)
# ts = list_team_squad_statistics_latest_sepcial_date('La Liga',62,team_statistics_repository.type_Summary,team_statistics_repository.view_Overall,utils.beforeXmonth(4))
# for t in ts:
#     print(t)