class Carta:
    """
    La clase Carta define una carta y para iniciarla
    hay que definir los atributos número y palo
    """
    
    def __init__(self, palo, numero):
        self._palo = palo        #definimos atributo palo
        self._numero = numero    #definimos atribto n'úmero de carta
        
    def __repr__(self):
        return self._numero + " de " + self._palo #este metodo representa una carta
    
    @property        #el decorador property necesita un método getter (coger),tiene retorno
    def palo(self):
        return self._palo
    
    @palo.setter     #el decorador atributo.setter(establecer) no lleva retorno
    def palo(self, palo):
        if palo in ["oros", "copas", "espadas", "bastos"]:
            self._palo = palo
        else:
            print("¡Esto no es un palo!")
            
    @property      #el decorador property necesita un método getter (coger),tiene retorno
    def numero(self):
        return self._numero

    @numero.setter #el decorador atributo.setter(establecer) no lleva retorno
    def numero(self, numero):
        valid = [str(n) for n in range(1,8)] + ["Sota", "Caballo", "Rey"]
        if numero in valid:
            self._numero = numero
        else:
            print("Este número no es válido")
    

mi_carta = Carta("espadas", "7") #objeto concreto de la clase Carta

#ordenes
print (mi_carta) #imprime mi carta

class Mazo:
    """
    La clase Mazo define un mazo de cartas en orden
    """

    def __init__(self):
        self._cartas = []
        self.populate()
        print(self._cartas)
        
        
    def populate(self):
        palos = ["oros", "copas", "espadas", "bastos"]
        numeros = [str(n) for n in range(1,8)]+["Sota", "Caballo", "Rey"]    
        self._cartas = [ Carta(p, n) for p in palos for n in numeros ]
        
    def __repr__(self):
        cartas_en_mazo = len(self._cartas)
        return "Mi mazo contiene " + str(cartas_en_mazo) + " cartas en total"
        
mi_mazo = Mazo()

print(mi_mazo)

            
