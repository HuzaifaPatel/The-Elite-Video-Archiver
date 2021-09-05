# this file updates the "file_exists" database column by checking if the file exists on my computer
# this will provide an accurate representation on how many videos I have VS the amount of video data in the database

import os.path
import mysql.connector
from tqdm import tqdm

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

def fileExists():
	my_cursor = mydb.cursor()
	my_cursor.execute("SELECT * FROM video_data")
	result = my_cursor.fetchall()

	for row in tqdm(result):
		if os.path.isfile("D:\\Truth Saver RSS Backup\\the-elite-videos\\" + row[5] + "\\" + row[10]):
			my_cursor.execute("UPDATE video_data SET file_exists = 1 WHERE rankings_id = %s", (row[12],))
		else:
			my_cursor.execute("UPDATE video_data SET file_exists = 0 WHERE rankings_id = %s", (row[12],))
		
		mydb.commit() #save


def fileExistsLTK():
	ltk_cursor = ltk_videos.cursor()
	ltk_cursor.execute("SELECT * FROM video_data")
	ltk_result = ltk_cursor.fetchall()

	for row in tqdm(ltk_result):
		if os.path.isfile("D:\\Truth Saver RSS Backup\\the-elite-ltk-videos\\" + row[5] + "\\" + row[10]):
			ltk_cursor.execute("UPDATE video_data SET file_exists = 1 WHERE rankings_id = %s", (row[12],))
		else:
			ltk_cursor.execute("UPDATE video_data SET file_exists = 0 WHERE rankings_id = %s", (row[12],))
		
		ltk_videos.commit() #save


def fileExistsSingleSegment():
	single_segment_cursor = single_segment.cursor()
	single_segment_cursor.execute("SELECT * FROM video_data")
	single_segment_result = single_segment_cursor.fetchall()

	for row in tqdm(single_segment_result):
		if os.path.isfile("E:\\the-elite-single-segment-videos\\" + row[5] + "\\" + row[10]) == True:
			single_segment_cursor.execute("UPDATE video_data SET file_exists = 1 WHERE rankings_id = %s", (row[12],))
		else:
			single_segment_cursor.execute("UPDATE video_data SET file_exists = 0 WHERE rankings_id = %s", (row[12],))
		
		single_segment.commit() #save

fileExists()
fileExistsLTK()
# fileExistsSingleSegment()