CREATE TABLE `fetch_url` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `type` varchar(45) NOT NULL COMMENT 'tournament,team_home,team_fixtures,player_fixtures,match_preview',
  `date` date NOT NULL,
  `status` varchar(45) NOT NULL COMMENT 'todo,done,something_blank_or_issue',
  `params_json` varchar(255) NOT NULL,
  `sdate` varchar(45) NOT NULL,
  `error_records` varchar(511) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `onlyone` (`url`,`sdate`,`type`)
) ENGINE=InnoDB AUTO_INCREMENT=149 DEFAULT CHARSET=utf8

CREATE TABLE `match_fixtures` (
  `match_id` bigint(20) NOT NULL COMMENT 'same as whoscored matches id',
  `tournament` varchar(45) NOT NULL,
  `date` date NOT NULL,
  `home_team_id` int(11) NOT NULL COMMENT 'same as whoscored team id',
  `home_team_name` varchar(45) NOT NULL,
  `away_team_id` int(11) NOT NULL COMMENT 'same as whoscored team id',
  `away_team_name` varchar(45) NOT NULL,
  `full_time_home_goals` int(11) NOT NULL,
  `full_time_away_goals` int(11) NOT NULL,
  `half_time_home_goals` int(11) DEFAULT NULL,
  `half_time_away_goals` int(11) DEFAULT NULL,
  `result` varchar(12) NOT NULL,
  `sdate` varchar(45) NOT NULL COMMENT '字符串时间',
  PRIMARY KEY (`match_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='队伍具体比赛数据'

CREATE TABLE `match_previews` (
  `match_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `home_team_id` int(11) NOT NULL,
  `home_team_name` varchar(45) NOT NULL,
  `home_goals` int(11) NOT NULL,
  `home_assists` int(11) NOT NULL,
  `home_average_ratings` double NOT NULL,
  `home_shots_pg` double NOT NULL,
  `home_aerial_duel_success` double NOT NULL,
  `home_dribbles_pg` double NOT NULL,
  `home_tackles_pg` double NOT NULL,
  `away_team_id` int(11) NOT NULL,
  `away_team_name` varchar(45) NOT NULL,
  `away_goals` int(11) NOT NULL,
  `away_assists` int(11) NOT NULL,
  `away_average_ratings` double NOT NULL,
  `away_shots_pg` double NOT NULL,
  `away_aerial_duel_success` double NOT NULL,
  `away_dribbles_pg` double NOT NULL,
  `away_tackles_pg` double NOT NULL,
  `home_missing_players` varchar(511) DEFAULT NULL,
  `away_missing_players` varchar(511) DEFAULT NULL,
  `home_players` varchar(2046) DEFAULT NULL,
  `away_players` varchar(2046) DEFAULT NULL,
  PRIMARY KEY (`match_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE TABLE `player_match_behavior` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `match_id` varchar(45) NOT NULL,
  `player_id` int(11) NOT NULL,
  `player_nick_name` varchar(45) NOT NULL,
  `mins` int(11) DEFAULT NULL,
  `rating_in_this_match` double DEFAULT NULL COMMENT 'Rating in this match',
  `sdate` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `onlyone` (`match_id`,`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='比赛中参与的人员和rating数据'

CREATE TABLE `squad_statistics` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tournament` varchar(45) NOT NULL,
  `team_id` int(11) NOT NULL,
  `type` varchar(45) NOT NULL,
  `view` varchar(45) NOT NULL,
  `player_id` int(11) NOT NULL COMMENT 'same as whoscored player id',
  `player_name` varchar(45) NOT NULL,
  `date` date NOT NULL,
  `rating` double NOT NULL,
  `cm` int(11) DEFAULT NULL,
  `apps` varchar(45) DEFAULT NULL,
  `mins` int(11) DEFAULT NULL,
  `goals` int(11) DEFAULT NULL,
  `assists` int(11) DEFAULT NULL,
  `shots_pg` double DEFAULT NULL,
  `pass` double DEFAULT NULL,
  `aerials_won` double DEFAULT NULL,
  `man_ot_match` int(11) DEFAULT NULL,
  `sdate` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `onlyone` (`tournament`,`type`,`view`,`player_id`,`sdate`,`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='球员数据根据多维度和时间进行划分'

CREATE TABLE `team_statistics` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `team_id` int(11) NOT NULL COMMENT 'same as whoscored team id',
  `team_name` varchar(45) NOT NULL,
  `date` date NOT NULL COMMENT '创建这条数据的时间',
  `type` varchar(45) NOT NULL COMMENT '''Summary | Defensive | Offensive''',
  `view` varchar(45) NOT NULL COMMENT '''Overall | Home | Away''',
  `tournament` varchar(45) NOT NULL COMMENT 'Tournament name',
  `rating` double DEFAULT NULL COMMENT 'rating',
  `apps` int(11) NOT NULL COMMENT 'app 参与次数',
  `goals` int(11) DEFAULT NULL COMMENT 'Total goals',
  `shots_pg` double DEFAULT NULL COMMENT 'Shots per game',
  `possession` double DEFAULT NULL COMMENT 'Possession Percentage 占有球,控场',
  `pass` double DEFAULT NULL COMMENT 'Pass success percentage',
  `aerials_won` double DEFAULT NULL COMMENT 'Aerial duels won per game 头球',
  `tackles_pg` double DEFAULT NULL COMMENT 'Tackles per game 铲球',
  `shots_conceded_pg` double DEFAULT NULL COMMENT 'Shots conceded per game',
  `interceptions_pg` double DEFAULT NULL COMMENT 'Interceptions per game 抢断',
  `fouls_pg` double DEFAULT NULL COMMENT 'Fouls per game 犯规',
  `offsides_pg` double DEFAULT NULL COMMENT 'Offsides per game 越位',
  `shots_ot_pg` double DEFAULT NULL COMMENT 'Shots on target per game',
  `dribbles_pg` double DEFAULT NULL COMMENT 'Dribbles per game 运球',
  `fouled_pg` double DEFAULT NULL COMMENT 'Fouled per game 犯规',
  `sdate` varchar(45) NOT NULL COMMENT '字符串时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `onlyone` (`team_id`,`sdate`,`view`,`tournament`,`type`)
) ENGINE=InnoDB AUTO_INCREMENT=8784 DEFAULT CHARSET=utf8 COMMENT='队伍的静态数据（重要性不大，更多是做佐证用，权重不要高，一般偏下，因为数据变化很慢，而且时间长度太长，没有近期时效性）'

CREATE TABLE `tournament_teams` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tournament` varchar(45) NOT NULL,
  `date` date NOT NULL,
  `no` int(11) NOT NULL,
  `team_name` varchar(45) NOT NULL,
  `team_link` varchar(255) NOT NULL,
  `team_id` int(11) NOT NULL,
  `played` int(11) NOT NULL,
  `win` int(11) NOT NULL,
  `draw` int(11) NOT NULL,
  `loss` int(11) NOT NULL,
  `goals_for` int(11) NOT NULL,
  `goals_against` int(11) NOT NULL,
  `goals_difference` int(11) NOT NULL,
  `points` int(11) NOT NULL,
  `sdate` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `onlyone` (`tournament`,`team_id`,`sdate`)
) ENGINE=InnoDB AUTO_INCREMENT=517 DEFAULT CHARSET=utf8 COMMENT='联赛球队积分排名情况'

