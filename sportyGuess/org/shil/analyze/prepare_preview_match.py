import json
from datetime import datetime
from org.shil import utils
from org.shil.db import tournament_page_repository,tournament_name_convert_utils,match_fixtures_repository,team_statistics_repository,match_preview_repository,squad_statistics_repository


def total(tournament_name):
    tournament_in_sql_name = tournament_name_convert_utils.tournamentPage2Match(tournament_name)
    #查询出当前最新排名
    tournament_teams = tournament_page_repository.list_latest_special_date_tournament_teams(tournament_name,datetime.now());
    for tournament_team in tournament_teams:
        print(str(tournament_team[2]) + " : "+ str(tournament_team[5]))
    #查询出所有团队的比赛历史记录
    t_matches = match_fixtures_repository.list_all_tournament_matches_since_qdate(tournament_in_sql_name, utils.beforeXmonth(6))
    for o_match in t_matches:
        print(o_match)
        m_id = o_match[0]
        m_date = o_match[2]
        home_t_id = o_match[3]
        away_t_id = o_match[5]
#         查询比赛前的预分析信息
        preview_match = match_preview_repository.query_one_match_preview(m_id)
        
#         查询每个队伍的数据详情
        home_t_summary_overall = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, home_t_id, team_statistics_repository.type_Summary, team_statistics_repository.view_Overall, m_date)
#         print(home_t_summary_overall)
        home_t_summary_home = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, home_t_id, team_statistics_repository.type_Summary, team_statistics_repository.view_Home, m_date)
        
        home_t_offensive_overall = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, home_t_id, team_statistics_repository.type_Offensive, team_statistics_repository.view_Overall, m_date)
        home_t_offensive_home = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, home_t_id, team_statistics_repository.type_Offensive, team_statistics_repository.view_Home, m_date)
        
        home_t_defensive_overall = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, home_t_id, team_statistics_repository.type_Defensive, team_statistics_repository.view_Overall, m_date)
        home_t_defensive_home = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, home_t_id, team_statistics_repository.type_Defensive, team_statistics_repository.view_Home, m_date)
#         print(home_t_offensive_home)
        home_missing_map = json.loads(preview_match[20])
        print(home_missing_map)
        home_squads_overall = squad_statistics_repository.list_team_squad_statistics_latest_sepcial_date(tournament_in_sql_name, home_t_id, team_statistics_repository.type_Summary,team_statistics_repository.view_Overall, m_date)
        home_squads_home = squad_statistics_repository.list_team_squad_statistics_latest_sepcial_date(tournament_in_sql_name, home_t_id, team_statistics_repository.type_Summary,team_statistics_repository.view_Home, m_date)
        
        
        away_t_summary_overall = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, away_t_id, team_statistics_repository.type_Summary, team_statistics_repository.view_Overall, m_date)
#         print(away_t_summary_overall)
        away_t_summary_home = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, away_t_id, team_statistics_repository.type_Summary, team_statistics_repository.view_Away, m_date)
        
        away_t_offensive_overall = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, away_t_id, team_statistics_repository.type_Offensive, team_statistics_repository.view_Overall, m_date)
        away_t_offensive_home = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, away_t_id, team_statistics_repository.type_Offensive, team_statistics_repository.view_Away, m_date)
        
        away_t_defensive_overall = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, away_t_id, team_statistics_repository.type_Defensive, team_statistics_repository.view_Overall, m_date)
        away_t_defensive_home = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, away_t_id, team_statistics_repository.type_Defensive, team_statistics_repository.view_Away, m_date)
#         print(away_t_defensive_home)
        away_missing_map = json.loads(preview_match[21])
        print(away_missing_map)
        away_squads_overall = squad_statistics_repository.list_team_squad_statistics_latest_sepcial_date(tournament_in_sql_name, away_t_id, team_statistics_repository.type_Summary,team_statistics_repository.view_Overall, m_date)
        away_squads_away = squad_statistics_repository.list_team_squad_statistics_latest_sepcial_date(tournament_in_sql_name, away_t_id, team_statistics_repository.type_Summary,team_statistics_repository.view_Away, m_date)

        print('---------')

def retrieveTournamentTeamData(tournament_name,query_date):
    tournament_teams = tournament_page_repository.list_latest_special_date_tournament_teams(tournament_name,query_date);
    tournament_team_map = {}
    for tournament_team in tournament_teams:
        print(str(tournament_team[2]) + " : "+ str(tournament_team[5]))
        tournament_team_map.setdefault(tournament_team[5], tournament_team)
    return tournament_team_map

# total("Italy - Serie A")

# x = retrieveTournamentTeamData("Italy - Serie A", utils.beforeXmonth(4))
# for k in x.keys():
#     print(k)
#     print(x.get(k))
    