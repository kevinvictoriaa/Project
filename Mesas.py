

class Mesas:

    def __init__(self, numero_mesas, cantidad_sillas, clientes):
        self.numero_mesas = numero_mesas
        self.cantidad_sillas = cantidad_sillas
        self.clientes = clientes

    def get_numeroMesas(self):
        return self.numero_mesas
    def set_numeroMesas(self, numeroMesas):
        self.numero_mesas = numeroMesas

    def get_Cantidad_Sillas(self):
        return self.cantidad_sillas
    def set_NumeroMesas(self, cantidad_sillas):
        self.cantidad_sillas = cantidad_sillas

    def get_Clientes(self):
        return self.clientes
    def set_numeroMesas(self, clientes):
        self.clientes = clientes