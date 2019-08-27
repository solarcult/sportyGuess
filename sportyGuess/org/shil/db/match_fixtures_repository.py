'''
Created on 2019-Mar-05

@author: shil

'''

from org.shil import utils
from org.shil.entity.match_fixture_entity import match_fixture_entity

def insert_match_fixture(match_fixture_entity):
    
    exist = query_one_match_fixture_entity(match_fixture_entity.match_id)
    
    if exist is not None \
        and exist == match_fixture_entity:
        print("match " + match_fixture_entity.match_id + " fixture already exist, no need insert")
        return
    
    insert_sql ="\
    INSERT INTO match_fixtures (\
        match_id,\
        tournament,\
        date,\
        home_team_id,\
        home_team_name,\
        away_team_id,\
        away_team_name,\
        full_time_home_goals,\
        full_time_away_goals,\
        result,\
        sdate)\
    VALUES \
        (%(match_id)s,\
        %(tournament)s,\
        %(date)s,\
        %(home_team_id)s,\
        %(home_team_name)s,\
        %(away_team_id)s,\
        %(away_team_name)s,\
        %(full_time_home_goals)s,\
        %(full_time_away_goals)s,\
        %(result)s,\
        %(sdate)s )"
        
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(insert_sql,match_fixture_entity.__dict__)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid

def query_match_id(home_team_id,away_team_id,sdate):
    query_one_match_id = "\
    SELECT match_id \
    FROM match_fixtures\
    WHERE \
        home_team_id = %s and away_team_id = %s and sdate= %s" 
    
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(query_one_match_id,(home_team_id,away_team_id,sdate))
    one_record = cursor.fetchone()
    if one_record is not None :
        return one_record[0]
    else:
        return None        

def query_one_match_fixture_entity(match_id):
    query_one_match_id = "\
    SELECT match_id, \
        tournament,\
        date,\
        home_team_id,\
        home_team_name,\
        away_team_id,\
        away_team_name,\
        full_time_home_goals,\
        full_time_away_goals,\
        half_time_home_goals,\
        half_time_away_goals,\
        result,\
        sdate\
    FROM match_fixtures\
    WHERE \
        match_id = %s" 
    
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(query_one_match_id,(match_id,))
    one_record = cursor.fetchone()
    if one_record is not None :
        match_fixture = match_fixture_entity()
        match_fixture.match_id = one_record[0]
        match_fixture.tournament = one_record[1]
        match_fixture.date = one_record[2]
        match_fixture.home_team_id = one_record[3]
        match_fixture.home_team_name = one_record[4]
        match_fixture.away_team_id = one_record[5]
        match_fixture.away_team_name = one_record[6]
        match_fixture.full_time_home_goals = one_record[7]
        match_fixture.full_time_away_goals = one_record[8]
        match_fixture.half_time_home_goals = one_record[9]
        match_fixture.half_time_away_goals = one_record[10]
        match_fixture.result = one_record[11]
        match_fixture.sdate = one_record[12]
        return match_fixture
    else:
        return None

def list_all_tournament_matches_since_qdate(tournament_name,query_date):
    list_all_tournament_matches_since_qdate = "\
    SELECT match_id, \
        tournament,\
        date,\
        home_team_id,\
        home_team_name,\
        away_team_id,\
        away_team_name,\
        full_time_home_goals,\
        full_time_away_goals,\
        result,\
        sdate\
    FROM match_fixtures\
    WHERE \
        tournament = %s \
        and date >= %s \
        order by date desc" 
    
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(list_all_tournament_matches_since_qdate,(tournament_name,query_date))
    return cursor.fetchall()
    
# xs = list_all_tournament_matches_since_qdate('Serie A', utils.beforeXmonth(6))
# for x in xs:
#     print(x)