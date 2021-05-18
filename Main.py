#Inicio
import os
from FuncUser import *
from FuncMenu import *
from colorama import init, Fore, Back

init(convert=True)
#Menu Iteravel
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    #  Logo do Banco SSH
    print('\033[36m='*40)
    print('Banco SSH'.center(40))
    print('='*40)

    print('\033[mPainel de consulta')
    Menu('Nova conta', 'Depositar', 'Sacar', 'Ver dados', 'Novo Cliente', 'Transferencia', 'Finalizar e Salvar')
    try:
        User = int(input('\nOpção: '))
    except:
        print('\033[31mOlhe o painel de consulta. Escolha uma opção valida!\033[35m')
        sleep(2)

    #Opções
    else:
        #  Nova conta
        if User == 0: 
            NovaConta()

        #  Depositar Dinhero
        elif User == 1:
            DepositarM()

        #  Sacar dinhero
        elif User == 2:
            SacarM()

        #  Ver dados do Usuario
        elif User == 3:
            SolicitarDB()

        #  Criar Cliente
        elif User == 4:
            NovoClient()

        #  Transferir
        elif User == 5:
            Transfery()

        elif User == 6:
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
