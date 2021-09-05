#__________________________________________________________________________________________________
#SQL Connector
import mysql.connector


def local_database():
	mydb = mysql.connector.connect(
		host = "",
		user = "",
		passwd = "",
		database = "",
	)

	return mydb
