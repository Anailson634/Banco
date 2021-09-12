#Inicio
import os
from FuncUser import *
from FuncMenu import *
from colorama import init

init(convert=True)



NovoClient()
NovaConta()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    Cabecario('Banco SSH')
    Menu('Depositar', 'Sacar', 'Ver dados', 'Transferencia', 'Finalizar e Salvar')

    User=int(input(">> "))

    if User == 0:
        DepositarM()

    elif User == 1:
        SacarM()

    elif User == 2:
        SolicitarDB()

    elif User == 3:
        Transfery()

    elif User == 4:
        print('Finalizando...')
        sleep(2)
        print('Pronto!')
        try:
            Save()
        except:
            print('Finalizado sem registro!')
        break
    else:
        print('\033[31mOpção invalida!\033[m')
        sleep(2)
