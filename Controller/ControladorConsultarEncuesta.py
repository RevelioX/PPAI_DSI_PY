from datetime import datetime, time
import csv
import sys

class ControladorConsultarEncuesta:

    def __init__(self, fechaInicioPeriodo, fechaFinPeriodo, llamadas, pantallaConsultarEncuesta = None):
        self._pantallaConsultarEncuesta = pantallaConsultarEncuesta
        self._fechaInicioPeriodo = fechaInicioPeriodo
        self._fechaFinPeriodo = fechaFinPeriodo
        #self._fechaInicio = datetime.combine(datetime.strptime(str(fechaInicioPeriodo), "%Y-%m-%d").date(), time.min)
        #self._fechaFin = datetime.combine(datetime.strptime(str(fechaFinPeriodo), "%Y-%m-%d").date(), time.max)
        self._llamadas = llamadas

    def newEncuesta(self):
        self._pantallaConsultarEncuesta.seleccionarPeriodo()

    def tomarPeriodo(self, fechaInicioPeriodo, fechaFinPeriodo):
        self._fechaInicioPeriodo = fechaInicioPeriodo
        self._fechaFinPeriodo = fechaFinPeriodo
        self.filtrarLlamada(fechaInicioPeriodo, fechaFinPeriodo)

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


    def llamadaSeleccion(self,llamada):
        self._pantallaConsultarEncuesta.mostrarLlamadaConEncuesta(llamada.mostrarDatos())

    def generarCSV(self, datos):
        nombre_archivo_csv = "DatosCliente.csv"

        with open(nombre_archivo_csv, "w", newline="") as file:
            escritor_csv = csv.writer(file)
            escritor_csv.writerow(["Nombre", "Estado", "Duracion", "Respuesta", "Pregunta", "Encuesta"])
            escritor_csv.writerow([datos[0], datos[1], str(datos[2]), datos[3][0][0], datos[3][0][1], datos[3][0][2]])
        self.FinCU()

    def FinCU(self):
        sys.exit()
