import config


def updateConfig():
	checkForExistingConfigFile()

def checkForExistingConfigFile():
	try:
		with open(config.default.configFilePath) as f: #@UnusedVariable
			pass
	except IOError as e: #@UnusedVariable
		configFile = open(config.default.configFilePath, "w")
		configFile.close()