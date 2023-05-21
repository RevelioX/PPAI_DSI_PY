class ControladorConsultarEncuesta:

    def __init__(self, fechaInicioPeriodo, fechaFinPeriodo, llamadas, pantallaConsultarEncuesta = None):
        self._pantallaConsultarEncuesta = pantallaConsultarEncuesta
        self._fechaInicioPeriodo = fechaInicioPeriodo
        self._fechaFinPeriodo = fechaFinPeriodo
        self._llamadas = llamadas

    def newEncuesta(self):
        self._pantallaConsultarEncuesta.seleccionarPeriodo()

    def tomarPeriodo(self, fechaInicioPeriodo, fechaFinPeriodo):
        self._fechaInicioPeriodo = fechaInicioPeriodo
        self._fechaFinPeriodo = fechaFinPeriodo
        #self.filtrarLlamada(fechaInicioPeriodo, fechaFinPeriodo)

        #No entiendo el porque de este metodo, no lo tenemos en el Diagrama de secuencia??? Y para que necesitamor recordar
        #el periodo en el controlador

    def filtrarLlamada(self, fechaInicioPeriodo, fechaFinPeriodo): #buscarLlamada
        llamadasFiltradas = []
        for llamada in self._llamadas:
            if (llamada.verificarPeriodo(fechaInicioPeriodo, fechaFinPeriodo) and llamada.verificarExistenciaDeRespuestas()):
                llamadasFiltradas.append(llamada)
        #-Anulo el retorno para ser consistente con el diagrama de Secuencia    return llamadasFiltradas
        #-Asi que voy a llamar a la función en la Interfaz
        self._pantallaConsultarEncuesta.mostrarLlamadas(llamadasFiltradas)

    def llamadaSeleccionada(self, llamada):
        return llamada.mostrarDatos()
