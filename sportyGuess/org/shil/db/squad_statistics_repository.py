from datetime import datetime
from org.shil import utils
from org.shil.db import team_statistics

def insert_squad_statistics_summary(tournament,view,player_id,player_name,rating,cm,apps,mins,goals,assists,shots_pg,apass,aerials_won,man_ot_match):
    sdate = (datetime.now().strftime('%d-%m-%Y'))
    exist = query_squad_statistics_last_record_sdate(tournament, player_id, team_statistics.type_Summary, view)
    if exist is not None \
        and sdate == exist:
        # already exist this record, do not insert again
        print(tournament + "_" + player_id +"_" + player_name +"_" + team_statistics.type_Summary +"_" + view +" already exsit, no need insert")
        return
    
    insert_sql ="\
    INSERT INTO `squad_statistics` (\
        `tournament`,\
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
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
    values=(tournament,team_statistics.type_Summary,view,player_id,player_name,datetime.now(),rating,cm,apps,mins,goals,assists,shots_pg,apass,aerials_won,man_ot_match,sdate)
    
    cnx = utils.getMysqlConnector()
    cursor = cnx.cursor()
    cursor.execute(insert_sql,values)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid
    
    
def query_squad_statistics_last_record_sdate(tournament,player_id,atype,view):
    query_last_date = "SELECT sdate FROM `squad_statistics` where tournament = %s and player_id = %s and type = %s and view = %s order by date desc limit 1"
    cnx = utils.getMysqlConnector()
    cursor = cnx.cursor()
    cursor.execute(query_last_date,(tournament,player_id,atype,view))
    sdates = cursor.fetchone()
    if sdates is not None :
        return sdates[0]
    else:
        return None