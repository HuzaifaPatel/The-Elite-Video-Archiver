import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "the-elite-videos",
)

ltk_videos = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "the-elite-ltk-videos",
)

single_segment = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "the-elite-single-segment-videos",
)

import sshtunnel

# with sshtunnel.SSHTunnelForwarder(
#         ('138.197.162.125', 22),
#         ssh_username="huzaifa",
#         ssh_password="theelitehuzi007",
#         remote_bind_address=('138.197.162.125', 22),
#         local_bind_address=('127.0.0.1', 3306)
# ) as tunnel:
#     mydb = mysql.connector.connect(
#         user="huzaifa",
#         password="theelitehuzi007",
#         host="138.197.162.125",
#         database="the-elite-videos",
#     )

my_cursor = mydb.cursor()
ltk_cursor = ltk_videos.cursor()
single_segment_cursor = single_segment.cursor()

def delete_Table():
	# clear table
	delete_all_rows = """truncate table dupe_checker"""
	my_cursor.execute(delete_all_rows)
	mydb.commit()

	# get data
	my_cursor.execute("SELECT * FROM video_data")
	data = my_cursor.fetchall()

	# fill table
	for i in data:
		filename = i[10]
		if filename.find("(") != -1:
			filename = filename[:len(filename)-(len(filename)-filename.find("("))] + ".mp4"

		add_file_name = "INSERT INTO dupe_checker (filename, rankings_id) VALUES (%s, %s)"
		my_cursor.execute(add_file_name, (filename, i[12]))
		mydb.commit() #save


def delete_LTK_Table():
	# clear table
	delete_all_rows = """truncate table dupe_checker"""
	ltk_cursor.execute(delete_all_rows)
	ltk_videos.commit()

	# get data
	ltk_cursor.execute("SELECT * FROM video_data")
	data = ltk_cursor.fetchall()

	# fill table
	for i in data:
		filename = i[10]
		if filename.find("(") != -1:
			filename = filename[:len(filename)-(len(filename)-filename.find("("))] + ".mp4"

		add_file_name = "INSERT INTO dupe_checker (filename, rankings_id) VALUES (%s, %s)"
		ltk_cursor.execute(add_file_name, (filename, i[12]))
		ltk_videos.commit() #save



def delete_SingleSegment_Table():
	# clear table
	delete_all_rows = """truncate table dupe_checker"""
	single_segment_cursor.execute(delete_all_rows)
	single_segment.commit() #save

	# get data
	single_segment_cursor.execute("SELECT * FROM video_data")
	data = single_segment_cursor.fetchall()

	# fill table
	for i in data:
		filename = i[10]
		if filename.find("(") != -1:
			filename = filename[:len(filename)-(len(filename)-filename.find("("))] + ".mp4"

		add_file_name = "INSERT INTO dupe_checker (filename, rankings_id) VALUES (%s, %s)"
		single_segment_cursor.execute(add_file_name, (filename, i[12]))
		single_segment.commit() #save