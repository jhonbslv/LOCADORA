from funcoes import criar_locadora_exemplo, executar_operacao

if __name__ == "__main__":
    dados = criar_locadora_exemplo()
    if not dados:
        print("Não foi possível iniciar a locadora.")
        exit()

    locadora, cliente1, cliente2, filme1, jogo1 = dados

    while True:
        print("\nLocadora Jhonigaco")
        print("1 - Listar clientes")
        print("2 - Listar itens")
        print("3 - Locar filme")
        print("4 - Devolver filme")
        print("5 - Locar jogo")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if opcao == 0:
            print("Até logo! Obrigado por usar a locadora.")
            break

        executar_operacao(locadora, cliente1, filme1, jogo1, opcao)
