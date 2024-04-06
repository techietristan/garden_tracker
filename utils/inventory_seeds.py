import os
from utils.datetime import getDateTime
from utils.json import readJson, writeJson
from utils.prompt_utils import prompt

filename = f'./json/seeds.json'
seedsFileExists: bool = os.path.isfile(filename)
defaultSeeds: dict = {'seedsDictsList': []}

if not seedsFileExists:
    writeJson(filename, defaultSeeds)
    
def updateSeeds(currentSeeds: dict, newSeedInfo: list[dict]) -> dict:
    currentSeedDictList: list = currentSeeds['seedsDictsList']
    return {'seedsDictsList': currentSeedDictList + newSeedInfo}

def getSeedInfo() -> list:
    seedName: str = prompt('Please enter the seed name: ')
    seedSerial: str = prompt('Please enter the seed serial: ')
    seedUpc: str = prompt('Please enter the seed UPC: ')
    seedQuantity: str = prompt('Please enter the seed quantity: ')
    
    return [ { 'seedSerial': seedSerial, 'seedName': seedName, 'seedUpc': seedUpc, 'seedQuantity': seedQuantity, 'seedInventoryDate': getDateTime() } ]

def promptForSeedInfo() -> None:
    while True:
        newSeedInfo: list[dict] = getSeedInfo()
        currentSeeds: dict = readJson(filename)
        newSeeds: dict = updateSeeds(currentSeeds, newSeedInfo)
        writeJson(filename, newSeeds)
        print('\n')