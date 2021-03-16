class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes += 1




vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
vingadores.dar_like()
print(f'nome: {vingadores.nome} - Ano: {vingadores.ano}  - Temporadas: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
print(f'nome: {atlanta.nome} - Ano: {atlanta.ano}  - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')