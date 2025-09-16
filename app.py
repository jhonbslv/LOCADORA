from classes import Locadora
from funcoes import menu, cadastrar_cliente, cadastrar_filme, cadastrar_jogo, locar_item, devolver_item

def main():
    locadora = Locadora()

    while True:
        menu()
        try:
            opcao = int(input("escolha uma opção: "))
        except ValueError:
            print("opção inválida, digite um número")
            continue

        match opcao:
            case 1:
                cadastrar_cliente(locadora)
            case 2:
                cadastrar_filme(locadora)
            case 3:
                cadastrar_jogo(locadora)
            case 4:
                locadora.listar_clientes()
            case 5:
                locadora.listar_itens()
            case 6:
                locar_item(locadora)
            case 7:
                devolver_item(locadora)
            case 0:
                print("saindo do sistema")
                break
            case _:
                print("opção inválida")

