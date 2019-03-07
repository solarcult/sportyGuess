import json
from org.shil.db import fetch_url_repository
from org.shil.page import tournament_page, team_page, team_fixtures_page,\
    player_fixtures_page, match_preview_page


def process_page_detail(atype,params):
    try:
        if atype == fetch_url_repository.type_Tournament:
            tournament_page.process_tournament_page(params[0], params[1])
            return
        if atype == fetch_url_repository.type_TeamHome:
            team_page.process_team_page(params)
            return
        if atype == fetch_url_repository.type_TeamFixtures:
            team_fixtures_page.process_team_fixtures(params)
            return
        if atype == fetch_url_repository.type_PlayerFixtures:
            player_fixtures_page.process_player_fixtures(params)
            return
        if atype == fetch_url_repository.type_MatchPreview:
            match_preview_page.process_match_preview(params)
            return
        print('where fuck am i ?')
        
    except Exception as e:
        print('sorry something has problem maybe network is too slow to load the content , please try next url : '+e)


'''

everything has a beginning has its ending

'''

xs = fetch_url_repository.query_todo_fetch_urls()

while xs is not None:
    
    for x in xs:
        process_page_detail(x[0], json.loads(str(x[1])))
    
    xs = fetch_url_repository.query_todo_fetch_urls()
    
    


