class Llamada:

    def __init__(self,descripcionOperador,detalleAccionRequerida,duracion,encuestaEnviada,observacionAuditor,respuestasDeEncuesta,cliente):
        self._descripcionOperador = descripcionOperador
        self._detalleAccionRequerida = detalleAccionRequerida
        self._duracion = duracion
        self._encuestaEnviada = encuestaEnviada
        self._observacionAuditor = observacionAuditor
        self._respuestasDeEncuesta = []
        self._cambioEstado = [] #todo Recordar Agregar el Primer Cambio de Estado
        self._accionRequerida = []
        self._cliente = cliente
        self._operador = []
        self._auditor = []
        self._subOpcionSeleccionada = []
        self._opcionSeleccionada = []

    def verificarPeriodoYExistenciaDeRespuestas(self,fechaInicio,fechaFin): #todo Cambie el nombre del Metodo
        return (self._cambioEstado[0].esDelPeriodo(fechaInicio,fechaFin) and len(self._respuestasDeEncuesta) > 0 )

    #todo |No estoy implementando el 'tomarRespuesta()' creo que lo entendimos mal, ya que no tiene que mostrar las respuestas, sino
    #todo |que simplemente validar que haya, entonces haria falta un metodo para eso?? Creo que simplemente con verificar que
    #todo |nuestro array sea mayor a 0 sirve, tal vez haya que corregir el Diagrama de Secuencia.

    def mostrarDatos(self):
        nombreCliente = self._cliente.mostrarNombre()
        for cambioEstado in self._cambioEstado:
            if(cambioEstado.esActivo()): #todo Arreglar el tema de que cambioEstado no sabe cual es el Activo
                #todo En el Diagrama de Secuencia cambiar el nombre de 'obtenerEstadoActivo()' a 'esActivo()'
                estado = cambioEstado.getNombre()
