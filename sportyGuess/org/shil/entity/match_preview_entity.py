class match_preview_entity:
    match_id = None
    home_team_id = None
    home_goals = None
    home_assists = None
    home_average_ratings = None
    home_shots_pg = None
    home_aerial_duel_success = None
    home_dribbles_pg = None
    home_tackles_pg = None
    away_team_id = None
    away_goals = None
    away_assists = None
    away_average_ratings = None
    away_shots_pg = None
    away_aerial_duel_success = None
    away_dribbles_pg = None
    away_tackles_pg = None
    home_missing_players = None
    away_missing_players = None
    home_players = None
    away_players = None
    
    
    def print_self(self):
        print(self.__dict__)