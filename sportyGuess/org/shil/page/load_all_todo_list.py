import json,time
from datetime import datetime
from org.shil.db import fetch_url_repository
from org.shil.page import tournament_page, team_page, team_fixtures_page,\
    player_fixtures_page, match_preview_page


def process_page_detail(atype,params,priority):
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
            player_fixtures_page.process_player_fixtures(params,priority)
            return
        if atype == fetch_url_repository.type_MatchPreview:
            match_preview_page.process_match_preview(params,priority)
            return
        print('where fuck am i ?')
        
    except Exception as e:
        print('sorry something has problem maybe network is too slow to load the content , please try next url : ')
        print(e)


'''

everything has a beginning has its ending

'''

xs = fetch_url_repository.query_todo_fetch_urls()

while xs is not None:
    
    for x in xs:
        starttime = time.time()
        process_page_detail(x[0], json.loads(str(x[1])),x[2])
        print(str(datetime.now()) + " done with seconds :" + str(time.time()-starttime))
    
    xs = fetch_url_repository.query_todo_fetch_urls()
    
    


