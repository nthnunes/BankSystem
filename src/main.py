import os
from banco import Banco
from cliente import Cliente
from conta import Conta
from saves import *

banco = Banco()
password = readPassword()

numero = check(banco)
if numero != None:
    cont = numero
else:
    cont = 999

while True:
    print("MENU:\n1 – Cadastrar cliente/conta\n2 – Consultar\n3 – Depositar\n4 - Sacar\n5 – Transferir\n6 - Finalizar")
    while True:
        try:
            opc = int(input("Digite a opção que deseja: "))
            break
        except ValueError:
            print("Entrada inválida, tente novamente\n")
        except Exception as e:
            log(e)

    if opc == 1:
        nome = input("Digite o Nome: ")
        cpf = input("Digite o CPF: ")
        endereco = input("Digite o endereço: ")
        telefone = input("Digite o telefone: ")
        tipo = input("\n1 - Corrente\n2 - Poupança\nTipo de conta: ")
        while True:
            try:
                saldo = float(input("Depósito inicial: "))
                break
            except ValueError:
                print("Valor inválido, use ponto em vez de vírgula\n")
            except Exception as e:
                log(e)
        banco.cadastrar(Cliente(nome, cpf, endereco, telefone, Conta(cont+1, tipo, saldo)))
        cont = cont + 1
        print("Cliente cadastrado com sucesso")

    elif opc == 2:
        nome = input("Digite o Nome que deseja consultar: ")
        if banco.consultar(nome) != None:
            cliente = banco.consultar(nome)
            print("\nNome: ",cliente.getNome())
            print("CPF:",cliente.getCpf())
            print("Endereço:",cliente.getEndereco())
            print("Telefone:",cliente.getTelefone())
            print("Conta:",cliente.getConta().getNumero())
            print("Saldo: R$%0.2f" %cliente.getConta().getSaldo())
        else:
            print("Cliente inexistente")

    elif opc == 3:
        nome = input("Digite o Nome que deseja depositar: ")
        if banco.consultar(nome) != None:
            valor = float(input("Valor de depósito: "))
            banco.depositar(nome, valor)
        else:
            print("Cliente não encontrado")

    elif opc == 4:
        nome = input("Digite o Nome que deseja Sacar: ")
        if banco.consultar(nome) != None:
            valor = float(input("Digite o valor que deseja sacar: "))
            if banco.sacar(nome, valor):
                print("Saque efetuado com sucesso")
            else:
                print("Saldo insuficiente")
        else:
            print("Cliente não encontrado")

    elif opc == 5:
        nome = input("Digite o Nome de quem irá transferir: ")
        if banco.consultar(nome) != None:
            nome2 = input("Digite o nome do cliente quem irá receber: ")
            valor = float(input("Digite o valor que deseja transferir: "))
            if banco.transferir(nome, nome2, valor):
                print("Transferência efetuada com sucesso")
            else:
                print("Saldo insuficiente")
        else:
            print("Cliente não encontrado")
            
    elif opc == 6:
        clientes = banco.getClientes()
        if os.path.exists('./data.dat'):
            try:
                os.remove("data.dat")
            except Exception as e:
                print(e)
                log(e)
        for i in range(len(clientes)):
            if clientes[i] != None:
                save(clientes[i])
        exit()

    elif opc == 777:
        if password == None:
            password = input("Nova senha: ")
            temp = input("Confirme a senha: ")
            if password != temp:
                print("As senhas não conferem.")
                password = None
            else:
                savePassword(password)
                print("Senha criada com sucesso!")
        else:
            temp = input("Senha: ")
            if password == temp:
                while True:
                    print("\nADMIN MODE:\n1 – Alterar dados\n2 – Apagar usuário\n3 – Deletar todos os dados\n4 - Exibir log\n5 - Sair")
                    while True:
                        try:
                            opc = int(input("Digite a opção que deseja: "))
                            break
                        except ValueError:
                            print("Entrada inválida, tente novamente\n")
                        except Exception as e:
                            log(e)

                    if opc == 1:
                        pass

                    elif opc == 2:
                        nome = input("Nome do cliente a ser deletado: ")
                        if banco.deletar(nome):
                            print("O cliente foi deletado com sucesso!")
                        else:
                            print("Cliente não encontrado.")

                    elif opc == 3:
                        temp = input("Tem certeza que deseja deletar todos os dados: [yes/cancel]\n")
                        if temp.lower() == "yes":
                            os.remove("data.dat")
                            banco = Banco()

                    elif opc == 4:
                        viewLog()

                    elif opc == 5:
                        break
            else:
                print("Senha incorreta.")
    
    print("")