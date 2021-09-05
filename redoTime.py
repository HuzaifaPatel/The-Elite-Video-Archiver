import mysql.connector
import time

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "the-elite-ltk-videos",
)

my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM video_data")
result = my_cursor.fetchall()

def redo():
	import time
	for data in result:
		reg_time = ""

		if int(data[3]) >= 3600:
			reg_time = time.strftime("%H:%M:%S", time.gmtime(int(data[3])))
		else:
			reg_time = time.strftime("%M:%S", time.gmtime(int(data[3])))


		reg_time = reg_time.split(":")

		for i in range(1):
			reg_time[0] = str(int(reg_time[0]))

		reg_time = ":".join(reg_time)
		my_cursor.execute("UPDATE video_data SET regular_time = %s WHERE rankings_id =  %s", (reg_time, data[12],))
		mydb.commit()
redo()

