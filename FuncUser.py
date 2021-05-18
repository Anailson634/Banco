from time import sleep
from time import localtime as Loc

def Cabecario(text): #  Cabecario
    print('\033[36m='*(len(text) + 2))
    print('\033[35m'+text.center(len(text)+2))
    print('\033[36m=\033[35m'*(len(text) + 2))

def Menu(*args): #  Montar um menu 
    for c, v in enumerate(args):
        print(f'\033[36m{c}- {v}\033[35m')

def NomeVerify(Text, tot=6):
    """
    Usado Somente para limitar X de caracteres
    """
    while True:
        Nome = str(input(Text)).strip()
        if len(Nome) < tot:
            print(f'\033[31mVocê precisa digitar pelo menos {tot} caracteres!\033[35m')
        else:
            return Nome

def ConRS(Nomel): # Converte em dinhero pt-br 
    return str(Nomel).replace(".", ",")
#Configuração de cliente

#Configuração de Conta
class Conta():
    """
    Criação do cliente, e atributos de depositos, etc...
    """
    def __init__(self, numero, cliente, saldo, limite):
        self.hstor = self.Hstorico()
        self.numero = numero
        self.cliente = cliente
        self.saldo = float(saldo)
        if limite > 10000.00:
            self.limite = 'Ilimitado'
        else:
            self.limite = float(limite)

    def Hstorico(self):
        """
        Historico de navegação
        """
        return {'Data': f'{Loc()[2]:0>2}/{Loc()[1]:0>2}/{Loc()[0]}', 'Tranzações': []}

    def Add(self):
        """
        Depositando X quantia a conta
        """
        while True:
            try:
                Depo = float(input('Depositar: '))
                self.saldo += Depo
                print('Deposito concluido!')
                self.hstor['Tranzações'].append(f'Depositou R${ConRS(Depo)}')
                break
            except:
                print('\033[31mVocé inserio uma letra. Só aceitamos Números.\033[m')

    def Retirar(self):
        """
        Retirar X da conta
        """

        while True:
            try:
                Saque = float(input('Saque: '))
                if Saque > self.limite and Saque < 0:
                    print('\033[31mLimite exedido\033[m')
                    sleep(2)
                else:
                    self.saldo -= Saque
                    print('Saque realizado com sucesso!')
                    self.hstor['Tranzações'].append(f'Retirou R${ConRS(Saque)}')
                    sleep(2)
                    break
            except:
                print('\033[31mPorfavor. coloque apenas números\033[m')

class Client():
    """
    Criação do cliente
    """

    def __init__(self, Nome, Sobrenome, cpf):
        self.Nome = Nome
        self.Sobrenome = Sobrenome
        self.cpf = cpf
