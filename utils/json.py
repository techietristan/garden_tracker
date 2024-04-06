import json, os

def readJson(filename: str) -> dict:
    with open(filename, 'r') as jsonFile:
        return json.load(jsonFile)

def writeJson(filename: str, data: dict) -> None:
    fileExists: bool = os.path.isfile(filename)
    if fileExists:
        existingData = readJson(filename)
        newData = dict(existingData, **data)
    else:
        newData = data
        
    with open(filename, 'w') as jsonFile:
        json.dump(newData, jsonFile)