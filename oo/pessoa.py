class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"

if __name__ == '__main__':
    Kaleu = Pessoa(nome="Kaleu")
    Andrey = Pessoa(Kaleu, nome = "Andrey")
    print(Pessoa.cumprimentar(Andrey))
    print(id(Andrey))
    print(Andrey.cumprimentar())
    print(Andrey.nome)
    print(Andrey.idade)
    for filho in Andrey.filhos:
        print(filho.nome)