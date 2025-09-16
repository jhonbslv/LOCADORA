class Item:
    def __init__(self, codigo: int, titulo: str):
        self.codigo = codigo
        self.titulo = titulo
        self.disponivel = True

    def alugar(self):
        if self.disponivel:
            self.disponivel = False
        else:
            raise Exception("Item já está alugado.")

    def devolver(self):
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"[{self.codigo}] {self.titulo} {status}"


class Filme(Item):
    def __init__(self, codigo: int, titulo: str, genero: str, duracao: int):
        super().__init__(codigo, titulo)
        self.genero = genero
        self.duracao = duracao

        def __str__(self):
            return f"Filme: {super().__str__()} Gênero: {self.genero} Duração: {self.duracao} min"


class Jogo(Item):
        def __init__(self, codigo: int, titulo: str, plataforma: str, faixaEtaria: int):
            super().__init__(codigo, titulo)
            self.plataforma = plataforma
            self.faixaEtaria = faixaEtaria

        def __str__(self):
            return f"Jogo: {super().__str__()} Plataforma: {self.plataforma} Faixa Etária: {self.faixaEtaria}+"

class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.itensLocados = []

    def locar(self, item: Item):
        if item.disponivel:
            item.alugar()
            self.itensLocados.append(item)
        else:
            raise Exception("Este item já está alugado.")

    def devolver(self, item: Item):
        if item in self.itensLocados:
            item.devolver()
            self.itensLocados.remove(item)
        else:
            raise Exception("Este item não foi alugado por este cliente.")

    def listarItens(self):
        if not self.itensLocados:
            print(f"{self.nome} não possui itens alugados.")
        else:
            print(f"Itens alugados por {self.nome}:")
            for item in self.itensLocados:
                print(f" - {item}")

    def __str__(self):
        return f"Cliente: {self.nome} CPF: {self.cpf}"


class Locadora:
    def __init__(self):
        self.clientes = []
        self.itens = []

    def cadastrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def cadastrar_item(self, item: Item):
        self.itens.append(item)

    def buscar_cliente(self, cpf: str):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def buscar_item(self, codigo: int):
        for item in self.itens:
            if item.codigo == codigo:
                return item
        return None

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def listar_itens(self):
        for item in self.itens:
            print(item)
