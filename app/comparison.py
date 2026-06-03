import json
from pathlib import Path
from datetime import datetime
from app.config import NEW_FILE, CURRENT_FILE, LOGGER_DIR


# VALIDANDO EXISTENCIA DO ARQUIVO
def valin_file():

    arquivo = CURRENT_FILE

    if arquivo.is_file():
        return True
    else:
        with open(CURRENT_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)

# VOLTANDO O ARQUIVO JSON COMO ANTIGO ARQUIVO
def load_Currentfile():
    if valin_file():
        with open(CURRENT_FILE, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    else: 
        with open(CURRENT_FILE, "w", encoding="utf-8") as arquivo:
            return json.dump([],arquivo)

def load_Newfile():
    with open(NEW_FILE, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def fazer_dump(dados):
    with open(CURRENT_FILE, "w", encoding="utf-8") as arquivo:
        return json.dump(dados,arquivo,indent=4)

def device_exists(new_device, current_devices):

    for current in current_devices:

        # DISPOSITIVOS COM MAC
        if (
            new_device["mac"] != "Sem MAC"
            and
            current["mac"] == new_device["mac"]
        ):
            return True

        # DISPOSITIVOS SEM MAC
        elif (
            new_device["mac"] == "Sem MAC"
            and
            current["ip"] == new_device["ip"]
        ):
            return True

    return False

# COMPARANDOS AS TABELAS 
def comparison(new_devices, current_devices):
    val_mac = {n_mac['mac'] for n_mac in current_devices}

    disp = 1 

    for new in new_devices:

        if not device_exists(new, current_devices):

            novo_dispositivo = {
                "ip": new["ip"],
                "mac": new["mac"],
                "fabricante": new["fabricante"],
                "data": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}

            current_devices.append(novo_dispositivo)
            val_mac.add(new["mac"])

    fazer_dump(current_devices)
            
current_devices = load_Currentfile()
new_devices = load_Newfile()
