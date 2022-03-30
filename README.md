# Agregacion-y-Composicion-POO
El link de este repositorio es: [Github](https://github.com/alexlomu/Agregacion-y-Composicion-POO)
https://github.com/alexlomu/Agregacion-y-Composicion-POO.
Para esta entrega hemos tenido que resolver un total de 3 problemas, que vienen a continuación.
# Ejercicio a) El dia siguiente
Para este ejercicio hemos tenido que realizar un código en el cual se definen ciudades, edificios y trabajadores de una empresa y crear una función que elimine una de estas ciudades, New York.
El código propuesto es el siguiente(hay que tener en cuenta que New York se elimina desde el archivo main.py):
```
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

```

# Ejercicio b) ¿Inmortal?
En este ejercicio nos pedían responder unas preguntas respecto a un código dado. El código en cuestión es el siguiente:
```
class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 
print(yang) 
#>>> <__main__.Yang object at 0x1011da828> 
print(yang is yin.yang) 
#>>> True 
del(yang) 
print("?") 
#>>> ? 
#Yang destruido
```

Las preguntas con sus respectivas respuestas son:
```
Teniendo en cuenta el siguiente código, explique por qué el mensaje Yang destruido, se muestra después del signo de interrogación. ¿Qué hay que hacer para que aparezca antes?
Se muestra primero el interrogante porque no se accede correctamente a la clase Yang ya que no es un atributo de Ying, para que apareciese primero tendriamos que hacer que Yang dejase de ser privado, es decir, ejecutar primero ambas clases correctamente.
```

# Ejercicio c) Alternativa a la herencia múltiple
Para este ejercicio teníamos que modificar unas clases de un código que usamos en una entrega anterior. El código queda de la siguiente manera:
```
class Pared:
    def __init__(self, orientacion, ventanas):
        self.orientacion = orientacion
        self.ventanas = []
        self.ventanas = ventanas

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
        for pared in Cristal.pared:
            for ventana in Pared.ventanas:
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
```
