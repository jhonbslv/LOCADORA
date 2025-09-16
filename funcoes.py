from classes import Locadora, Cliente, Filme, Jogo

def menu():
    print("\nLocadora JHONIGACO")
    print("1 - cadastrar cliente")
    print("2 - cadastrar filme")
    print("3 - cadastrar jogo")
    print("4 - listar clientes")
    print("5 - listar itens")
    print("6 - locar item")
    print("7 - devolver item")
    print("0 - sair")


def cadastrar_cliente(locadora: Locadora):
    nome = input("nome do cliente: ")
    cpf = input("CPF do cliente: ")
    locadora.cadastrar_cliente(Cliente(nome, cpf))
    print("cliente cadastrado com sucesso!")


def cadastrar_filme(locadora: Locadora):
    try:
        codigo = int(input("código do filme: "))
        titulo = input("título: ")
        genero = input("gênero: ")
        duracao = int(input("duração (min): "))
        locadora.cadastrar_item(Filme(codigo, titulo, genero, duracao))
        print("filme cadastrado com sucesso!")
    except ValueError:
        print("entrada inválida. tente novamente.")


def cadastrar_jogo(locadora: Locadora):
    try:
        codigo = int(input("código do jogo: "))
        titulo = input("título: ")
        plataforma = input("plataforma: ")
        faixaEtaria = int(input("faixa etária: "))
        locadora.cadastrar_item(Jogo(codigo, titulo, plataforma, faixaEtaria))
        print("jogo cadastrado com sucesso!")
    except ValueError:
        print("entrada inválida. tente novamente.")


def locar_item(locadora: Locadora):
    cpf = input("CPF do cliente: ")
    cliente = locadora.buscar_cliente(cpf)
    if not cliente:
        print("cliente não encontrado.")
        return

    try:
        codigo = int(input("código do item: "))
        item = locadora.buscar_item(codigo)
        if not item:
            print("item não encontrado.")
            return

        cliente.locar(item)
        print(f"{cliente.nome} alugou '{item.titulo}' com sucesso!")
    except Exception as e:
        print(f"erro: {e}")


def devolver_item(locadora: Locadora):
    cpf = input("CPF do cliente: ")
    cliente = locadora.buscar_cliente(cpf)
    if not cliente:
        print("cliente não encontrado.")
        return

    try:
        codigo = int(input("código do item: "))
        item = locadora.buscar_item(codigo)
        if not item:
            print("item não encontrado.")
            return

        cliente.devolver(item)
        print(f"{cliente.nome} devolveu '{item.titulo}' com sucesso!")
    except Exception as e:
        print(f"erro: {e}")
