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
        
    def imprimirLista(self):
        aux=self.primero
        while(aux!=None):
            print("_____________________________________")
            print("El idclientees: ",aux.idcliente , "\nEl nombre del cliente: ",aux.nombreCliente,"\nEl idcarrito: ",aux.carrito)
            print("_____________________________________")
            aux=aux.siguiente
