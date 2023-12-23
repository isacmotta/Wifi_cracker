import os
import socket
from wifi import Cell


#detectar a rede wifi.
#potencia...
def ScanWifiProx():
    #listando redes ão alcance.
    cells=Cell.all('wlan0')
    for cell in cells:
        print ('#'*33)
        print cell.ssid
        print ('#'*33)

    #testar potencia do wifi
    cells = Cell.all('wlan0')
    cell_power = []

    for cell in cells:
        cell_power.append((cell.ssid,cell.signal))
    cell_power.sort(key=lambda cell.signal:cell.signal[1])

    print('*'*33)
    print(cell_power)
    print('*'*33)




def inicio():
    print('='*33)
    print("Wifi Exploiter by isacmotta")
    print('+'*33)
    print('''
    Escolha uma das opçẽs
    [1].Iniciar
    [2].Logs
    [x].Sair''')
    op = input("  $~ ")
    if op == 1:
        return ScanWifiProx()
    elif op == 'x' or 'Sair' or 'sair' or 'exit':
        exit()


inicio()