class Onibus:
    def __init__(self,chassi):
        self.chassi = chassi
    def __str__(self):
        return f"Identificador do onibus: {self.chassi}"
onibus = Onibus(0)
print(onibus)