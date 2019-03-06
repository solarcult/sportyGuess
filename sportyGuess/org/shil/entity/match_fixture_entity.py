class match_fixture_entity:
    match_id = None
    tournament = None
    date = None
    home_team_id = None
    home_team_name = None
    away_team_id = None
    away_team_name = None
    full_time_home_goals = None
    full_time_away_goals = None
    half_time_home_goals = None
    half_time_away_goals = None
    result = None
    sdate = None

    def __eq__(self,other):
        if self is None \
            or other is None:
            return False
#         return self.__dict__ == other.__dict__
        return str(self.match_id) == str(other.match_id) \
             and str(self.home_team_id) == str(other.home_team_id) \
             and str(self.away_team_id) == str(other.away_team_id) \
             and str(self.full_time_home_goals) == str(other.full_time_home_goals) \
             and str(self.full_time_away_goals) == str(other.full_time_away_goals) \
             and str(self.sdate) == str(other.sdate)
    
    def print_self(self):
        print(self.__dict__)
    

# a = match_fixture_entity()
# a.match_id = 1274003
# 
# b = match_fixture_entity()
# b.match_id = 1274003
# 
# print(a == b)