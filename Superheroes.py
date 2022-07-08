from enum import Enum
from multiprocessing.sharedctypes import Value
import random
from Escenarios import Escenarios
from SerVivo import SerVivo

class Superheroe_Type(Enum):
    HUMANO = 1
    NOHUMANO = 0

    def from_str(x):

        superheroe = x.upper()
        e = None

        for tp in Superheroe_Type:
            if superheroe == tp.name:
                e = tp
                break

        if type(e) != Superheroe_Type:
            raise TypeError("Invalid type for attribute tipo superheroe")

        return e


class Movimiento_Type(Enum):
    ATAQUE = 1
    DEFENSA = 0


class Movimientos_General():
    def __init__(self, x, a, daño):
        self.__nombre = x
        self.__tipo = a
        self.__daño = daño

    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo #varaible de tipo enum

    def get_daño(self):
        return self.__daño

    def set_daño(self, daño):
        self.__daño = daño


class Movimientos_Especifico(Movimientos_General):    #es el mismmo pero tiene asociado un superheroe
    def __init__(self, x, a, daño, superheroe):
        super().__init__(x, a, daño)
        self.__superheroe = superheroe

    def get_superheroe(self):
        return self.__superheroe


class Superheroes(SerVivo):

    numero_superheroes = 0 #variable global que comparten todas las instancias de tipo Superheroes

    def __init__(self,alias,identidadSecreta,tipo, esc):  #a partir de estos valores iniciales necesarios me construyo los atributos
        self.__identificador = Superheroes.numero_superheroes
        self.__alias = alias
        self.__identidadSecreta = identidadSecreta
        self.__movimientos = []
        self.__tipo = tipo    #solo pueden ser 2 HUMANO Y NO HUMANO sino error. este es un objeto de tipo enumerador-->Superheroe_Type.HUMANO o .NOHUMANO
        if type(tipo) != Superheroe_Type:
            raise TypeError("Invalid type for attribute tipo")
        elif tipo.value !=1 or tipo.value!=0:
            raise ValueError("introduzca un numero valido")
        elif tipo.value ==1:
            self.__parrilla_poderes = [random.randint(3,7),random.randint(1,6), random.randint(2,5), random.randint(2,5), random.randint(1,6), random.randint(1,7)]
        else:  #elif tipo.value ==0:
            self.__parrilla_poderes = [random.randint(4,6),random.randint(1,7), random.randint(1,7), random.randint(3,7), random.randint(1,7), random.randint(3,6)]
        if type(esc) != Escenarios:
            raise TypeError("Invalid type for attribute tipo")
        else:
            self.__coste = (esc.get_monedas()/esc.get_miembros_ekip())*(sum(self.__parrilla_poderes)/30)
            self._energia = (esc.get_energia_vital()*self.__parrilla_poderes[3]) #protegido-->las clases que hereden de Superheroes pueden cambiar este valor.
            Superheroes.numero_superheroes += 1

        #Identificar al siguiente superheroe en su posicion en la lista

    def get_identificador(self):
        return self.__identificador

    def get_alias(self):
        return self.__alias

    def get_movimientos(self):
        return self.__movimientos

    def get_tipo(self):
        return self.__tipo

    def get_parrillapoderes(self):
        return self.__parrilla_poderes

    def get_coste(self):
        return self.__coste

    def get_energia(self):
        return self._energia

    def isalive(self):
        return self.is_vivo()


    def set_movimientos(self,x):#cambia los mov. poniendo su valor real(en funcion del escenario)
        for movimiento in x:
            if movimiento.get_tipo().value ==1:
                movimiento.set_daño((movimiento.get_daño()/10)*(0.8*self.__parrilla_poderes[1] + 0.25*self.__parrilla_poderes[2] + 0.75*self.__parrilla_poderes[5] + self.__parrilla_poderes[4]))#pones el daño real
            else:
                movimiento.set_daño((movimiento.get_daño()/10)*(self.__parrilla_poderes[0] + 0.75*self.__parrilla_poderes[2] + 0.25*self.__parrilla_poderes[5] + 0.2*self.__parrilla_poderes[1]))
            self.__movimientos.append(movimiento)

    def fight_defense(self, daño):
        if type(daño) != int:
            raise TypeError("el daño tiene que ser un numero entero")
        else:
            self._energia = self._energia - daño
            if self._energia <= 0:
                self.die()
                self._energia = 0

    def fight_attack(self, rival):#no tiene sentido que se implemente el atributo hero porque el self ya es el hero
        posicion = random.randint(0,len(self.__movimientos))#cojo un numero al azar de ls lista de movimientos del superheroe
        rival.fight_defense(self.__movimientos[posicion].get_daño())

    def __str__(self):
        return str(self.get_identificador()) + "| Alias: " + self.get_alias() + "| Tipo:" + self.get_tipo().name + "| Coste:" + str(self.get_coste()) + "| Energia:" + str(self.get_energia()) + "\n"
