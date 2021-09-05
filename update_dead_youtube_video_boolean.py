import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import time
import feedparser
import os
import youtube_dl
import requests # for def get_time_info():
from tqdm import tqdm
import refresh

#__________________________________________________________________________________________________
#SQL Connector
import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "the-elite-videos",
)

my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM video_data")
result = my_cursor.fetchall()

for time in tqdm(result):
	try:
		ydl_opts = {'outtmpl' : time[10], 'noplaylist' : True}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.extract_info(time[7], download = False)
		my_cursor.execute("UPDATE video_data SET dead_youtube_url = 0 WHERE rankings_id = %s", (time[12],))
		mydb.commit() #save
	except:
	# except (youtube_dl.utils.DownloadError, youtube_dl.utils.ExtractorError, youtube_dl.utils.ERROR):
		my_cursor.execute("UPDATE video_data SET dead_youtube_url = 1 WHERE rankings_id =  %s", (time[12],))
		mydb.commit()
