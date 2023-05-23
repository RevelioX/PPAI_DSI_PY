from Entity import RespuestaPosible
from Entity import Encuesta

class Pregunta:

    def __init__(self,pregunta='',respuestasPosible = None):

        self._pregunta = pregunta
        self._respuestasPosibles = []

    def getDescripcion(self):
        return self._pregunta

    def listarRespuestasPosibles(self):
        respuestas = []
        for respuestaPosible in self._respuestasPosibles:
            respuestas.append(respuestaPosible.getDescripcion())
        return respuestas

    def buscarEncuesta(self):
        encuestas = Encuesta.generarEncuestaAleatoria()

        for i in encuestas:
            for j in i.getPreguntas():
                if self._pregunta == j._pregunta:
                    return i

    def mostrarEncuesta(self):
        encuesta = self.buscarEncuesta()
        return encuesta.getDescripcionEncuesta()

preguntasRandom = ["Hola?","Telefono?","Bicicleta?"]

def generarPreguntasAleatorias(cantidadPreguntas):
    preguntas = []
    for i in range(1, cantidadPreguntas + 1):
        pregunta = Pregunta()
        pregunta._pregunta = preguntasRandom[i-1]
        pregunta._respuestasPosibles.append(RespuestaPosible.obtenerRespuestaCliente(1))
        pregunta._respuestasPosibles.append(RespuestaPosible.obtenerRespuestaCliente(2))
        preguntas.append(pregunta)
    return preguntas
