class Pregunta:

    def __init__(self,pregunta,respuestasPosible):

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
