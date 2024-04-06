import datetime, os
from utils.datetime import getDateTime
from utils.json import readJson, writeJson
from utils.prompt_utils import prompt

year: str = datetime.date.today().year

filename = f'./json/{year}_sprouts.json'
sproutsFileExists: bool = os.path.isfile(filename)
defaultSprouts: dict = {'sproutsDictList': []}

if not sproutsFileExists:
    writeJson(filename, defaultSprouts)
    
def updateSprouts(currentSprout: dict, newSproutInfo: list[dict]) -> dict:
    currentSproutDictList: list = currentSprout['sproutsDictList']
    return {'sproutsDictList': currentSproutDictList + newSproutInfo}

def getSproutInfo() -> list:
    podSerial: str = prompt('Please enter the pod serial: ')
    seedSerial: str = prompt('Please enter the seed serial: ')
    
    return [ { 'seedSerial': seedSerial, 'podSerial': podSerial, 'germinationDate': getDateTime() } ]

def promptForSproutInfo() -> None:
    while True:
        newSproutInfo: list[dict] = getSproutInfo()
        currentSprouts: dict = readJson(filename)
        newSprouts: dict = updateSprouts(currentSprouts, newSproutInfo)
        writeJson(filename, newSprouts)
        print('\n')