class NodoCliente:
    def __init__(self,idcliente,nombreCliente,carrito):
        self.idcliente = idcliente
        self.nombreCliente = nombreCliente
        self.carrito = carrito
        self.siguiente = None
