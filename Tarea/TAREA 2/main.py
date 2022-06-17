class NodoLista_Doble_Enlasada(object):
    def __init__(self,valor=None, siguiente=None,anterior=None):
        self.valor=valor
        self.siguiente=siguiente
        self.anterior=anterior

class Lista_Doble_Enlasada(object):
    def __init__(self):
        self.cabeza=None
        self.cola=None

    def Insertar(self,valor):
        nodo=NodoLista_Doble_Enlasada(valor)  

        if (self.cabeza is None):
            self.cabeza =nodo
            self.cola=self.cabeza
        else:
            nodo.anterior=self.cola
            self.cola.siguiente=nodo
            self.cola=nodo

    def recorrerLista(self):
        actual = self.cabeza
        while(actual!=None):
            valor= actual.valor
            actual=actual.siguiente
            yield valor
            
    def buscar(self,valor):
        print("elementos de la lista  circular")
        aux=self.cabeza
        while(aux!=None):
            if(aux.valor==valor):
                print("Anterior: ", str(aux.anterior.valor))
                print("Actual: ",aux.valor)
                print("Siguiente:",aux.siguiente.valor)
            if(aux.siguiente==self.cabeza):
                return
            aux=aux.siguiente



numeros=Lista_Doble_Enlasada()
numeros.Insertar(1)
numeros.Insertar(2)
numeros.Insertar(3)
numeros.Insertar(4)
numeros.Insertar(5)

for recorridoo in numeros.recorrerLista():
    print(recorridoo)

numeros.buscar(4)