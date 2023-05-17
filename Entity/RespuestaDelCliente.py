import datetime

class RespuestaDelCliente:

    def __init__(self, fechaEncuesta, respuestaPosible):
        self._fechaEncuesta = fechaEncuesta
        self._respuestaPosible = respuestaPosible

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
