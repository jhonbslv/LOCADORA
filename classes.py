class Item:
    def __init__(self, codigo: int, titulo: str):
        self.codigo = codigo
        self.titulo = titulo
        self.disponivel = True  
    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            return f"Você alugou '{self.titulo}' com sucesso!"
        return f"O item '{self.titulo}' já está alugado."

    def devolver(self):
        self.disponivel = True
        return f" '{self.titulo}' foi devolvido e já está disponível."


class Filme(Item):
    def __init__(self, codigo: int, titulo: str, genero: str, duracao: int):
        super().__init__(codigo, titulo)
        self.genero = genero
        self.duracao = duracao

    def __str__(self):
        return f" Filme: {self.titulo} | {self.genero} - {self.duracao} min"


class Jogo(Item):
    def __init__(self, codigo: int, titulo: str, plataforma: str, faixaEtaria: int):
        super().__init__(codigo, titulo)
        self.plataforma = plataforma
        self.faixaEtaria = faixaEtaria

    def __str__(self):
        return f"Jogo: {self.titulo} | {self.plataforma} - {self.faixaEtaria}+"


class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.itensLocados = []

    def locar(self, item: Item):
        if item.disponivel:
            resp = item.alugar()
            self.itensLocados.append(item)
            return resp
        return f"O item '{item.titulo}' já está alugado por outra pessoa."

    def devolver(self, item: Item):
        if item in self.itensLocados:
            resp = item.devolver()
            self.itensLocados.remove(item)
            return resp
        return f"Você não alugou '{item.titulo}'."

    def listarItens(self):
        if not self.itensLocados:
            return f"ℹ {self.nome} não tem nada alugado no momento."
        lista = "\n".join([f" - {item}" for item in self.itensLocados])
        return f"Itens alugados por {self.nome}:\n{lista}"


class Locadora:
    def __init__(self):
        self.clientes = []
        self.itens = []

    def cadastrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        return f"Cliente '{cliente.nome}' cadastrado com sucesso!"

    def cadastrar_item(self, item: Item):
        self.itens.append(item)
        return f"Item '{item.titulo}' adicionado ao catálogo."

    def listar_clientes(self):
        if not self.clientes:
            return "ℹ Nenhum cliente cadastrado ainda."
        return "\n".join([f" - {c.nome} (CPF: {c.cpf})" for c in self.clientes])

    def listar_itens(self):
        if not self.itens:
            return "ℹ Nenhum item cadastrado ainda."
        return "\n".join([
            f" - {i} | {'Disponível' if i.disponivel else 'Alugado'}"
            for i in self.itens
        ])
