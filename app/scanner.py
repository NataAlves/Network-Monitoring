from datetime import datetime
import nmap
import json
from app.config import NEW_FILE

# FAZENDO O DUMP DE UM NOVO ARQUIVO
def new_device_scan(devices):
    with open(NEW_FILE,"w", encoding="utf-8") as arquivo: 
        json.dump(devices, arquivo, indent=4)

# FAZENDO SCANNER DA REDE
def scanner_network():

    print("Escaneando rede...")
    rede = "192.168.10.1/24"
    scanner = nmap.PortScanner()
    scanner.scan(hosts=rede, arguments='-sn')
    
    for host in scanner.all_hosts():

        mac = "Desconhecido"
        fabricante = "UNKNOWN"

        if 'addresses' in scanner[host]:
            mac = scanner[host]['addresses'].get('mac', 'UNKNOWN')

        if 'vendor' in scanner[host]:
            vendor_dict = scanner[host]['vendor']

            if vendor_dict:
                fabricante = list(vendor_dict.values())[0]

        dispositivo = {
            "ip": host,
            "mac": mac,
            "fabricante": fabricante,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }   

        devices.append(dispositivo)

    new_device_scan(devices)
    
    
devices = []
