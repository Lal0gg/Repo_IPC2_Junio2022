import os
from subprocess import check_output
from tokenize import Name
import xml.etree.ElementTree as ET

#arbol empleados
arbol1=None
#raiz empelados
raiz1=None
#arbol discos
raiz2=None
#arbol2 discos
arbol2=None

def menuEmpleados(raiz1):
    op =0
    while op!=6:
        try:
            print("")
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
                print(" Viendo emmpleado . . .")
                VerEmpleado(raiz1)
            elif(op ==2):
                print("Modificando empleado . . .")
                modfiicarEmpleado(raiz1)
            elif(op ==3):
                print("Eliminando empleado . . .")
                eliminarEmpelado(raiz1)
            elif(op ==4):
                print("Ver todo el arbol")
                MostrarEmpleados(raiz1)
            elif(op ==5):
                GenerarArchivoEmpleado()
                print("Generarando  archivo . . .")
            elif(op ==6):
                print("Regresando. . .")
                break
            else: 
                print("Ingrese una opción correcta plox :D")
        except Exception as e:
            print("Ingrese una opcion válida plox :)", e)

def MostrarEmpleados(raiz1):
    for departamento in raiz1:
        print('Departamento: ', departamento.attrib['departamento'])
        for empleado in departamento:
            print('\t ID: ', empleado.attrib['id'])
            print('\t\t Nombre: ', empleado.findall('nombre')[0].text)
            print('\t\t Puesto: ', empleado.findall('puesto')[0].text)
            print('\t\t Salario: ', empleado.findall('salario')[0].text)

def modfiicarEmpleado(raiz1):
    iddd = int(input("Ingrese el id del empleado: "))
    for departamento in raiz1:
        for empleado in departamento:
            idactual = int(empleado.attrib['id'])
            if(iddd==idactual):
                print('Departamento: ', departamento.attrib['departamento'])
                nuevoNombre = str(input("Ingrese el nuevo nombre: "))
                nuevoPuesto = str(input("Ingrese el nuevo puesto: "))
                nuevoSalario= str(input("Ingrese el nuevo salario: "))
                empleado.findall('nombre')[0].text=nuevoNombre
                empleado.findall('puesto')[0].text=nuevoPuesto
                empleado.findall('salario')[0].text=nuevoSalario
                print("Se han modificado los datos :D")
                return
    print("No se encontró el id")

def GenerarArchivoEmpleado():
    arbol1.write('nuevoEmpleado.xml',"utf-8")

def VerEmpleado(raiz1):
    iddd = int(input("Ingrese el id del empleado: "))
    for departamento in raiz1:
        for empleado in departamento:
            idactual = int(empleado.attrib['id'])
            if(iddd==idactual):
                print('Departamento: ', departamento.attrib['departamento'])
                print('\t __________________________________________________________________________________')
                print('\t| ID: ', empleado.attrib['id'])
                print('\t| Nombre: ', empleado.findall('nombre')[0].text,  end="|" )
                print('\t| Puesto: ', empleado.findall('puesto')[0].text,   end="|")
                print('\t| Salario: ', empleado.findall('salario')[0].text, end="|")
                print('\n\t|__________________________________________________________________________________|')
                return
    print("No se encontró el empleado :(")

def eliminarEmpelado(raiz1):
    iddd = int(input("Ingrese el id del empleado: "))
    for departamento in raiz1:
        for empleado in departamento:
            idactual=int(empleado.attrib['id'])
            if(iddd==idactual):
                departamento.remove(empleado)
                print("Empleado elminado")
                return
    print("No se encontró el empleado :( ")

