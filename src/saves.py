import os
from datetime import datetime
from cliente import Cliente
from conta import Conta

def save(cliente) -> bool:
    try:
        data = open("data.dat", "a")
        data.write(cliente.getNome())
        data.write("\n")
        data.write(cliente.getCpf())
        data.write("\n")
        data.write(cliente.getEndereco())
        data.write("\n")
        data.write(cliente.getTelefone())
        data.write("\n")
        data.write(str(cliente.getConta().getNumero()))
        data.write("\n")
        data.write(str(cliente.getConta().getTipo()))
        data.write("\n")
        data.write(str(cliente.getConta().getSaldo()))
        data.write("\n")
        data.close()
        return True
    except Exception as e:
        print(e)
        log(e)
        return False

def read(banco) -> int:
    cont = 0
    data = open("data.dat", "r")

    try:
        lines = data.readlines()

        for i in range(0, len(lines), 7):
            nome = lines[0+cont].strip('\n')
            cpf = lines[1+cont].strip('\n')
            endereco = lines[2+cont].strip('\n')
            telefone = lines[3+cont].strip('\n')
            numero = int(lines[4+cont].strip('\n'))
            tipo = lines[5+cont].strip('\n')
            saldo = float(lines[6+cont].strip('\n'))

            banco.cadastrar(Cliente(nome, cpf, endereco, telefone, Conta(numero, tipo, saldo)))
            cont = cont + 7

        data.close()
        return numero
    except Exception as e:
        print(e)
        log(e)
        return None

def check(banco) -> int:
    if os.path.exists('./data.dat'):
        if len(open("data.dat", "r").readlines()) > 2:
            numero = read(banco)
            if numero != None:
                print("Dados carregados com sucesso!\n")
                return numero       
            else:
                print("Houve um erro ao carregar os dados.\n")
                return None
    return None

def savePassword(password) -> None:
    data = open("utils.dat", "a")
    data.write(password)
    data.close()

def readPassword() -> str:
    if os.path.exists('./utils.dat'):
        data = open("utils.dat", "r")
        password = data.readline()
        data.close()
        return password
    return None

def log(error) -> None:
    data = open("logger.log", "a")
    time = datetime.now()
    data.write(str(time))
    data.write(" -> ")
    data.write(str(error))
    data.write("\n")
    data.close()

def viewLog() -> None:
    print("\nLogs:")
    if os.path.exists('./logger.log'):
        data = open("logger.log", "r")
        log = data.readlines()
        for i in range(len(log)):
            print(log[i].strip('\n'))
        data.close()
    else:
        print("Empty Log")