import datetime
from Entity import Pregunta


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

        def getfechaFinVigencia(self):
            return self._fechaFinVigencia

nomEncuestas = ['Encuesta de satisfaccion', 'Encuesta de calidad', 'Encuesta de servicio',
    'Encuesta de producto', 'Encuesta de atencion al cliente', 'Encuesta de atencion al publico']

def generarEncuestaAleatoria(n = 1):

    encuestas = [Encuesta("Soy la Encuesta 1", datetime.date(2023, 0o5, 0o6),Pregunta.generarPreguntasAleatorias(3))]
    encuestas.append(Encuesta("Soy la Encuesta 2",datetime.date(2023, 0o7, 0o3),Pregunta.generarPreguntasAleatorias(2)))
    return encuestas
