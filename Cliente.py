

class Cliente:
    def __init__(self, id, nombre, apellido, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono