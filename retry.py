# Sometimes, when I run main.py, youtube-dl doesn't download some videos even though they are 'alive'.
# This script will go through the db and attempt to download videos that have file_exists = 0
# It acts as a retry attempt
import youtube_dl
import mysql.connector
import os
from tqdm import tqdm

successful = []
success = 0
failed = 0

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "the-elite-videos",
)

my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM video_data WHERE file_exists = 0")
result = my_cursor.fetchall()
print("")

def check_If_Dead():
	global successful
	global success
	global failed
	for time in tqdm(result, desc = "retrying"):

		os.chdir("D:\\Truth Saver RSS Backup\\the-elite-videos\\" + time[5] + "\\")

		if time[5] == "Roger_Cantley" and time[4] == "1:32":
			print(time[5] + " - " + time[4])
		if "www.activigor.com" in time[7]:
			continue
		try:
			ydl_opts = {'outtmpl' : time[10], 'noplaylist' : True}
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				# ydl.extract_info(time[7], download = False)
				ydl.download([time[7]])
			my_cursor.execute("UPDATE video_data SET dead_youtube_url = 0 WHERE rankings_id = %s", (time[12],))
			mydb.commit() #save
			successful.append(time[10])
			success =  success + 1
		except:
		# except (youtube_dl.utils.DownloadError, youtube_dl.utils.ExtractorError, youtube_dl.utils.ERROR):
			my_cursor.execute("UPDATE video_data SET dead_youtube_url = 1 WHERE rankings_id =  %s", (time[12],))
			mydb.commit()
			failed = failed + 1

		print("")

	print("")
	for filename in successful:
		print(filename)
	print("Success: " + str(success))
	print("Failed: " + str(failed))

check_If_Dead()