def menuDiscos(raiz2):
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
                print("Viendo disco . . .")
                VerDisco(raiz2)
            elif(opcion ==2):
                print("Modificando disco . . .")
                ModificarDisco(raiz2)
            elif(opcion ==3):
                print("Eliminando disco . . .")
                EliminarDisco(raiz2)
            elif(opcion ==4):
                print("Viendo discos. . .")
                MostrarDiscos(raiz2)
            elif(opcion ==5):
                print("Generando archivo. . . ")
                GenerarArchivoDiscos()
            elif(opcion ==6):
                print("Regresando . . .")
                break
            else: 
                print("Ingrese una opción correcta plox :D")
        except Exception as e:
            print("Ingrese una opcion válida plox :)", e)       

def MostrarDiscos(raiz2):
    print("Catálogo de discos :D ")
    for cd in raiz2:
        print('\t CD:')
        print('\t\t  Title: ', cd.findall('title')[0].text)
        print('\t\t  Artist: ', cd.findall('artist')[0].text)
        print('\t\t  Country: ', cd.findall('country')[0].text)
        print('\t\t  Company: ', cd.findall('company')[0].text)
        print('\t\t  Price: ', cd.findall('price')[0].text)
        print('\t\t  Year: ', cd.findall('year')[0].text)
    print('\t Número de discos en el catálogo: ', len(raiz2) )

def VerDisco(raiz2):
    title=str(input("Ingrese el título: "))
    for cd in raiz2:
        titleactual = cd.findall('title')[0].text
        if( titleactual==title):
            print('\t CD:')
            print("\t\t  ________________________________________________________")
            print('\t\t | Title: ', cd.findall('title')[0].text)
            print('\t\t | Artist: ', cd.findall('artist')[0].text)
            print('\t\t | Country: ', cd.findall('country')[0].text)
            print('\t\t | Company: ', cd.findall('company')[0].text)
            print('\t\t | Price: ', cd.findall('price')[0].text)
            print('\t\t | Year: ', cd.findall('year')[0].text)
            print("\t\t |________________________________________________________")
            return
    print("No se encontró el title :( ")

def ModificarDisco(raiz2):
    title=str(input("Ingrese el título: "))
    for cd in raiz2:
        titleactual = cd.findall('title')[0].text
        if( titleactual==title):
            newArtist = str(input("Ingrese el nuevo Artist: "))
            newCountry =str(input("Ingrese el nuevo Country: "))
            newCompany =str(input("Ingrese la nueva Company: "))
            newPrice=str(input("Ingrese el nuevo  Price: "))
            newYear =str(input("Ingrese el nuevo Year: "))
            cd.findall('artist')[0].text = newArtist
            cd.findall('country')[0].text = newCountry
            cd.findall('company')[0].text = newCompany
            cd.findall('price')[0].text = newPrice  
            cd.findall('year')[0].text = newYear
            print("Se ha actualizado el title :D ")
            return
    print("No se encontró el title :(")

def EliminarDisco(raiz2):
    title=str(input("Ingrese el título: "))
    for cd in raiz2:
        titleactual = cd.findall('title')[0].text
        if( titleactual==title):
            raiz2.remove(cd)
            print("Se eliminó el CD")
            return
    print("No se encontró el title :(")

def GenerarArchivoDiscos():
    arbol2.write('nuevoDisco.xml',"utf-8")

