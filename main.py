import json
import modules.funcionGlobal as fg
import modules.corefiles as cf
import ui.uiMenuPrincipal as uiE

fg.borrar_pantalla()
if __name__ == '__main__':
        cf.iniciarRegistroTransacciones()
print(uiE.mainMenu("op"))