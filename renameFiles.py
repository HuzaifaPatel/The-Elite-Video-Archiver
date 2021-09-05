import os

DIRECTORY = "D:\\Truth Saver RSS Backup\\the-elite-videos\\Jezz_S\\"
NEW_PLAYER = "Jezz_Savage"

for file in os.listdir(DIRECTORY):
	filename = ".".join(file.split("..")).split(".")
	filename[-2] = NEW_PLAYER
	filename = ".".join(filename)

	os.rename(DIRECTORY + file, DIRECTORY + filename)