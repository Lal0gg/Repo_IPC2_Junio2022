from NodoCarrito import Nodocarrito

class PilaCarrito:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.sizeC=0

    def push(self,idcarrito):
        nuevo=Nodocarrito(idcarrito)
        if (self.primero==None):
            self.primero=nuevo
            self.sizeC+=1
        else:
            nuevo.anterior=self.ultimo
            self.ultimo.setSiguiente(nuevo)
            self.sizeC+=1
        self.ultimo=nuevo

    def imprimirPilaCarrito(self):
        print("Elementos de la lista")
        aux=self.primero
        while(aux!=None):
            print("Carrito:",aux.getId(), end=" --> ")
            aux=aux.siguiente
        
    def recorreCarrito(self):
        actual = self.primero
        while(actual!=None):
            idcarrito= primero.idcarrito
            primero=primero.siguiente
            yield idcarrito



    def pop(self):
        aux=self.ultimo
        if (aux.anterior!=None):
            self.ultimo=aux.anterior
            aux.anterior.siguiente=None
            self.sizeC-=1
        else:
            self.primero=None
            self.ultimo=None
        print("\n Se elimino el elemento ",aux.idcarrito)
        del aux







