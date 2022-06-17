class Nodocarrito:
    def __init__(self,idcarrito):
        self.idcarrito=idcarrito
        self.anterior =None
        self.siguiente = None
    
    def setId(self,idcarrito):
        self.idcarrito = idcarrito
    
    def getId(self):
        return self.idcarrito
    
    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self,carrito):
        self.siguiente = carrito
