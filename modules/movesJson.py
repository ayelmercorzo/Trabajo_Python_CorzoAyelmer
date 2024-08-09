import json
import os

def checkfile(databaseFile, datachek):
    if os.path.isfile(databaseFile):
        return
    with open(databaseFile, "w") as file:
        json.dump(datachek, file, indent=4)
