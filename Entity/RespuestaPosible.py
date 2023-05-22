import random
from Entity import Pregunta

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
        return self.getDescripcion()

    def mostrarPregunta(self):
        pregunta = self.buscarPregunta()
        return pregunta.getDescripcion()

    def mostrarEncuesta(self):
        pregunta = self.buscarPregunta() #todo
        return pregunta.mostrarEncuesta()

    def buscarPregunta(self):
        preguntasAleatorias = Pregunta.generarPreguntasAleatorias(3)
        for i in preguntasAleatorias:
            if self._descripcion in i.listarRespuestasPosibles():
                return i


def obtenerRespuestaCliente():
    descripcionesGenerales = ['1 al 10', 'Si/No']
    descripcion = random.choice(descripcionesGenerales)
    valoresGenerales = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    valor = random.choice(valoresGenerales)
    respuesta = RespuestaPosible("Al Usuario le gustan las milanesas",4)
    return respuesta
