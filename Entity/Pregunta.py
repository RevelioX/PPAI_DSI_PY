from Entity import RespuestaPosible
class Pregunta:

    def __init__(self,pregunta='',respuestasPosible = None):

        self._pregunta = pregunta
        self._respuestasPosibles = respuestasPosible

    def getDescripcion(self):
        return self._pregunta

    def listarRespuestasPosibles(self):
        respuestas = []
        for respuestaPosible in self._respuestasPosibles:
            respuestas.append( (respuestaPosible.getDescripcion(),respuestaPosible.getValor()) )
        return respuestas

    def buscarEncuesta(self):
        pass

    def mostrarEncuesta(self):
        encuesta = self.buscarEncuesta()
        return encuesta.getDescripcionEncuesta()

preguntasRandom = {
    1: ['¿Le gustó la atención?', ['Sí', 'No']],
    2: ['¿Del 1 al 10 en cuánto nos calificaría?', []],
    3: ['¿Nos recomendaría a otras personas?', []]
}

def generarPreguntasAleatorias(cantidadPreguntas):
    preguntas = []
    for i in range(1, cantidadPreguntas + 1):
        pregunta = Pregunta()
        pregunta._pregunta = preguntasRandom[i][0]
        pregunta._respuestasPosibles = preguntasRandom[i][1]
        preguntas.append(pregunta)

    print('Preguntas generadas con éxito')

    return preguntas
