import config
import os
import sqlite3


def run(): # TODO rename this
	filePath = os.path.join(os.getcwdu(), config.default.dbFileName)
	
	connection = sqlite3.connect(filePath)
	connection.close()