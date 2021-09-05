# this file updates the "file_exists" database column by checking if the file exists on my computer
# this will provide an accurate representation on how many videos I have VS the amount of video data in the database

import os.path
import mysql.connector
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import time
import feedparser
import os
import youtube_dl
import requests # for def get_time_info():
from tqdm import tqdm

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	# database = "the-elite-ltk-videos",
	database = "the-elite-videos",
)

my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM video_data GROUP BY player")
result = my_cursor.fetchall()

player_colors = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "player-colors",
)

player_colors_cursor = player_colors.cursor()

player_names = []
player_url = []

for db in result:
	player_names.append(db[5])
	player_url.append("https://rankings.the-elite.net/" + "~" + db[5].replace("_","+"))



for i in range(len(player_names)):
	request = requests.get(player_url[i])
	html_content = request.text
	soup = BeautifulSoup(html_content, 'lxml')
	rta_type = soup.find_all(['h1'])#[51]
	# print(rta_type)
	rta_type = str(rta_type)
	rta_type = rta_type[rta_type.find("#"):]
	rta_type = rta_type[0:rta_type.find('"')]
	print(player_names[i] + " : " + rta_type + " : " + player_url[i])

	add_colors = "INSERT INTO player_colors (player, profile_url, hexcode) VALUES (%s, %s, %s)"
	player_colors_cursor.execute(add_colors, (player_names[i], player_url[i], rta_type))
	player_colors.commit() #save