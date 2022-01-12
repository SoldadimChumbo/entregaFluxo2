from motorista import Motorista


class Fiscal (Motorista):
    def __str__(self):
        return f"Fiscal: {self.nome} \n" \
               f"Identificador: {self.id}"
fiscal = Fiscal(0, "José Maria")

print(fiscal)
