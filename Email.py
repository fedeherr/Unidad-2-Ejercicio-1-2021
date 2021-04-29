import csv

class Email:
    __idCuenta = "a"
    __dominio = "xx"
    __tipodominio = "xx"
    __contrasenia = "default"

    def __init__(self, idCuenta = "a", dominio = "xx", tipodominio = "xx", contrasenia = "default"):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipodominio = tipodominio
        self.__contrasenia = contrasenia
    def retornaEmail(self):
        return"El email es %s@%s.%s" % (self.__idCuenta, self.__dominio,self.__tipodominio)
    def getDominio(self):
        return self.__dominio
    def crearCuenta(self, correo):
                x = correo.split("@",1)
                idc = x[0]
                x = x[1].split(".",1)
                dom = x[0]
                tipdom = x[1]
                self.__idCuenta = idc
                self.__dominio = dom
                self.__tipodominio = tipdom
    def consultarDominios(self, dominio):
        a = 0
        archivo = open('Emails.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                "'saltear cabecera'"
                bandera = not bandera
            else:
                if (fila[1] == dominio): a = a + 1
        return(a)
    def cambiocontrasenia(self):
        contra = input("Ingrese la contraseña actual (default por defecto): ")
        if (contra == self.__contrasenia):
            nuevacontra = input("Ingrese la nueva contraseña: ")
            self.__contrasenia = nuevacontra
        else: print ("Contraseña equivocada")