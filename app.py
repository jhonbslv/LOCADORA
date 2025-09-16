from classes import Locadora
from funcoes import menu, cadastrar_cliente, cadastrar_filme, cadastrar_jogo, locar_item, devolver_item

def main():
    locadora = Locadora()

    while True:
        menu()
        try:
            opcao = int(input("escolha uma opção: "))
        except ValueError:
            print("opção inválida, digite um número.")
            continue

