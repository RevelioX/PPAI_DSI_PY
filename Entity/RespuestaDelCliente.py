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


def respuesEncuesta():
    nroRandom = random.randint(0, 1)
    respuestasV = []
    if nroRandom != 0:
        for i in range(20):
            anio_aleatorio = random.randint(2000, 2023)
            mes_aleatorio = random.randint(1, 12)
            dia_aleatorio = random.randint(1, 29)
            respuesta = RespuestaPosible.obtenerRespuesta()
            fechaRandom = datetime(anio_aleatorio, mes_aleatorio, dia_aleatorio)
            respuestasV.append(RespuestaDelCliente(fechaRandom, respuesta))
    return respuestasV
