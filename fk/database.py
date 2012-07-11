import config
import os
import sqlite3



def run(): # TODO rename this
	checkForExistingDatabase()

def checkForExistingDatabase():
	try:
		with open(config.default.dbFilePath) as f: #@UnusedVariable
			pass
	except IOError as e: #@UnusedVariable
		setUpDatabase()

def setUpDatabase():
	connection = sqlite3.connect(config.default.dbFilePath)
	cursor = connection.cursor()
	
	command = ("""
		CREATE TABLE musicfiles
			(name text, path text, size integer)
	""")
	cursor.execute(command)
	
	connection.commit()
	connection.close()

def clearDatabase():
	connection = sqlite3.connect(config.default.dbFilePath)
	cursor = connection.cursor()
	
	command = ("""
		DROP TABLE IF EXISTS musicfiles
	""")
	cursor.execute(command)
	
	connection.commit()
	connection.close()

def fillDatabase():
	for root, dirs, files in os.walk(config.libraryPath):
		print dirs