import os

class default:
	configFileName = "config.cfg"
	dbFileName = "library.db"
	configFilePath = os.path.join(os.getcwdu(), configFileName)
	dbFilePath = os.path.join(os.getcwdu(), dbFileName)

libraryPath = "D:\\Music"