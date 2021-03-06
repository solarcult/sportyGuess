import json,time
from datetime import datetime
from org.shil import utils
from org.shil.db import fetch_url_repository
from org.shil.page import tournament_page, team_page, team_fixtures_page, player_fixtures_page, match_preview_page


def process_page_detail(atype,params,priority,process='GoOd'):
    try:
        if atype == fetch_url_repository.type_Tournament:
            tournament_page.process_tournament_page(params[0], params[1],priority)
            return
        if atype == fetch_url_repository.type_TeamHome:
            team_page.process_team_page(params,priority)
            return
        if atype == fetch_url_repository.type_TeamFixtures:
            team_fixtures_page.process_team_fixtures(params,priority)
            return
        if atype == fetch_url_repository.type_PlayerFixtures:
            player_fixtures_page.process_player_fixtures(params)
            return
        if atype == fetch_url_repository.type_MatchPreview:
            match_preview_page.process_match_preview(params)
            return
        print('where fuck am i ?')
        
    except Exception as e:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print('sorry something has problem maybe network is too slow to load the content , please try next url : ')
        print(e)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        errors = []
        errors.append(str(e))
        if atype == fetch_url_repository.type_Tournament:
            if process == fetch_url_repository.status_Error:
                try:
                    fetch_url_repository.update_last_record_of_url_status(params[0], errors)
                except:
                    did = fetch_url_repository.query_fetch_url_last_Error_record_sdate(params[0])[1]
                    fetch_url_repository.delete_id(did)
            else:
                fetch_url_repository.mark_url_errors(params[0], errors)
        else:
            if process == fetch_url_repository.status_Error:
                try:
                    fetch_url_repository.update_last_record_of_url_status(params, errors)
                except:
                    did = fetch_url_repository.query_fetch_url_last_Error_record_sdate(params)[1]
                    fetch_url_repository.delete_id(did)
            else:
                fetch_url_repository.mark_url_errors(params, errors)
'''

everything has a beginning has its ending

'''

xs = fetch_url_repository.query_todo_fetch_urls()

while xs is not None and len(xs) > 0:
    
    for x in xs:
        starttime = time.time()
        process_page_detail(x[0], json.loads(str(x[1])),x[2])
        print(str(datetime.now()) + " done with seconds :" + str(time.time()-starttime))
    
    xs = fetch_url_repository.query_todo_fetch_urls()
    print(xs)
    
utils.browser_implicitly_wait = 30
es = fetch_url_repository.query_error_fetch_urls()

for e in es:
    starttime = time.time()
    process_page_detail(e[0], json.loads(str(e[1])),e[2],fetch_url_repository.status_Error)
    print(str(datetime.now()) + " done with seconds :" + str(time.time()-starttime))
    

