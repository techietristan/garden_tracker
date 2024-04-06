import os, sys
from utils.datetime import getDateTime
from utils.json import readJson, writeJson

filename = f'./json/seeds.json'
seedsFileExists: bool = os.path.isfile(filename)
defaultSeedsDict = {'seedDictList': []}

if not seedsFileExists:
    writeJson(filename, defaultSeedsDict)

def checkQuit(input: str) -> None:
    if input.lower() in ['q', 'quit', 'e', 'exit']:
        sys.exit(0)
    
def updateSeeds(currentSeeds: dict, newSeedInfo: list) -> dict:
    currentSeedDictList = currentSeeds['seedDictList']
    return {'seedDictList': currentSeedDictList + newSeedInfo}

def getSeedInfo() -> list:
    seedName = input('Please enter the seed name: ')
    checkQuit(seedName)
    seedSerial = input('Please enter the seed serial: ')
    checkQuit(seedSerial)
    
    return [ { 'seedSerial': seedSerial, 'seedName': seedName, 'seedInventoryDate': getDateTime() } ]

def promptForSeedInfo() -> None:
    while True:
        newSeedInfo: list = getSeedInfo()
        currentSeeds: dict = readJson(filename)
        newSeeds: dict = updateSeeds(currentSeeds, newSeedInfo)
        writeJson(filename, newSeeds)

