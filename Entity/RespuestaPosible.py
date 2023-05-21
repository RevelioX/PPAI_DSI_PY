class RespuestaPosible:

    def __init__(self,descripcion,valor):
        self._descripcion = descripcion
        self._valor = valor

    def getDescripcion(self):
        return self._descripcion

    def setDescripcion(self,descripcion):
        self._descripcion = descripcion

    def getValor(self):
        return self._valor

    def setValor(self,valor):
        self._valor = valor

    def mostrarDatos(self):
        return (self.getDescripcion(), self.getValor())
