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
		setUp()

def setUp():
	connection = sqlite3.connect(config.default.dbFilePath)
	cursor = connection.cursor()
	
	cursor.execute("""
		CREATE TABLE musicfiles
			(name text, path text, size integer)
	""")

	connection.commit()
	connection.close()

def clear():
	connection = sqlite3.connect(config.default.dbFilePath)
	cursor = connection.cursor()
	
	cursor.execute("""
		DROP TABLE IF EXISTS musicfiles
	""")

	connection.commit()
	connection.close()
	
	createTables()

def createTables():
	connection = sqlite3.connect(config.default.dbFilePath)
	cursor = connection.cursor()
	
	cursor.execute("""
		CREATE TABLE musicfiles
			(name text, path text, size integer)
	""")
	
	connection.commit()
	connection.close()

def fill():
	connection = sqlite3.connect(config.default.dbFilePath)
	cursor = connection.cursor()

	for root, dirs, files in os.walk(config.libraryPath): #@UnusedVariable
		for name in files:
			if name.lower().endswith(".mp3"):
				cursor.execute("""
					INSERT INTO musicfiles VALUES(:name, :path, :size)
				""",
				{"name": unicode(name), "path": unicode(os.path.join(root, name)), "size": 0})

	connection.commit()
	connection.close()