import json
import os
import modules.corefiles as cf

def checkfile(databaseFile, datachek):
    if os.path.isfile(databaseFile):
        return  
    with open(databaseFile, "w") as file:
        json.dump(datachek, file, indent=4)

def aggDataTransacciones(*param):
    transacciones = list(param)
    with open(cf.DATABASE_TRANSACCIONES, "r+") as rwf:
        data_transacciones_file = json.load(rwf)
        if len(param) > 1:
            data_transacciones_file[transacciones[0]].update({transacciones[1]: transacciones[2]})
        else:
            data_transacciones_file.update({param[0]})
        rwf.seek(0)
        json.dump(data_transacciones_file, rwf, indent=4)




