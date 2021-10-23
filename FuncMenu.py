from FuncUser import *


class Ui_Menu:
    def __init__(self) -> None:
        self.Guest = ...
        self.cliente = False

    def NovaConta(self): # Menu Criação da conta
        Cabecario('Nova conta')
        while True:
            try:
                Numero =str(input('Número: '))
                Saldo =float(input('Saldo: '))
                Limite =float(input('Limite: '))
                if self.cliente.Nome:
                    self.Guest = Conta(Numero, self.cliente, Saldo, Limite)
            except ValueError:
                print('\033[31mPrencha os dados corretamente!\033[35m')
                sleep(2.5) 
            finally:
                break

    def NovoClient(self): # Menu Criando self.cliente
        Cabecario('Novo cliente')
        nome =NomeVerify('Nome: ', tot=6)
        sobre =NomeVerify('Sobrenome: ', tot=5)
        while True:
            try:
                CPF =int(input('CPF (Sem pontuação): '))
            except ValueError:
                print('Ocorreu um erro')
            else:
                if len(str(CPF)) == 11:
                    self.cliente = Client(Nome=nome, Sobrenome=sobre, cpf=CPF)
                    break
                else:
                    print('Por favor. seu CPF tem que ter 11 caracteres')

    def DepositarM(self): # Menu Deposito
        Cabecario('Depositar uma quantia')
        try:
            self.Guest.Add()
        except NameError:
            print('\033[31mVocê ainda não criou sua conta!\033[35m')
            sleep(2.5)

    def SacarM(self): # Menu Sacando
        Cabecario('Sacar dinhero')
        try:
            self.Guest.Retirar()
        except NameError:
            print('\033[31mVocê ainda não criou sua conta!\033[35m')
            sleep(2.5)

    def SolicitarDB(self): # Menu Solicitação de dados
        Cabecario('Minhas informações')
        try:
            print(f'Número:   {self.Guest.numero}')
            print(f'Nome:     {self.cliente.Nome} {self.cliente.Sobrenome}')
            print(f'CPF:      {self.cliente.cpf}')
            print(f'Saldo:    {ConRS(self.Guest.saldo)}')
            print(f'Limite:   {ConRS(self.Guest.limite)}')
        except ValueError:
            print('\033[31mPelo visto sua conta ainda não foi criada!\033[35m')


    def Transfery(self): # Transferir Dinhero par FULANO
        IdFu = str(input('ID do Usuario: '))

        while True:
            try:
                Transfy = float(input('Quantia: '))
            except:
                print('\033[31mEsse valor não é valido!\033[35m')
                    
            else:
                try:
                    if Transfy > self.Guest.limite:
                        print('\033[31mUm valor menor, por favor.\033[36m')
                    else:
                        self.Guest.saldo -= Transfy
                        self.Guest.hstor['Tranzações'].append(f'Transferio {ConRS(Transfy)} para {IdFu}')
                        break
                except:
                    print('\033[31mVocê ainda não criou sua conta!')
                    sleep(2)
                    break

    def Save(self): # Salvando informações do Usuario

        arq = open('Conta_Banco.txt', 'w')
        arq.write(f'Data: {self.Guest.hstor["Data"]} \n----------------\n')
        arq.write(f'Número: {self.Guest.numero}\n')
        arq.write(f'Nome: {self.Guest.self.cliente.Nome} {self.Guest.self.cliente.Sobrenome}\n')
        arq.write(f'CPF: {self.Guest.self.cliente.cpf}\n')
        arq.write(f'Saldo: {ConRS(self.Guest.saldo)}\n')
        arq.write(f'Limite: {ConRS(self.Guest.limite)}\n')

        arq.write('Tranzações:\n')
        for v in self.Guest.hstor['Tranzações']:
            arq.write(f'\t{v}\n')
