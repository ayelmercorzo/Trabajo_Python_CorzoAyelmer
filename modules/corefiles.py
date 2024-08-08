import json
import modules.movesJson as mj

DATABASE_TRANSACCIONES = 'data/transacciones.json'

transaccionesDatabase = {"transacciones": {}}

def iniciarRegistroTransacciones():
    mj.checkfile(DATABASE_TRANSACCIONES, transaccionesDatabase)



