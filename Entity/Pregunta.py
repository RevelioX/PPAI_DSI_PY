class Pregunta:

    def __init__(self,pregunta,respuestasPosible):

        self._pregunta = pregunta
        self._respuestasPosibles = respuestasPosibles


    def listarRespuestasPosibles(self):
        respuestas = []
        for respuestaPosible in self._respuestasPosibles:
            respuestas.append( (respuestaPosible.getDescripcion(),respuestaPosible.getValor()) )
        return respuestas




