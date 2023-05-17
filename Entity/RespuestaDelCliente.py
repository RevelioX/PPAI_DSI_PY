import datetime

class RespuestaDelCliente:

    def __init__(self, fechaEncuesta, respuestaPosible):
        self._fechaEncuesta = fechaEncuesta
        self._respuestaPosible = respuestaPosible

    def getDescripcionRta(self):
        return self._respuestaPosible.getDescripcion()

    def get_fechaEncuesta(self):
        return self._fechaEncuesta

    def set_fechaEncuesta(self, fechaEncuesta):
        self._fechaEncuesta = fechaEncuesta

    def get_respuestaPosible(self):
        return self._respuestaPosible

    def set_respuestaPosible(self, respuestaPosible):
        self._respuestaPosible = respuestaPosible
