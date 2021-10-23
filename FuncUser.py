from time import sleep
from time import localtime as Loc

def Cabecario(text):
    print('\033[36m='*40)
    print('\033[35m'+text.center(40))
    print('\033[36m=\033[35m'*40)

def Menu(*args):
    for c, v in enumerate(args):
        print(f'\033[36m{c}- {v}\033[35m')

def NomeVerify(Text, tot=6):
    while True:
        Nome = str(input(Text)).strip()
        if len(Nome) < tot:
            print(f'\033[31mVocê precisa digitar pelo menos {tot} caracteres!\033[35m')
        else:
            return Nome

def ConRS(RS):
    RS=f'{RS:.2f}'
    n=0
    Cnv=''
    for c in str(RS)[::-1]:
        if n==3:
            Cnv+=','
            n=0
        Cnv+=c
        n+=1

    return f"R${Cnv[::-1].replace(f',.', '.')}"  # Colocando tudo em ordem

class Conta():
    def __init__(self, numero, cliente, saldo, limite):
        self.hstor = {'Data': f'{Loc()[2]:0>2}/{Loc()[1]:0>2}/{Loc()[0]}', 'Tranzações': []}
        self.numero = numero
        self.cliente = cliente
        self.saldo = float(saldo)

        if limite > 10000.00:
            self.limite = 'Ilimitado'
        else:
            self.limite = float(limite)

    def Add(self):
        while True:
            try:
                Depo = float(input('Depositar: '))
                self.saldo += Depo
                print('Deposito concluido!')
                self.hstor['Tranzações'].append(f'Depositou {ConRS(Depo)}')
                break
            except ValueError:
                print('\033[31mVocé inserio uma letra. Só aceitamos Números.\033[m')

    def Retirar(self):
        while True:
            try:
                Saque = float(input('Saque: '))
                if Saque > self.limite or Saque < 0:
                    print('\033[31mLimite exedido\033[m')
                    sleep(2)
                else:
                    self.saldo -= Saque
                    print('Saque realizado com sucesso!')
                    self.hstor['Tranzações'].append(f'Retirou {ConRS(Saque)}')
                    sleep(2)
                    break
            except:
                print('\033[31mPorfavor. coloque apenas números\033[m')

class Client():
    def __init__(self, Nome, Sobrenome, cpf):
        self.Nome = Nome
        self.Sobrenome = Sobrenome
        self.cpf = self.Convert(str(cpf))

    def Convert(self, num):
        nu = list(num.replace('.', '').replace('-', ''))

        c1 = 0  # Contagem de verificação
        for c3, c2 in enumerate(nu[0:9]):
            c1 += 1
            if c1 == 4:  # Atingiu o valor esperado?
                nu.insert(c3, '.')
                c1 -= 4
        nu.insert(-2, '-')
        st = ''
        for c in nu:
            st += c
        return st
