from org.shil import utils

def insert_player_match_behavior(match_id,player_id,player_name,mins,rating_in_this_match,sdate):
	
	if query_player_match_behavior(match_id, player_id) is not None:
		print(str(match_id) + " " + player_id + " already exist, no need insert")
		return
	
	insert_sql = "\
	INSERT INTO player_match_behavior( \
		`date`,\
		`match_id`,\
		`player_id`,\
		`player_nick_name`,\
		`mins`,\
		`rating_in_this_match`,\
		`sdate`)\
	VALUES\
		(%s,%s,%s,%s,%s,%s,%s)"
		
	values = (utils.sdate2date(sdate),match_id,player_id,player_name,mins,rating_in_this_match,sdate)
	
	cnx = utils.get_mysql_connector()
	cursor = cnx.cursor()
	cursor.execute(insert_sql,values)
	nid = cursor.lastrowid
	
	cnx.commit()
	cursor.close()
	cnx.close()
	return nid


def query_player_match_behavior(match_id,player_id):
	
	query_sql = "SELECT match_id FROM player_match_behavior where match_id = %s and player_id = %s"
	
	cnx = utils.get_mysql_connector()
	cursor = cnx.cursor()
	cursor.execute(query_sql,(match_id,player_id))
	one_record = cursor.fetchone()
	if one_record is not None :
		return one_record[0]
	else:
		print('None')
		return None

# print(query_player_match_behavior(232, 2332))