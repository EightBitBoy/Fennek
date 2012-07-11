import config
import os
import sqlite3


def checkDatabase():
	global connection
	global cursor
	databaseExists = False
	
	try:
		with open(config.default.dbFilePath) as f: #@UnusedVariable
			databaseExists = True
	except IOError as e: #@UnusedVariable
		databaseExists = False
	
	connection = sqlite3.connect(config.default.dbFilePath)
	cursor = connection.cursor()
	if not databaseExists:
		createTables()

def clear():
	with connection:
		cursor.execute("""
			DROP TABLE IF EXISTS musicfiles
		""")
	createTables()

def createTables():
	with connection:
		cursor.execute("""
			CREATE TABLE musicfiles
				(name text, path text, size integer)
		""")
	
def fill():
	for root, dirs, files in os.walk(config.libraryPath): #@UnusedVariable
		for name in files:
			if name.lower().endswith(".mp3"):
				with connection:
					cursor.execute("""
						INSERT INTO musicfiles VALUES(:name, :path, :size)
					""",
					{"name": unicode(name), "path": unicode(os.path.join(root, name)), "size": 0})