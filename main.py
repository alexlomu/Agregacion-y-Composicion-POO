from Classes.ejercicioA import *
from Classes.ejercicioB import *
from Classes.ejercicioC import *

if __name__ == "__main__":
    ejercicio = input("Introduce a que ejercicio quieres acceder(a o c)")
    ejercicio = ejercicio.lower()
    if ejercicio == "a":
        print("Se va a eliminar la ciudad de Nueva York")
        Ciudad.catastrofe(NewYork)
    elif ejercicio == "c":
        pared_cortina = Cristal(pared_sur, 10, "SUR")
        casa.paredes[2] = pared_cortina 
        print(casa.superficie_cristal()) 
