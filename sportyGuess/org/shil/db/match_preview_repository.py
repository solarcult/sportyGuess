'''
Created on 2019-Mar-06 22:59

@author: shil

'''

from org.shil import utils
from org.shil.entity.match_preview_entity import match_preview_entity
import json

def insert_match_preview(match_preview_entity):
    exist = query_one_match_preview(match_preview_entity.match_id)
    if exist is not None \
        and exist == int(match_preview_entity.match_id):
        print(match_preview_entity.match_id + " preview already exist, no need insert")
        return
    
    insert_sql = "\
    INSERT INTO match_previews ( \
        `match_id`,\
        `date`,\
        `home_team_id`,\
        `home_team_name`,\
        `home_goals`,\
        `home_assists`,\
        `home_average_ratings`,\
        `home_shots_pg`,\
        `home_aerial_duel_success`,\
        `home_dribbles_pg`,\
        `home_tackles_pg`,\
        `away_team_id`,\
        `away_team_name`,\
        `away_goals`,\
        `away_assists`,\
        `away_average_ratings`,\
        `away_shots_pg`,\
        `away_aerial_duel_success`,\
        `away_dribbles_pg`,\
        `away_tackles_pg`,\
        `home_missing_players`,\
        `away_missing_players`,\
        `home_players`,\
        `away_players`)\
    VALUES\
        (%(match_id)s,\
        %(date)s,\
        %(home_team_id)s,\
        %(home_team_name)s,\
        %(home_goals)s,\
        %(home_assists)s,\
        %(home_average_ratings)s,\
        %(home_shots_pg)s,\
        %(home_aerial_duel_success)s,\
        %(home_dribbles_pg)s,\
        %(home_tackles_pg)s,\
        %(away_team_id)s,\
        %(away_team_name)s,\
        %(away_goals)s,\
        %(away_assists)s,\
        %(away_average_ratings)s,\
        %(away_shots_pg)s,\
        %(away_aerial_duel_success)s,\
        %(away_dribbles_pg)s,\
        %(away_tackles_pg)s,\
        %(home_missing_players)s,\
        %(away_missing_players)s,\
        %(home_players)s,\
        %(away_players)s )"
    
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(insert_sql,match_preview_entity.__dict__)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid

def query_one_match_preview(match_id):
    query_one_sql =" SELECT * FROM match_previews WHERE match_id = %s"
    
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(query_one_sql,(match_id,))
    one_record = cursor.fetchone()
    if one_record is not None :
        return one_record
    else:
        return None

print(query_one_match_preview(1281313)[21])
print(query_one_match_preview(1281313)[20])
h = json.loads(query_one_match_preview(1281313)[20])
print(type(h))
for o in h.keys():
    print(o)
    print(h[o])
    print("----------------")