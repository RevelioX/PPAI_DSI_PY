class Estado:

    def __init__(self, nombre):
        self._nombre = nombre

    def esIniciada(self):
        if self._nombre == "Iniciada":
            return True
        else:
            return False

    def esFinalizada(self):
        if self._nombre == "Finalizada":
            return True
        else:
            return False

    def getNombre(self):
        return self._nombre