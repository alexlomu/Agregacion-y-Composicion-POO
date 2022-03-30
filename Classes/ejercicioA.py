class Empleado:
    def __init__(self, empleado):
        self.empleado = empleado

class Edificio:
    def __init__(self, edificio, empleado):
        self.edificio = edificio
        self.empleado = empleado

class Ciudad:
    def __init__(self, ciudad, edificio, empleado):
        self.edificio = edificio
        self.empleado = empleado
        self.ciudad = ciudad
    def catastrofe(self, ciudad):
        del self.ciudad

class Empresa:
    def __init__(self, empresa, ciudad, edificio, empleado):
        self.empresa = empresa
        self.edificio = edificio
        self.empleado = empleado
        self.ciudad = ciudad

SresMartin = Empleado("SresMartin")
Salim = Empleado("Salim")
SraXing = Empleado("Sra. Xing")

ediA = Edificio("edificioA", SresMartin)
ediB = Edificio("edificioB", Salim)
ediC = Edificio("edificioC", SraXing)

NewYork = Ciudad("NewYork", [ediA, ediB], [SresMartin, Salim])
LosAngeles = Ciudad("LosAngeles", ediC, SraXing)

Yahoo = Empresa("Yahoo", [NewYork, LosAngeles], [ediA, ediB, ediC], [SresMartin, Salim, SraXing])
