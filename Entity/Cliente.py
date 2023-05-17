class Cliente:

    def __init__(self,dni, nombreCompleto, nroCelular):
        self._dni = dni
        self._nombreCompleto = nombreCompleto
        self._nroCelular = nroCelular

    def getNombre(self):
        return self._nombreCompleto
