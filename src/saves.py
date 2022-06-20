def save(cliente) -> bool:
    try:
        data = open("data.dat", "a")
        data.write(str(cliente.getNome()))
        data.write("__")
        data.write(str(cliente.getCpf()))
        data.write("__")
        data.write(str(cliente.getEndereco()))
        data.write("__")
        data.write(str(cliente.getTelefone()))
        data.write("__")
        data.write(str(cliente.getConta().getNumero()))
        data.write("__")
        data.write(str(cliente.getConta().getTipo()))
        data.write("__")
        data.write(str(cliente.getConta().getSaldo()))
        data.write("\n")
        data.close()
        return True
    except Exception as e:
        print(e)
        return False

def read() -> bool:
    try:
        data = open("data.dat", "r")
        clients = data.readlines()

        data.close()
        return True
    except Exception as e:
        print(e)
        return False