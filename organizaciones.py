from enum import Enum
from re import S
import string

# class Organizaciones(Enum):
#     #parejas clave valor
#     avengers = 1
#     AForce = 2
#     MercsForMoney =3
#     LeagueOfRealms =4
#     StrangeAcademy = 5
#     XMen =6
#     # non nestoy seguro---ver si cambiar o no.+--- CREO Q NO ES ASI

class Organizacion():
    def __init__(self, x, y):   #     x-->nombre-----y-->lista de superheroes del equipo(min un superheroe)
        if type(x) != str:
            raise TypeError("not a name")
        elif type(y) != list:
            raise TypeError("not a list")                                                     #aqui hace falta todavia meter el tipo de guerrero(igual q en la clase nave-->no estoy de acuerdo con que se le pase y HAY Q CAMBIARLO)
        elif not y:
            raise ValueError("The team must have at least one superhero")
        else:
            self.__nombre = x
            self.__superheroes= y
#es muy importante que estos atributos sean privados porque ,por ejemplpo, no se puede cambiar el nombre de la organizacion.Sin embargo, no hay necesidad de hacer privados los metodos

    def get_nombre(self):
        return self.__nombre

    def get_superheroes(self):
        return self.__superheroes

    def set_superheroes(self,x):
        if type(x) != list:
            raise TypeError("not a list")
        if not x:
            raise ValueError("The team must have at least one superhero")
        self.__superheroes = x

    #Los nombres no se pueden cambiar, pero los superheroes pueden salir o entrar a distintas organizaciones, lo que es lógico. Por esta razón, no existe metodo set_nombre.

    def is_undefeated(self):
        x = False
        for i in range(len(self.__superheroes)):
            if self.__superheroes[i].is_vivo():
                x = True
                break
        return x
#compruebo que existe al menos un superheroe vivo en la lista de superheroes
    def surrender(self):
        for superheroe in self.__superheroes:
            superheroe.die()

    def __str__(self):
        tp = ""
        for superheroe in self.__superheroes:
            tp += str(superheroe.get_identificador()) + ". Alias: " + superheroe.get_alias() + ", Tipo:" +  superheroe.get_tipo().name + ", Coste:" + str(superheroe.get_coste()) + ", Energia:" + str(superheroe.get_energia()) + "\n" #repasar esto

        return tp

    def __repr__(self):
        tr = ""
        for superheroe in self.__superheroes:
            tr += superheroe.get_identificador() + "\t" + superheroe.get_tipo() + "\t" + superheroe.get_movimientos() + "\n"

        return tr

    def get_super_undefeated(self):
        sup_vivos = []
        for i in range(0, len(self.__superheroes)):
            if self.__superheroes[i].is_vivo():
                sup_vivos.append(self.__superheroes[i])

        return sup_vivos


        #tengase en cuenta que se esta tomando por defecto que la lista componentes de la organización esta compuesta por superheroes
        #falta definir el líder aspecto clave de la organizacion
