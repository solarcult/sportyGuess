from datetime import datetime
from org.shil import utils
import json

type_Tournament = 'tournament' #tournament_page
type_TeamHome = 'team_home' #team_page
type_TeamFixtures  = 'team_fixtures'
type_PlayerFixtures = 'player_fixtures'
type_MatchPreview = 'match_preview'

status_TODO = 'TODO'
status_Done = 'Done'
status_SomethingBlankOrIssue = 'Something_blank_or_issue'


def insert_fetch_url(url,atype,params):
    sdate = utils.date2sdate(datetime.now())
    exist = query_fetch_url_last_record_sdate(url)
    if exist is not None and sdate == exist:
        # already exist this record, do not insert again
        print(atype + "_" + url +" fetch url already exist, no need insert")
        return
    
    insert_sql ="\
    INSERT INTO `fetch_url` (\
        `url`,\
        `type`,\
        `date`,\
        `status`,\
        `params_json`,\
        `sdate`)\
    VALUES \
        (%s,%s,%s,%s,%s,%s) "

    values = (url,atype,datetime.now(),status_TODO,json.dumps(params),sdate)
    
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(insert_sql,values)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid

def update_last_record_of_url_status(url,errors):
    
    sdate = query_fetch_url_last_record_sdate(url)
    status = status_Done
    if len(errors) > 0 :
        status = status_SomethingBlankOrIssue
    
    update_sql = " UPDATE fetch_url SET status = %s , error_records = %s , sdate = %s  WHERE url = %s and sdate = %s "
    
    values = (status,json.dumps(errors),utils.date2sdate(datetime.now()),url,sdate)
    
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(update_sql,values)
    nid = cursor.lastrowid
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return nid

def query_fetch_url_last_record_sdate(url):
    query_last_date = "SELECT sdate FROM `fetch_url` where url = %s order by date desc limit 1"
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(query_last_date,(url,))
    sdates = cursor.fetchone()
    if sdates is not None :
        return sdates[0]
    else:
        return None
    
    
def query_todo_fetch_urls():
    query_todo_sql ="SELECT type, params_json FROM fetch_url WHERE status = 'TODO' "
    cnx = utils.get_mysql_connector()
    cursor = cnx.cursor()
    cursor.execute(query_todo_sql)
    fetches = cursor.fetchall()
    if fetches is not None :
        return fetches    
    else:
        return None
    
# insert_fetch_url("12345", type_TeamHome, "goodluck")
# print(query_fetch_url_last_record_sdate("12345"))
# errors = []
# update_last_record_of_url_status("12345", errors)
# print(query_todo_fetch_urls())
