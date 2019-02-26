CREATE TABLE `team_statistics` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `team_id` int(11) NOT NULL,
  `team_name` varchar(45) NOT NULL,
  `date` date NOT NULL COMMENT '创建这条数据的时间',
  `type` varchar(45) NOT NULL COMMENT '''Summary | Defensive | Offensive''',
  `view` varchar(45) NOT NULL COMMENT '''Overall | Home | Away''',
  `tournament` varchar(45) NOT NULL COMMENT 'Tournament name',
  `rating` double NOT NULL COMMENT 'rating',
  `apps` int(11) NOT NULL COMMENT 'app 参与次数',
  `goals` int(11) DEFAULT NULL COMMENT 'Total goals',
  `shots_pg` double DEFAULT NULL COMMENT 'Shots per game',
  `possession` double DEFAULT NULL COMMENT 'Possession Percentage 占有球,控场',
  `pass` double DEFAULT NULL COMMENT 'Pass success percentage',
  `aerials_won` double DEFAULT NULL COMMENT 'Aerial duels won per game 头球',
  `tackles_pg` double DEFAULT NULL COMMENT 'Tackles per game 铲球',
  `shoted_pg` double DEFAULT NULL COMMENT 'Shots conceded per game',
  `interceptions_pg` double DEFAULT NULL COMMENT 'Interceptions per game 抢断',
  `fouls_pg` double DEFAULT NULL COMMENT 'Fouls per game 犯规',
  `offsides_pg` double DEFAULT NULL COMMENT 'Offsides per game 越位',
  `shots_ot_pg` double DEFAULT NULL COMMENT 'Shots on target per game',
  `dribbles_pg` double DEFAULT NULL COMMENT 'Dribbles per game 运球',
  `fouled_pg` double DEFAULT NULL COMMENT 'Fouled per game 犯规',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='队伍的静态数据（重要性不大，更多是做佐证用，权重不要高，一般偏下，因为数据变化很慢，而且时间长度太长，没有近期时效性）'


CREATE TABLE `team_fixtures` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tournament` varchar(45) NOT NULL,
  `date` date NOT NULL,
  `home_team` varchar(45) NOT NULL,
  `away_team` varchar(45) NOT NULL,
  `home_goals` int(11) NOT NULL,
  `away_goals` int(11) NOT NULL,
  `result` varchar(12) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='队伍具体比赛数据'