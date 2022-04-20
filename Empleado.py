class Empleado:

    def __init__(self, id, nombre, apellido, usuario, password):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password

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

    def get_usuario(self):
        return self.usuario
    def set_usuario(self, usuario):
        self.usuario = usuario

    def get_password(self):
        return self.password
    def set_password(self, password):
        self.password = password