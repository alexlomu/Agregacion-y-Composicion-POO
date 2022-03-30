class Pared:
    def __init__(self, orientacion, ventana):
        self.orientacion = orientacion
        self.ventana = ventana


class Cristal:
    def __init__(self, pared, superficie, orientacion):
        Pared.__init__(self, orientacion)
        self.pared = pared
        self.superficie = superficie


class Casa:
    def __init__(self, paredes):
        self.paredes = paredes
    def superficie_cristal(self):
        superficie = 0
        for self.pared in Cristal.pared:
            for self.ventana in Pared.ventana:
                superficie += Cristal.superficie
        return superficie

pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = Pared("SUR") 
pared_este = Pared("ESTE") 

# Instanciación de las ventanas 
ventana_norte = Cristal(pared_norte, 0.5, "NORTE") 
ventana_oeste = Cristal(pared_oeste, 1, "OESTE") 
ventana_sur = Cristal(pared_sur, 2, "SUR") 
ventana_este = Cristal(pared_este, 1, "ESTE") 

# Instanciación de la casa con las 4 paredes 
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
print(casa.superficie_cristal()) 