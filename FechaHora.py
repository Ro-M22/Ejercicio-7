
class FechaHora:
    __dia = 0
    __mes = 0
    __año = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__(self, dia=1, mes=1, año=2020, hora=0, minutos=0, segundos=0):
        self.__dia = dia
        self.__mes = mes
        self.__año = año
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos

    def __str__(self):
        return 'Fecha:{}/{}/{} \n Hora: {}:{}:{}'.format(self.__dia, self.__mes, self.__año, self.__hora,
                                                         self.__minutos, self.__segundos)

    def getHora(self):
        return self.__hora

    def getMin(self):
        return self.__minutos

    def getSeg(self):
        return self.__segundos

    def getDIA(self):
        return self.__dia

    def getMES(self):
        return self.__mes

    def getANIO(self):
        return self.__año

        # def __add__(self, otraHora):
        #    return FechaHora(self.__hora + otraHora.getHora(), self.__minutos + otraHora.getMin(), self.__segundos + otraHora.getSeg())

    #def __add__(self, otraFecha):
     #   print("Estoy en la clase HORA en el add")
      #  print("SELF", type(self))
       # print("OTRO", type(otraFecha))
       # input()
       # aux = self
       # h = self.getHora() + otraFecha.getHora()
       # m = self.getMin() + otraFecha.getMin()
       # s = self.getSeg() + otraFecha.getSeg()

        #aux = FechaHora(otraFecha.getDIA(), otraFecha.getMES(), otraFecha.getANIO(), h, m, s)
        #return aux

    def __sub__(self, otraFecha):
        print("Estoy en la clase HORA en el add")
        print("SELF", type(self))
        print("OTRO", type(otraFecha))
        input()
        aux = self
        h = self.getHora() - otraFecha.getHora()
        m = self.getMin() - otraFecha.getMin()
        s = self.getSeg() - otraFecha.getSeg()

        aux = FechaHora(otraFecha.getDIA(), otraFecha.getMES(), otraFecha.getANIO(), h, m, s)
        return aux


    def __gt__(self, otraFecha):
        print("Estoy en la clase HORA en el add")
        print("SELF", type(self))
        print("OTRO", type(otraFecha))
        input()
        aux = self
        h = self.getHora() > otraFecha.getHora()
        if h==False:
            H=otraFecha.getHora()
        else:
            H=self.getHora()

        m = self.getMin() > otraFecha.getMin()
        if m==False:
            M=otraFecha.getMin()
        else:
            M=self.getMin()
        s = self.getSeg() > otraFecha.getSeg()
        if s==False:
            S=otraFecha.getSeg()
        else:
            S=self.getSeg()
        print("Resultados de comparaciones:")
        print("¿Hora 1 es Mayor comparado con Hora 2?\n ", h,":"" ",m,":"" ",s)
        aux = FechaHora(otraFecha.getDIA(), otraFecha.getMES(), otraFecha.getANIO(), H, M, S)

        return aux


    def ponerEnHora(self, hora=0, minuto=0, segundo=0):
        self.__hora = hora
        self.__minutos = minuto
        self.__segundos = segundo

    def Mostrar(self):
        s=' ' + repr(self.__dia) + '/' + repr(self.__mes) + '/' + repr(self.__año) + ' '+repr(self.__hora)+':'+repr(self.__minutos)+':'+repr(self.__segundos)
        #repr muestra lo imprimible
        print(s)

    def AdelantarHora(self, hora=0, minuto=0, seg=0):
        self.__hora+=int(hora)
        self.__minutos+=int(minuto)
        self.__segundos+=int(seg)
        if self.__segundos>59:
            self.__segundos = self.__segundos-60
            self.__minutos+=1
        if self.__minutos>59:
            self.__minutos = self.__minutos-60
            self.__hora+=1
        if self.__hora>=24:
            self.__hora = self.__hora-24
            self.__dia=self.__dia+1
        if (self.__mes==11 or self.__mes==4 or self.__mes==6 or self.__mes==9):
            if self.__dia>30:
                self.__dia-=30
                self.__mes+=1

            else:
                if (self.__mes==1 or self.__mes==3 or self.__mes==5 or self.__mes==7 or self.__mes==8 or self.__mes==10 or self.__mes==12):
                    if self.__dia>31:
                        if self.__mes==12:
                            self.__año+=1
                            self.__mes=1
                        else:
                            self.__mes+=1
                            self.__dia-=31

                    else:
                        if bisiesto (self.__año):
                            if self.__dia>29:
                                self.__dia-=29
                        else:
                            if self.__dia>28:
                                self.__dia-=28
                        self.__mes+=1

def bisiesto(a):
    if a %4==0 and a %100 !=0 or a %400==0:
        return True
    else:
        return False

def valida (d, mes, a, h, m, s):
    if (a in range (3000)):
        if (mes in range(13)):
            if (mes==11 or mes==4 or mes==6 or mes==9):
                if (d in range(30)):
                    if (h in range(24)):
                        if (m in range(60)):
                            if (s in range(60)):
                                return True
                            else:
                                print("Los valores válidos son de 0..59")
                                return False
                        else:
                            print("Los valores válidos son de 0..59")
                            return False
                    else:
                        print("Los valores válidos son de 1..23")
                        return False
                else:
                    print("Los valores válidos para dias en el mes ", mes," son de 1..30")
                    return False
            else:
                if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==10 or mes==12):
                    if (d in range(31)):
                        if (h in range(24)):
                            if (m in range(60)):
                                if (s in range(60)):
                                    return True
                                else:
                                    print("Los valores válidos son de 0..59")
                                    return False
                            else:
                                print("Los valores válidos son de 0..59")
                                return False
                        else:
                            print("Los valores válidos son de 1..23")
                            return False
                    else:
                        print("Los valores válidos para dias en el mes ", mes, " son de 1..31")
                        return False
                else:
                    if (mes==2 and bisiesto(a)):
                        if (d in range(1, 30)):
                            if (h in range(24)):
                                if (m in range(60)):
                                    if (s in range(60)):
                                        return True
                                    else:
                                        print("Los valores válidos son de 0..59")
                                        return False
                                else:
                                    print("Los valores válidos son de 0..59")
                                    return False
                            else:
                                print("Los valores válidos son de 1..23")
                                return False
                        else:
                            print("Los valores válidos para dias en el mes ", mes, " son de 1..29")
                            return False
                    else:
                        if (d in range(1,29)):
                            if (h in range(24)):
                                if (m in range(60)):
                                    if (s in range(60)):
                                        return True
                                    else:
                                        print("Los valores válidos son de 0..59")
                                        return False
                                else:
                                    print("Los valores válidos son de 0..59")
                                    return False
                            else:
                                print("Los valores válidos son de 1..23")
                                return False
                        else:
                            print("Los valores válidos para dias en el mes ", mes, " son de 1..28")
                            return False





#d=int(input("Ingrese Dia: "))
#mes=int(input("Ingrese Mes: "))
#a=int(input("Ingrese Año: "))
#h=int(input("Ingrese Hora: "))
#m=int(input("Ingrese Minutos: "))
#s=int(input("Ingrese Segundos: "))
#gere=FechaHora(d,mes,a,h,m,s)







