


def menuEmpleados():
    op =0
    while op!=6:
        try:
            print("= = = = = =  MENÚ EMPLEADOS  = = = = = =")
            print("=   1.    Ver Empleado                 =")
            print("=   2.    Modificar                    =")
            print("=   3.    Eliminación                  =")            
            print("=   4.    Ver todo                     =")
            print("=   5     Generar Archivo              =")
            print("=   6.    Regresar al menú principal   =")
            print("= = = = = = = = = = = = = = = = = = =  = ")
            op=int(input("Ingrese la opción que desee: "))
            if(op ==1):
                print(" Viendo emmpleado gg")
            elif(op ==2):
                print("Modificar empleado")
            elif(op ==3):
                print("Eliminando disco")
            elif(op ==4):
                print("Ver todo el arbol")
            elif(op ==5):
                print("Generar archivo . . .")
            elif(op ==6):
                print("Regreando. . .")
                break
            else: 
                print("Ingrese una opción correcta plox :D")
        except Exception as e:
            print("Ingrese una opcion válida plox :)", e)


def menuReportes():
    opcion =0
    while opcion!=3:
        try:
            print("= = = = = = =  MENÚ REPORES  = = = = = = =")
            print("=   1.    Reporte de empleados           =")
            print("=   2.    Reporte de discos              =")
            print("=   3.    Regresar al menú principal     =")
            print("= = = = = = = = = = = = = = = = = = = =  =")
            opcion=int(input("Ingrese la opción que desee: "))
            if(opcion ==1):
                print("Reporte empleados (:")
            elif(opcion ==2):
                print("Reporte :Discos")
            elif(opcion ==3):
                print("Regreando. . .")
                break
            else: 
                print("Ingrese una opción correcta plox :D")
        except Exception as e:
            print("Ingrese una opcion válida plox :)", e)

def menuDiscos():
    opcion =0
    while opcion!=6:
        try:
            print("= = = = = = =  MENÚ DISCOS  = = = = = = =")
            print("=   1.    Ver Disco                     =")
            print("=   2.    Modificar                     =")
            print("=   3.    Eliminación                   =")            
            print("=   4.    Ver todo                      =")
            print("=   5     Generar Archivo               =")
            print("=   6.    Regresar al menú principal    =")
            print("= = = = = = = = = = = = = = = = = = = = =")
            opcion=int(input("Ingrese la opción que desee: "))
            if(opcion ==1):
                print("Ver disco gg")
            elif(opcion ==2):
                print("Modificar disco")
            elif(opcion ==3):
                print("Eliminar disco")
            elif(opcion ==4):
                print("Ver todo ")
            elif(opcion ==5):
                print("Generando archivo. . . ")
            elif(opcion ==6):
                print("Regresando . . .")
                break
            else: 
                print("Ingrese una opción correcta plox :D")
        except Exception as e:
            print("Ingrese una opcion válida plox :)", e)       


def Menu():
    opcion = 0
    while opcion!=5:
        try:
            print()
            print(" ___________________________________________________")
            print("|     .___  ___.  _______ .__   __.  __    __       |")  
            print("|     |   \/   | |   ____||  \ |  | |  |  |  |      |")   
            print("|     |  \  /  | |  |__   |   \|  | |  |  |  |      |")   
            print("|     |  |\/|  | |   __|  |  . `  | |  |  |  |      |")   
            print("|     |  |  |  | |  |____ |  |\   | |  `--'  |      |")   
            print("|     |__|  |__| |_______||__| \__|  \______/       |")  
            print("|___________________________________________________|")
            print(" ____________________________")
            print("| 1. Cargar datos            |")
            print("| 2. Gestión de Empleados    |")
            print("| 3. Gestión de discods      |")
            print("| 4. Reportes                |")
            print("| 5. Salir c:                |")
            print("|____________________________|")
            opcion = int(input("Ingrese la opción que desee: "))
            if opcion == 1:
                print("Hola, ingrese la ruta :D")
            elif opcion == 2:
                print("Hola, bienvenido a menu empleados :D")
                menuEmpleados()
            elif opcion == 3:
                print("Hola, bienvenido a menu discos :D")
                menuDiscos()
            elif opcion == 4:
                print("Hola, bienviedo a menu reportes :D ")  
                menuReportes()
            elif opcion == 5:
                print("Saliendo.....")
                print("Gracias por usar mi programda :v/ ")
                break
            else:
                print("Ingrese una opcion válida plox :D ")
        except Exception as e:
            print("Ingrese una opcion válida plox :)", e)




Menu()