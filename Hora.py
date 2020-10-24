from FechaHora import FechaHora

class Hora:
    __hora=0
    __minuto=0
    __segundo=0

    def __init__(self, hora=0, minuto=0, segundo=0):
        self.__hora=hora
        self.__minuto=minuto
        self.__segundo=segundo


    def getHora(self):
        return self.__hora

    def getMin(self):
        return self.__minuto

    def getSeg(self):
        return self.__segundo

    def Mostrar(self):
        s= " " +repr(self.__hora)+":"+repr(self.__minuto)+":"+repr(self.__segundo)
        print(s)


    def __radd__(self, otro):           ######otro=FECHAHORA // self=HORA
        h=self.getHora()+otro.getHora()
        m=self.getMin()+otro.getMin()
        s=self.getSeg()+otro.getSeg()
        aux=FechaHora(otro.getDIA(), otro.getMES(), otro.getANIO(), h, m, s)
        print("ESTOY en CLASE HORA en el radd")
        print("SELF: ", type(self))
        print("OTRO: ", type(otro))

        return aux

    def __add__(self, otro):
        print("Estoy en la clase HORA en el add")
        print("SELF", type(self))
        print("OTRO", type(otro))
        input()
        aux=self
        h=self.getHora()+otro.getHora()
        m=self.getMin()+otro.getMin()
        s=self.getSeg()+otro.getSeg()
        aux=FechaHora(otro.getDIA(), otro.getMES(), otro.getANIO(), h, m, s)
        return aux






















