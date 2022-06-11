from NodoCliente import NodoCliente

class ListaCliente:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size=0
    
    def insertarCliente(self,idcliente,nombreCliente,idcarrito):
        aux=NodoCliente(idcliente,nombreCliente,idcarrito)
        if(self.primero==None):
            self.primero=aux
            self.size+=1
        else:
            self.ultimo.siguiente=aux
            self.size+=1
        self.ultimo=aux
    
    def busqueda(self,idcliente):
        aux=self.primero
        while(aux!=None):
            if(aux.idcliente==idcliente):
                print("_____________________________________")
                print("ID cliente: ", str(aux.idcliente), "\nNombre del Cliente:",str(aux.nombreCliente),"\nEl id carrito",str(aux.carrito))
                print("_____________________________________")
                return
            aux=aux.siguiente
        print("No se encontró el valor D:")

    def imprimirLista(self):
        aux=self.primero
        while(aux!=None):
            print("_____________________________________")
            print("El idclientees: ",str(aux.idcliente) , "\nEl nombre del cliente: ",str(aux.nombreCliente),"\nEl idcarrito: ",str(aux.carrito),end="")
            print("\n_____________________________________")
            aux=aux.siguiente
