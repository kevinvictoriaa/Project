

class Mesero(Empleado):

    def __init__(self, mesas):
        self.mesas = mesas

    def get_mesas(self):
        return self.mesas
    def set_mesas(self, mesas):
        self.mesas = mesas