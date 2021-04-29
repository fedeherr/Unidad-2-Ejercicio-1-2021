from Email import Email
if __name__ == "__main__":
    bandera = False
    nomb = input("ingrese nombre de la persona ")
    while (not bandera):
        correocrear = input("ingrese email de la persona ")
        if '@' in correocrear:
            if '.' in correocrear:
                correo = Email()
                correo.crearCuenta(correocrear)
                print (correo.retornaEmail())
                print (f"Estimado {nomb} te enviaremos tus mensajes a la dirección {correocrear}")
                correo.cambiocontrasenia()
                bandera = True
            else: print("direccion invalida")
        else: print("direccion invalida")
    dom = input ("Ingrese dominio a buscar ")
    print ("Hay un total de " + str(correo.consultarDominios(dom)) + " direcciones con ese dominio")
    input()
        
        