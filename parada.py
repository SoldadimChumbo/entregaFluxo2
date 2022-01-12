from motorista import Motorista


class Parada(Motorista):

    def __str__(self):
        return f"Ponto de parada: {self.nome}"

parada = Parada(0,"Pantanal")
print(parada)
