import datetime

class Encuesta:
        def __init__(self,descripcion,fechaFinVigencia,pregunta):
            self._descripcion = descripcion
            self._fechaFinVigencia = fechaFinVigencia
            self._pregunta = pregunta

        def esVigente(self):
            fechaActual = datetime.datetime.now()
            if (fechaActual < self._fechaFinVigencia):
                return True
            else:
                return False

        def getDescripcionEncuesta(self):
            return self._descripcion

        def getPreguntas(self):
            return self._pregunta
