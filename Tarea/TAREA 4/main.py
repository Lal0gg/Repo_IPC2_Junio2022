import xml.etree.ElementTree as ET
raiz1 = None
arbol1 = None
def MostrarDiscos(raiz1):
    anio=str(input("Ingrese el año del cd: "))
    print("Catálogo de discos :D ")
    conta=0 
    for cd in raiz1:
        anioactual= cd.findall('year')[0].text
        if(anio==anioactual):
            print("\t___________________________________________")
            print('\t CD:')
            print('\t\t  Title: ', cd.findall('title')[0].text)
            print('\t\t  Artist: ', cd.findall('artist')[0].text)
            print('\t\t  Country: ', cd.findall('country')[0].text)
            print('\t\t  Company: ', cd.findall('company')[0].text)
            print('\t\t  Price: ', cd.findall('price')[0].text)
            print('\t\t  Year: ', cd.findall('year')[0].text)
            conta+=1
    print('\t Número de discos con la misma fecha: ', conta)
    return
def menuDiscos(raiz1):
    op=0
    while op!=3:
        try:
            print(" = = = = = = = = = = = = = = =")
            print(" 1. Cargar Datos: ")
            print(" 2. Buscar Discos por año: ")
            print(" 3. Salir")
            print(" = = = = = = = = = = = = = = =")
            op = int(input("Ingres la opción: "))
            if(op ==1):
                ruta1 = str(input("Ingrese una ruta discos: "))
                try:
                    arbol1 = ET.parse(ruta1)
                    raiz1 = arbol1.getroot()
                    print("Datos Cargados :D")
                except Exception as e:
                    print("Error al abrir archivo", e)
            elif(op==2):
                MostrarDiscos(raiz1)
            elif(op==3):    
                print("bye . . .")
                break
            else:
                print("Ingrese una opción valida")
        except Exception as e:
            print("Ingrese una opción válida",e)
menuDiscos(raiz1)
