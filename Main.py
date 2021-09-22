#Inicio
import os
from FuncUser import *
from FuncMenu import *
from colorama import init
init(convert=True)


root=Ui_Menu()

root.NovoClient()
root.NovaConta()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    root.SolicitarDB()

    Cabecario('Banco SSH')
    Menu('Depositar', 'Sacar', 'Ver dados', 'Transferencia', 'Finalizar e Salvar')

    User=int(input(">> "))

    if User == 0:
        root.DepositarM()

    elif User == 1:
        root.SacarM()

    elif User == 3:
        root.Transfery()

    elif User == 4:
        print('Finalizando...')
        sleep(2)
        print('Pronto!')
        try:
            root.Save()
        except:
            print('Finalizado sem registro!')
        break
    else:
        print('\033[31mOpção invalida!\033[m')
        sleep(2)
