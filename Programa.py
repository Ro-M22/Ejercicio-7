from Hora import Hora
from FechaHora import FechaHora

####################################################VALIDA EN MAIN##
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

####################################################FIN VALIDA###

if __name__ == '__main__':

    d=int(input("\n -Ingrese Dia: "))
    mes=int(input("\n -Ingrese Mes: "))
    a=int(input("\n -Ingrese Año: "))
    h=int(input("\n -Ingrese Hora: "))
    m=int(input("\n -Ingrese Minutos: "))
    s=int(input("\n -Ingrese Segundos: "))

    ##validar = valida()CREAR CLASE VALIDA

    if valida(d, mes, a, h, m, s):
       f = FechaHora(d, mes, a, h, m, s)
       f.Mostrar()
       input()
       h1 = int(input("h1= Ingrese Hora: "))
       m1 = int(input("m1= Ingrese Minutos: "))
       s1 = int(input("s1= Ingrese Segundos: "))
       r = Hora(h, m, s)
       print("\t\tmuestro R: ")
       r.Mostrar()
       input("presione Enter")
       print("sumo f+r\n")
       f2 = f + r
       f2.Mostrar()
       print("fin mostrar F2")
       input("enter para ver f3")
       f3 = r + f
       f3.Mostrar()
       print("FIN F3\n")
       input("enter")
       f4 = f3 - 1  # Al restar un número entero a un objeto FechaHora se debe restar la cantidad de
       # días indicada por el número entero
       f4.Mostrar()
       f4 = 1 + f2  # suma un día a un objeto FechaHora
       input()
    else:
         print('______________________________________________________ ')
         print('\n\t >> Ingreso de datos incorrecto << ')
         print(' \t >> Intentelo de nuevo más tarde <<')
         print('______________________________________________________\n ')