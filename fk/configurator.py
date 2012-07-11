import os
import config

filePath = os.path.join(os.getcwdu(), config.default.configFileName)

def updateConfig():
	checkForExistingConfigFile()

def checkForExistingConfigFile():
	try:
		with open(filePath) as f: #@UnusedVariable
			pass
	except IOError as e: #@UnusedVariable
		configFile = open(filePath, "w")
		configFile.close()
		writeDefaultConfig()

def writeDefaultConfig():
	pass

def loadConfig():
	pass