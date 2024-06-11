"""
Operação de DEPOSITO: deve ser possível depositar valores positivos para a minha conta bancária
apenas 1 usuário , todos os depositos devem ser armazenados em uma variável e exibidos na operação extrato

Operação de SAQUE: o sistema deve permitir 3 saques diários com limite máximo de R$ 500,00 por saque.
Caso o usuário nao tenha saldo em conta, o sistema deve exibir uma mensagem informando que nao é possivel 
sacar o dinheiro por falta de saldo, todos os saque devem ser armazandos em uma variavel e exibidos na operação extrato

Operação EXTRATO: essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx
exemplo: 1500.45 = R$1500.45

"""
                            
def Menu():
    
    print("""
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
    """)


def Banco():
    
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    transaçoes = []
    

    while True:
        Menu()
        opção = int(input("Opção: "))
        
        if opção == 1:
            deposito = float(input("Valor a ser depositado R$: "))
            if deposito > 0:
                saldo += deposito
                transaçoes.append(deposito)
                print("Deposito de {} reais realizado com sucesso!".format(deposito))
                print("Saldo atual da conta R$: {}".format(saldo))
            else: 
                print("Valor invalido, tente novamente!")
            
        elif opção == 2:
            if numero_saques >= LIMITE_SAQUES:
                print("Limite de saques diários atingidos")
                continue
            
            saque = float(input("Valor do saque R$: "))
            if saque > saldo:
                print("Não é possível prosseguir com a operação")
            elif saque > limite:
                print("Valor de saque excede o limite permitido")
            else:
                saldo -= saque
                numero_saques += 1
                transaçoes.append(saque)
                print("Saque no valor R$: {} realizado com sucesso".format(saque))
                
        elif opção == 3:
            print("\nExtrato:")
            for transacao in transaçoes:
                print(transacao)
            print("saldo atual: {}".format(saldo))
            
        elif opção == 0:
            print("Saindo do sistema...")
            break
        
        



Banco()