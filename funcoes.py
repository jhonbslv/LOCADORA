from classes import Filme, Jogo, Cliente, Locadora

def criar_locadora_exemplo():
    locadora = Locadora()
    try:
        c1 = Cliente("João Silva", "123.456.789-00")
        c2 = Cliente("Maria Souza", "987.654.321-00")
        print(locadora.cadastrar_cliente(c1))
        print(locadora.cadastrar_cliente(c2))

        f1 = Filme(1, "Vingadores", "Ação", 140)
        j1 = Jogo(2, "The Last of Us", "PlayStation", 18)
        print(locadora.cadastrar_item(f1))
        print(locadora.cadastrar_item(j1))

        return locadora, c1, c2, f1, j1
    except Exception as e:
        print(f"Erro ao configurar os dados iniciais: {e}")


def executar_operacao(locadora, cliente, filme, jogo, opcao):
    """
    Recebe uma opção do menu e usa match-case para decidir a ação.
    """
    try:
        match opcao:
            case 1:
                print(locadora.listar_clientes())
            case 2:
                print(locadora.listar_itens())
            case 3:
                print(cliente.locar(filme))
            case 4:
                print(cliente.devolver(filme))
            case 5:
                print(cliente.listarItens())
            case 6:
                print(cliente.locar(jogo))
            case _:
                print("Escolha uma opção certa.")
    except Exception as e:
        print(f"Algo deu errado: {e}")
