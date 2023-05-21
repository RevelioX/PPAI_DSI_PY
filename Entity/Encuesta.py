import datetime
import random

from Entity import Pregunta


class Encuesta:
        def __init__(self,pregunta=None, fechaFinVigencia='',descripcion=''):
            self._descripcion = descripcion
            self._fechaFinVigencia = fechaFinVigencia
            self._pregunta = pregunta

        def esVigente(self):
            fechaActual = datetime.datetime.now()
            if (fechaActual < self._fechaFinVigencia):
                return True
            else:
                return False

       # def mostrarEncuesta(self):
       #     print(self.getDescripcionEncuesta())
       #     print(self.getPreguntas())
       #     print(self.getfechaFinVigencia())

        def getDescripcionEncuesta(self):
            return self._descripcion

        def getPreguntas(self):
            return self._pregunta

        def getfechaFinVigencia(self):
            return self._fechaFinVigencia

nomEncuestas = ['Encuesta de satisfaccion', 'Encuesta de calidad', 'Encuesta de servicio',
    'Encuesta de producto', 'Encuesta de atencion al cliente', 'Encuesta de atencion al publico']

def generarEncuestaAleatoria():
    encuestas = []
    for i in range(3):
        descripcion = nomEncuestas[i]
        current_year = datetime.datetime.now().year
        fechaFinVigenciate = datetime.date(random.randint(current_year, (current_year + 10)), random.randint(1, 12), random.randint(1, 28))
        pregunta = Pregunta.generarPreguntasAleatorias(3)
        encuestas.append(Encuesta(pregunta, fechaFinVigenciate, descripcion))
    return encuestas
