from FuncUser import *

Guest = ...
cliente = ...

def NovaConta(): # Menu Criação da conta
    global Guest
    Cabecario('Nova conta')
    while True:
        try:
            Numero = str(input('Número: '))
            Saldo = float(input('Saldo: '))
            Limite = float(input('Limite: '))
            try:
                if cliente.Nome:
                    Guest = Conta(Numero, cliente, Saldo, Limite)
            except:
                print('\033[31mVocê ainda não tem um conta cliente!. Crie uma para continuar (lOCALIZDA NO PAINEL!).')
                sleep(3.5)
        except:
            print('\033[31mPrencha os dados corretamente!\033[35m')
            sleep(2.5)
        break

def DepositarM(): # Menu Deposito
    global Guest
    Cabecario('Depositar uma quantia')
    try:
        Guest.Add()
    except NameError:
        print('\033[31mVocê ainda não criou sua conta!\033[35m')
        sleep(2.5)

def SacarM(): # Menu Sacando
    global Guest
    Cabecario('Sacar dinhero')
    try:
        Guest.Retirar()
    except NameError:
        print('\033[31mVocê ainda não criou sua conta!\033[35m')
        sleep(2.5)

def SolicitarDB(): # Menu Solicitação de dados
    Cabecario('Solisitação de dados')
    try:
        print(f'Número: {Guest.numero}')
        print(f'Nome: {cliente.Nome} {cliente.Sobrenome}')
        print(f'CPF: {cliente.cpf}')
        print(f'Saldo: R${Guest.saldo:.2f}')
        print(f'Limite: R${Guest.limite:.2f}')
        sleep(6.4)
    except:
        print('\033[31mPelo visto sua conta ainda não foi criada!\033[35m')
        sleep(2.5)

def NovoClient(): # Menu Criando cliente
    global cliente
    Cabecario('Novo cliente')
    nome = NomeVerify('Nome: ', tot=6)
    sobre = NomeVerify('Sobrenome: ', tot=5)
    while True:
        try:
            CPF = int(input('CPF (Sem pontuação): '))
        except ValueError:
            print('Ocorreu um erro')
        else:
            if len(str(CPF)) == 11:
                cliente = Client(Nome=nome, Sobrenome=sobre, cpf=CPF)
                break
            else:
                print('Por favor. seu CPF tem que ter 11 caracteres')

def Transfery(): # Transferir Dinhero par FULANO
    IdFu = str(input('ID do Usuario: '))

    while True:
        try:
            Transfy = float(input('Quantia: '))
        except:
            print('\033[31mEsse valor não é valido!\033[35m')
                
        else:
            try:
                if Transfy > Guest.limite:
                    print('\033[31mUm valor menor, por favor.\033[36m')
                else:
                    Guest.saldo -= Transfy
                    Guest.hstor['Tranzações'].append(f'Transferio R${ConRS(Transfy)} para {IdFu}')
                    break
            except:
                print('\033[31mVocê ainda não criou sua conta!')
                sleep(2)
                break

def Save(): # Salvando informações do Usuario

    arq = open('Conta_Banco.txt', 'w')
    arq.write(f'Data: {Guest.hstor["Data"]} \n----------------\n')
    arq.write(f'Número: {Guest.numero}\n')
    arq.write(f'Nome: {Guest.cliente.Nome} {Guest.cliente.Sobrenome}\n')
    arq.write(f'CPF: {Guest.cliente.cpf}\n')
    arq.write(f'Saldo: R${ConRS(Guest.saldo)}\n')
    arq.write(f'Limite: R${ConRS(Guest.limite)}\n')

    arq.write('Tranzações:\n')
    for v in Guest.hstor['Tranzações']:
        arq.write(f'\t{v}\n')
