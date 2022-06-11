from NodoCarrito import Nodocarrito
from ListaCliente import ListaCliente
from NodoCliente import NodoCliente
from PilaCarrito import PilaCarrito

PilaCarritoo = PilaCarrito()
ListaClientee =ListaCliente()

def CrearCarritos():
    try:
        caarrito = int(input("Ingrese el número de carritos que desee : "))
        if(caarrito>0):
            for i in range(caarrito):
                carrito=i+1
                PilaCarritoo.push(carrito)
            
            print("\nSe agregaron los carritos correctamente :) ")
        else:
            print("Ingrese un número positivo plos :D")
    except Exception as e:
            print("Ingrese una opcion válida plox :)", e)
idcliente1=1
def AgregarClientes():
    global idcliente1 
    nombreCliente =str(input("Ingrese su nombre: "))
    if (PilaCarritoo.sizeC>0):
        carrito1 =PilaCarritoo.pop()
        ListaClientee.insertarCliente(idcliente1,nombreCliente,carrito1)
        idcliente1+=1
        print("Se agregó el cliente con éxito :) ")
    else:
        print("No hay usuarios registrados")

def verCliente():
    idcliente1 = int(input("Ingrese el id cliente: "))
    if(ListaClientee.busqueda(idcliente1) is not None):
        ListaClientee.busqueda(id)
        print()
        

def Menu():
    opcion = 0
    while opcion!=6:
        try:
            print()
            print(" ___________________________________________")
            print("| 88888b d88888                             |")
            print("| 888Y88888P888   d88b   88888b   888  888  |")
            print("| 888 Y888P 888 d8P  Y8b 888  88b 888  888  |")
            print("| 888  Y8P  888 88888888 888  888 888  888  |")
            print("| 888       888 Y8b      888  888 Y88b 888  |")
            print("| 888       888   Y8888  888  888  Y88888   |")
            print("|___________________________________________|")
            print(" _______________________")
            print("| 1. Ingreso de datos   |")
            print("| 2. Nuevo cliente      |")
            print("| 3. Ver cliente        |")
            print("| 4. Caja registradora  |")
            print("| 5. Visualizar Datos   |")
            print("| 6. Salir              |")
            print("|_______________________|")
            opcion = int(input("Ingrese la opción que desee: "))
            if opcion == 1:
                print("Hola, ingrese los datos :D")
                CrearCarritos()
            elif opcion == 2:
                print("Hola, inngrese el nuevo cliente :D")
                AgregarClientes()
            elif opcion == 3:
                print("Acá puede ver los clientes :D ")
                verCliente()

            elif opcion == 4:
                print("Hola, acá es la caja registradora :D ")
            elif opcion == 5:
                print("Hola, acá puede visualizar los datos :D ")
                print("Carritos: ")
                PilaCarritoo.imprimirPilaCarrito()
                print("\nClientes: ")
                ListaClientee.imprimirLista()
            elif opcion == 6:
                print("Saliendo.....")
                print("Gracias por usar mi programda :v/ ")
                break
            else:
                print("Ingrese una opcion válida plox :D ")
        except Exception as e:
            print("Ingrese una opcion válida plox :)", e)
Menu()


