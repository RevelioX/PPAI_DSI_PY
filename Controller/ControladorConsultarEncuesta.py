class ControladorConsultarEncuesta:

    def __init__(self):
        self._llamadas = []

    def filtrarLlamada(self,fechaInicio,fechaFin):
        llamadasFiltradas = []
        for llamada in self._llamadas:
            if (llamada.verificarPeriodo(fechaInicio,fechaFin)):
                llamadasFiltradas.append(llamada)
        return llamadasFiltradas

    def llamadaSeleccionada(self,llamada):
        return llamada.mostrarDatos()
