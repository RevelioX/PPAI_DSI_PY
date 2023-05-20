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

    def filtrarLlamada(self, fechaInicioPeriodo, fechaFinPeriodo): #buscarLlamada
        llamadasFiltradas = []
        for llamada in self._llamadas:
            if (llamada.verificarPeriodo(fechaInicioPeriodo, fechaFinPeriodo)):
                llamadasFiltradas.append(llamada)
        return llamadasFiltradas

    def llamadaSeleccionada(self, llamada):
        return llamada.mostrarDatos()

    def verPeriodo(self):
        return self._fechaInicioPeriodo
