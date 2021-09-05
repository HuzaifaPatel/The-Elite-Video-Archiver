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

rankings_url = []
db_rankings_url  = [] 	#youtube video url on db
db_youtube_url = []		#youtube url on db
rankings_youtube_url = []
merged_yt_url = []

my_cursor.execute("SELECT * FROM video_data WHERE dead_youtube_url = 1 AND file_exists = 1")
result = my_cursor.fetchall()

for i in result:
	db_rankings_url.append(i[9])
	db_youtube_url.append(i[7])

counter = 0
def get_yt_url():
	global counter
	for speedrun_with_video in range(0,len(db_rankings_url)):
		http = httplib2.Http()
		status, response = http.request(db_rankings_url[speedrun_with_video])
		video = BeautifulSoup(response, 'html.parser')

		time.sleep(0.01)
		for yt_video in video.find_all('a', href=True):
			if 'youtube.com' in yt_video['href'] or 'twitch.tv/videos' in yt_video['href'] or 'activigor.com' in yt_video['href'] or 'thengamer.com/' in yt_video['href']:
				counter = counter + 1
				rankings_youtube_url.append(yt_video['href'])

get_yt_url()

db_youtube_url = set(db_youtube_url)
rankings_youtube_url = set(rankings_youtube_url)

newset = db_youtube_url - rankings_youtube_url

print(len(newset))

for i in newset:
	print(i)