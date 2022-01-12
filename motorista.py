class Motorista:

    def __init__(self,id,nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"Motorista: {self.nome}! \n" \
               f"Identificador: {self.id}!"
motorista = Motorista(0,"Jose Maria")

print(motorista)
