# funcoes.py
from classes import Locadora, Cliente, Filme, Jogo

def menu():
    print("\n📀 Sistema de Locadora 📀")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar filme")
    print("3 - Cadastrar jogo")
    print("4 - Listar clientes")
    print("5 - Listar itens")
    print("6 - Locar item")
    print("7 - Devolver item")
    print("0 - Sair")


def cadastrar_cliente(locadora: Locadora):
    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    locadora.cadastrar_cliente(Cliente(nome, cpf))
    print("✅ Cliente cadastrado com sucesso!")


def cadastrar_filme(locadora: Locadora):
    try:
        codigo = int(input("Código do filme: "))
        titulo = input("Título: ")
        genero = input("Gênero: ")
        duracao = int(input("Duração (min): "))
        locadora.cadastrar_item(Filme(codigo, titulo, genero, duracao))
        print("filme cadastrado com sucesso!")
    except ValueError:
        print("entrada inválida. Tente novamente.")


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
        print(f"✅ {cliente.nome} alugou '{item.titulo}' com sucesso!")
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
