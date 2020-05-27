class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f"{cls} - olhos {cls.olhos}"

if __name__ == '__main__':
    Kaleu = Pessoa(nome = "Kaleu")
    Andrey = Pessoa(Kaleu, nome = "Andrey")
    print(Pessoa.cumprimentar(Andrey))
    print(id(Andrey))
    print(Andrey.cumprimentar())
    print(Andrey.nome)
    print(Andrey.idade)
    for filho in Andrey.filhos:
        print(filho.nome)
    Andrey.sobrenome = "Aires"
    del Andrey.filhos
    Andrey.olhos = 1
    del Andrey.olhos
    print(Andrey.__dict__)
    print(Kaleu.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Andrey.olhos)
    print(Kaleu.olhos)
    print(id(Pessoa.olhos), id(Andrey.olhos), id(Kaleu.olhos))
    print(Pessoa.metodo_estatico(), Andrey.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Andrey.nome_e_atributos_de_classe())

