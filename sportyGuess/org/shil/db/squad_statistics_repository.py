from datetime import datetime
from org.shil import utils
from org.shil.db import team_statistics_repository

def insert_squad_statistics_summary(tournament,team_id,view,player_id,player_name,rating,cm,apps,mins,goals,assists,shots_pg,apass,aerials_won,man_ot_match):
    
    exist = query_squad_statistics_last_record_data(tournament, team_id, player_id, team_statistics_repository.type_Summary, view)
    if mins is not None:
        imins = int(mins)
    else:
        imins = None
    if rating is not None:
        frating = float(rating)
    else:
        frating = None
    insert_values =(imins,frating)
    
    if exist is not None \
        and insert_values == exist:
        # already exist this record, do not insert again
        print(tournament + "_"+ team_id+ "_" + player_id +"_" + player_name +"_" + team_statistics_repository.type_Summary +"_" + view +" squad nothing change, no need insert")
        return
    
    sdate = utils.date2sdate(datetime.now())
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
    
    
def query_squad_statistics_last_record_data(tournament,team_id,player_id,atype,view):
    query_last_data = "SELECT mins,rating FROM `squad_statistics` where tournament = %s and team_id = %s and player_id = %s and type = %s and view = %s order by date desc limit 1"
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(query_last_data,(tournament,team_id,player_id,atype,view))
    last_date = cursor.fetchone()
    if last_date is not None :
        return last_date
    else:
        return None