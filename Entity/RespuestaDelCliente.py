import datetime
import random
from datetime import datetime
from Entity import RespuestaPosible


class RespuestaDelCliente:

    def __init__(self, fechaEncuesta, respuestaSeleccionada):
        self._fechaEncuesta = fechaEncuesta
        self._respuestaSeleccionada = respuestaSeleccionada

    def getDescripcionRta(self):
        return self._respuestaPosible.getDescripcion()

    def getFechaEncuesta(self):
        return self._fechaEncuesta

    def setFechaEncuesta(self, fechaEncuesta):
        self._fechaEncuesta = fechaEncuesta

    def getRespuestaPosible(self):
        return self._respuestaPosible

    def setRespuestaPosible(self, respuestaPosible):
        self._respuestaPosible = respuestaPosible

    def mostrarDatosRTA(self):
        return self._respuestaSeleccionada.mostrarDatos()

    def mostrarPregunta(self):
        return self._respuestaSeleccionada.mostrarPregunta()

    def mostrarEncuesta(self):
        return self._respuestaSeleccionada.mostrarEncuesta()


def respuesEncuesta():
    nroRandom = random.randint(0, 1)
    respuestasV = []
    if nroRandom != 0:
        for i in range(1):
            anio_aleatorio = random.randint(2015, 2023)
            mes_aleatorio = random.randint(1, 12)
            dia_aleatorio = random.randint(1, 27)
            respuesta = RespuestaPosible.obtenerRespuestaCliente(1)
            fechaRandom = datetime(anio_aleatorio, mes_aleatorio, dia_aleatorio)
            respuestasV.append(RespuestaDelCliente(fechaRandom, respuesta))
        for i in range(1):
            anio_aleatorio = random.randint(2015, 2023)
            mes_aleatorio = random.randint(1, 12)
            dia_aleatorio = random.randint(1, 27)
            respuesta = RespuestaPosible.obtenerRespuestaCliente(2)
            fechaRandom = datetime(anio_aleatorio, mes_aleatorio, dia_aleatorio)
            respuestasV.append(RespuestaDelCliente(fechaRandom, respuesta))
    return respuestasV