def GraficarEmpleados(raiz1):
    
    contenido=""
    contenido+="digraph G { \n"
    contenido+='''node[shape=doublecircle,color=blue,fontname="Arial Black",style=filled,fillcolor="darkturquoise:aquamarine"] \n'''
    contenido+="nodoRaiz[label=\"Empresa\" fontsize=35] \n"

    for departamento in raiz1:
        NameNodoDep="nodoDepto"+departamento.attrib['departamento']

        contenido+=NameNodoDep+"[label=\""+departamento.attrib['departamento']+"\"] \n"

        contenido+="nodoRaiz ->"+NameNodoDep+"\n"

        for empleado in departamento:

            NameNodoIdEmp="nodoEmpl"+empleado.attrib['id']
            contenido+=NameNodoIdEmp+"[label=\"Empleado: "+empleado.attrib['id']+"\"] \n"
            contenido+=NameNodoDep+"->"+NameNodoIdEmp+"\n"

            #Nombre
            NameNodoNameEmp=NameNodoIdEmp+"name"
            nameEmp=empleado.findall('nombre')[0].text
            vargg=nameEmp.replace('"','\\"')
            contenido+=NameNodoNameEmp+"[label=\"Nombre: "+vargg+" \"] \n"
            contenido+=NameNodoIdEmp+"->"+NameNodoNameEmp+"\n"
            
            #Puesto
            NameNodoPuestoEmp=NameNodoIdEmp+"Puest"
            puestoEmp=empleado.findall('puesto')[0].text
            varg=puestoEmp.replace('"','\\"')
            contenido+=NameNodoPuestoEmp+"[label=\"Puesto: "+varg+" \"] \n"
            contenido+=NameNodoIdEmp+"->"+NameNodoPuestoEmp+"\n"
            
            #Salario
            NameNodoSalarioEmp=NameNodoIdEmp+"Salar"
            salarioEmp=empleado.findall('salario')[0].text
            varr=salarioEmp.replace('"','\\"')
            contenido+=NameNodoSalarioEmp+"[label=\"Salario: "+varr+" \"] \n"
            contenido+=NameNodoIdEmp+"->"+NameNodoSalarioEmp+"\n"


    contenido+="}"

    
    archivoDot=open("comandos/archivo.dot",'w',encoding="utf-8")
    archivoDot.write(contenido)
    archivoDot.close()

    #Print para verificar lo que escribimos
    print(contenido)

    #Ejecutar el comando en CMD
    comandoDot = "dot -Tjpg comandos/archivo.dot -o reportes/reporteEmpleados.jpg"
    check_output(comandoDot, shell=True)
    # comandoDot2 = "dot -Tjpg comandos/archivo.dot -o reportes/reporte2.jpg"
    # os.system(comandoDot2)

def GraficarDiscos(raiz2):
    contadorcd=1
    contenido=""
    contenido+="digraph G { \n"
    contenido+='''node[shape=doublecircle,color=blue,fontname="Arial Black",style=filled,fillcolor="darkturquoise:aquamarine"] \n'''
    contenido +='\nnodoRaiz[label=\"Catalog\" fontsize=35];\n'
    for cd in raiz2:
        
        NameNodocd="nodoCd"+str(contadorcd)
        contenido+=NameNodocd+"[label=\"Cd:  "+str(contadorcd)+"\"] \n"
        contenido+="nodoRaiz ->"+NameNodocd+"\n"
        #Title
        NameNodoNameTitle=NameNodocd+"title"
        titleCD=str(cd.findall('title')[0].text)
        var1=titleCD.replace('"','\\"')
        contenido+=NameNodoNameTitle+"[label=\"Title: "+var1+" \"] \n"
        contenido+=NameNodocd+"->"+NameNodoNameTitle+"\n"

        #Artist
        NameNodoNameArtist=NameNodocd+"artist"
        artistCD=str(cd.findall('artist')[0].text)
        var2=artistCD.replace('"','\\"')
        contenido+=NameNodoNameArtist+"[label=\"Artist: "+var2+" \"] \n"
        contenido+=NameNodocd+"->"+NameNodoNameArtist+"\n"

        #Country
        NameNodoNameCountry=NameNodocd+"country"
        countryCD=str(cd.findall('country')[0].text)
        var3=countryCD.replace('"','\\"')
        contenido+=NameNodoNameCountry+"[label=\"Country: "+var3+" \"] \n"
        contenido+=NameNodocd+"->"+NameNodoNameCountry+"\n"

        #Company
        NameNodoNameCompany=NameNodocd+"company"
        companyCD=str(cd.findall('company')[0].text)
        var4=companyCD.replace('"','\\"')
        contenido+=NameNodoNameCompany+"[label=\"Company: "+var4+" \"] \n"
        contenido+=NameNodocd+"->"+NameNodoNameCompany+"\n"
        
        #Price
        NameNodoNamePrice=NameNodocd+"price"
        priceCD=str(cd.findall('price')[0].text)
        var5=priceCD.replace('"','\\"')
        contenido+=NameNodoNamePrice+"[label=\"Price: "+var5+" \"] \n"
        contenido+=NameNodocd+"->"+NameNodoNamePrice+"\n"

        #Year
        NameNodoNameYear=NameNodocd+"year"
        yearCD=str(cd.findall('year')[0].text)
        var6=yearCD.replace('"','\\"')
        contenido+=NameNodoNameYear+"[label=\"Year: "+var6+" \"] \n"
        contenido+=NameNodocd+"->"+NameNodoNameYear+"\n"
        contadorcd+=1
    contenido+="}"

    archivoDot=open("comandos/archivo2.dot",'w',encoding="utf-8")
    archivoDot.write(contenido)
    archivoDot.close()
    print(contenido)
    #Ejecutar el comando en CMD

    comandoDot = "dot -Tjpg comandos/archivo2.dot -o reportes/reporteDiscos.jpg"
    check_output(comandoDot, shell=True)

    #comandoDot2 = "dot -Tjpg comandos/archivo.dot -o reportes/reporte2.jpg"
    os.system(comandoDot)

