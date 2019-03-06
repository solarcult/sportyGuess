from datetime import datetime
from org.shil import utils

type_Summary = 'Summary'
type_Defensive = 'Defensive'
type_Offensive = 'Offensive'
view_Overall ='Overall'
view_Home = 'Home'
view_Away = 'Away'

def insert_team_statistics_summary(tournament,team_id,team_name,view,rating,apps,goals,shots_pg,possession, apass,aerials_won):

    exist = query_team_statistics_last_record_data(tournament, team_id, type_Summary, view)
    if apps is not None:
        iapps = int(apps)
    else:
        iapps = None
        
    if rating is not None:
        frating = float(rating)
    else:
        frating = None
    insert_values =(iapps,frating)
    if exist is not None \
        and insert_values == exist:
        # already exist this record, do not insert again
        print(tournament + "_" + str(team_id) +"_" + team_name +"_" + type_Summary +"_" + view +" nothing change, no need insert")
        return
    sdate = utils.date2sdate(datetime.now())
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
    
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(insert_sql,values)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid

def insert_team_statistics_defensive(tournament,team_id,team_name,view,rating,apps,shots_conceded_pg,tackles_pg,interceptions_pg,fouls_pg,offsides_pg):
    
    exist = query_team_statistics_last_record_data(tournament, team_id, type_Defensive, view)
    if apps is not None:
        iapps = int(apps)
    else:
        iapps = None
        
    if rating is not None:
        frating = float(rating)
    else:
        frating = None
    insert_values =(iapps,frating)
    if exist is not None \
        and insert_values == exist:
        # already exist this record, do not insert again
        print(tournament + "_" + str(team_id) +"_" + team_name +"_" + type_Defensive +"_" + view +" nothing change, no need insert")
        return
    sdate = utils.date2sdate(datetime.now())
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

    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(insert_sql,values)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid

def insert_team_statistics_offensive(tournament,team_id,team_name,view,rating,apps,shots_pg,shots_ot_pg,dribbles_pg,fouled_pg):
    
    exist = query_team_statistics_last_record_data(tournament, team_id, type_Offensive, view)
    if apps is not None:
        iapps = int(apps)
    else:
        iapps = None
        
    if rating is not None:
        frating = float(rating)
    else:
        frating = None
    insert_values =(iapps,frating)
    if exist is not None \
        and insert_values == exist:
        # already exist this record, do not insert again
        print(tournament + "_" + str(team_id) +"_" + team_name +"_" + type_Offensive +"_" + view +" nothing change, no need insert")
        return
    sdate = utils.date2sdate(datetime.now())
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
    
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(insert_sql,values)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid
    
    
def query_team_statistics_last_record_data(tournament,team_id,atype,view):
    query_last_data = "SELECT apps,rating FROM `team_statistics` where tournament = %s and team_id = %s and type = %s and view = %s order by date desc limit 1"
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(query_last_data,(tournament,team_id,atype,view))
    last_data = cursor.fetchone()
    if last_data is not None :
        return last_data
    else:
        return None


# x = query_team_statistics_last_record_data('League Cup', 560, 'Summary', 'Overall')
# print(x)
# y = (8,None)
# print(x==y)
# print(insert_team_statistics_summary('League Cup', 560,'abc', 'Overall', None, 8, 2.32, 2.65, None,None,None))