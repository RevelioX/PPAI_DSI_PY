import random

from Entity import Cliente


class Llamada:

    def __init__(self, descripcionOperador, detalleAccionRequerida, duracion, encuestaEnviada, observacionAuditor,
                 cliente):
        self._descripcionOperador = descripcionOperador
        self._detalleAccionRequerida = detalleAccionRequerida
        self._duracion = duracion
        self._encuestaEnviada = encuestaEnviada
        self._observacionAuditor = observacionAuditor
        self._respuestasDeEncuesta = []
        self._cambioEstado = []  # todo Recordar Agregar el Primer Cambio de Estado
        self._accionRequerida = []
        self._cliente = cliente
        self._operador = []
        self._auditor = []
        self._subOpcionSeleccionada = []
        self._opcionSeleccionada = []

    def verificarPeriodoYExistenciaDeRespuestas(self, fechaInicio, fechaFin):  # todo Cambie el nombre del Metodo
        return (self._cambioEstado[0].esDelPeriodo(fechaInicio, fechaFin) and len(self._respuestasDeEncuesta) > 0)

    # todo |No estoy implementando el 'tomarRespuesta()' creo que lo entendimos mal, ya que no tiene que mostrar las respuestas, sino
    # todo |que simplemente validar que haya, entonces haria falta un metodo para eso?? Creo que simplemente con verificar que
    # todo |nuestro array sea mayor a 0 sirve, tal vez haya que corregir el Diagrama de Secuencia.

    def mostrarDatos(self):
        nombreCliente = self._cliente.mostrarNombre()
        for cambioEstado in self._cambioEstado:
            if (cambioEstado.esActivo()):  # todo Arreglar el tema de que cambioEstado no sabe cual es el Activo
                # todo En el Diagrama de Secuencia cambiar el nombre de 'obtenerEstadoActivo()' a 'esActivo()'
                estado = cambioEstado.getNombre()

    def getDuracion(self):
        return self._duracion


def generarLlamada():
    desc = ['Ofrecimiento de reembolso o crédito para compensar cualquier cargo adicional.',
            'Asistencia técnica para resolver problemas de velocidad de conexión.',
            'Aclaración de las políticas de cancelación', 'Aclaración de las políticas de de cambio de servicio.',
            'Actualización de servicios.']

    observaciones_auditor = ["El operario fue amable y cortés durante toda la llamada.",
                             "Mostró un buen conocimiento del producto y pudo resolver las dudas del cliente.",
                             "Sin embargo, se tomó demasiado tiempo para buscar la información necesaria.",
                             "El operario mostró impaciencia cuando el cliente planteó preguntas adicionales.",
                             "Sería recomendable que el operario mejore su habilidad para manejar situaciones de conflicto."]

    accionreq = ['Comunicar saldo.', 'Dar de baja tarjeta.', 'Denunciar un robo.']
    llamada_totales = []
    for i in range(10):
        descripcionOperador = random.choice(desc)
        detalleAccionRequerida = random.choice(accionreq)
        duracion = random.randint(1, 20)
        encuestaEnviada = bool(random.getrandbits(1))
        observacionAuditor = random.choice(observaciones_auditor)
        cliente = Cliente.crearCliente()[0]
        cliente.getNombre()
        individual = Llamada(descripcionOperador, detalleAccionRequerida, duracion, encuestaEnviada, observacionAuditor,
                             cliente)
        llamada_totales.append(individual)
    return llamada_totales