def VerificarArchivoExistente():    
    pass
def menuReportes(raiz1, raiz2):
    opcion =0
    while opcion!=3:
        try:
            print("")
            print("= = = = = = =  MENÚ REPORES  = = = = = = =")
            print("=   1.    Reporte de empleados           =")
            print("=   2.    Reporte de discos              =")
            print("=   3.    Regresar al menú principal     =")
            print("= = = = = = = = = = = = = = = = = = = =  =")
            opcion=int(input("Ingrese la opción que desee: "))
            if(opcion ==1):
                GraficarEmpleados(raiz1)
                print("Generando Reporte empelados. . .")
            elif(opcion ==2):
                GraficarDiscos(raiz2)
                print("Generando Reporte discos. . .")
            elif(opcion ==3):
                print("Regresando. . .")
                break
            else: 
                print("Ingrese una opción correcta plox :D")
        except Exception as e:
            print("Ingrese una opcion válida plox :)", e)

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
            print("___________________________________________")
            print("Hola, bienvenido a la carga de archivos :D ")
            print("1. Ingrese archivo empleados")
            print("2. Ingrese archivo discos")
            print("___________________________________________")
            op= int(input("Ingrese la opción que desee: "))
            try:
                if (op==1):
                    ruta1= str(input("Ingrese una ruta empleados: "))
                    try:
                        arbol1 = ET.parse(ruta1)
                        raiz1=arbol1.getroot()
                        print("Datos Cargados :D")
                    except Exception as e:
                        print("Error al abrir archivo",e)
                elif(op==2):
                    ruta2= str(input("Ingrese una ruta discos: "))
                    try:
                        arbol2 = ET.parse(ruta2)
                        raiz2=arbol2.getroot()
                        print("Datos Cargados :D")
                    except Exception as e:
                        print("Error al abrir archivo",e)
                else:
                    print("Ingrese un opcion correcta ")
            except Exception as e:
                        print("Ingrese una opción correcta",e)
                
        elif opcion == 2:
            print("Hola, bienvenido a menu empleados :D")
            menuEmpleados(raiz1)
        elif opcion == 3:
            print("Hola, bienvenido a menu discos :D")
            menuDiscos(raiz2)
        elif opcion == 4:
            print("Hola, bienviedo a menu reportes :D ")  
            menuReportes(raiz1, raiz2)
        elif opcion == 5:
            print("Saliendo.....")
            print("Gracias por usar mi programda :v/ ")
            break
        else:
            print("Ingrese una opcion válida plox :D ")
    except Exception as e:
        print("Ingrese una opcion válida plox :)", e)
