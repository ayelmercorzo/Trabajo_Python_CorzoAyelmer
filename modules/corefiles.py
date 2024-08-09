import json
import modules.movesJson as mj

DATABASE_TRANSACCIONES = 'data/transacciones.json'
DATABASE_COMPRAS = 'data/compras.json'

def iniciarRegistroTransacciones():
    mj.checkfile(DATABASE_TRANSACCIONES, {"transacciones": []})
    mj.checkfile(DATABASE_COMPRAS, {"compras": []})
