from datetime import datetime
from org.shil import utils
from org.shil.db import tournament_page_repository,tournament_name_convert_utils,match_fixtures_repository,team_statistics_repository,match_preview_repository


def total(tournament_name):
    tournament_in_sql_name = tournament_name_convert_utils.tournamentPage2Match(tournament_name)
    #查询出当前最新排名
    tournaments = tournament_page_repository.list_latest_tournament_teams(tournament_name,datetime.now());
    for tournament in tournaments:
        print(str(tournament[3]) + " : "+ str(tournament[6]))
    #查询出所有团队的比赛历史记录
    t_matches = match_fixtures_repository.list_all_tournament_matches_since_qdate(tournament_in_sql_name, utils.beforeXmonth(6))
    for o_match in t_matches:
        print(o_match)
#         查询比赛前的预分析信息
        preview_match = match_preview_repository.query_one_match_preview(o_match[0])
        home_missing = preview_match[20]
#         查询每个队伍的数据详情
        home_t_summary_overall = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, o_match[3], team_statistics_repository.type_Summary, team_statistics_repository.view_Overall, o_match[2])
#         print(home_t_summary_overall)
        home_t_summary_home = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, o_match[3], team_statistics_repository.type_Summary, team_statistics_repository.view_Home, o_match[2])
        home_t_offensive_home = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, o_match[3], team_statistics_repository.type_Offensive, team_statistics_repository.view_Home, o_match[2])
        home_t_defensive_home = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, o_match[3], team_statistics_repository.type_Defensive, team_statistics_repository.view_Home, o_match[2])
        print(home_t_offensive_home)

#         if(home_t_offensive_home is None):
#             print('home')
#             print(o_match[0])
#             print(o_match[3])
#             print(o_match[2])
#             print("----------")

        away_t_summary_overall = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, o_match[5], team_statistics_repository.type_Summary, team_statistics_repository.view_Overall, o_match[2])
        print(away_t_summary_overall)
        away_t_summary_home = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, o_match[5], team_statistics_repository.type_Summary, team_statistics_repository.view_Away, o_match[2])
        away_t_offensive_home = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, o_match[5], team_statistics_repository.type_Offensive, team_statistics_repository.view_Away, o_match[2])
        away_t_defensive_home = team_statistics_repository.query_team_statistic_last_record_data_before_date(tournament_in_sql_name, o_match[5], team_statistics_repository.type_Defensive, team_statistics_repository.view_Away, o_match[2])
#         print(away_t_defensive_home)

#         if(away_t_defensive_home is None):
#             print("away")
#             print(o_match[0])
#             print(o_match[5])
#             print(o_match[2])
#             print("----------")

total("Italy - Serie A")