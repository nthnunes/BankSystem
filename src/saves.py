import os
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
        return None

def check(banco) -> int:
    if os.path.exists('./data.dat'):
        numero = read(banco)
        if numero != None:
            print("Dados carregados com sucesso!\n")
            return numero       
        else:
            print("Houve um erro ao carregar os dados.\n")
            return None
    else:
        return None