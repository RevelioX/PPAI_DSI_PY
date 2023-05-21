import random

from Entity import Cliente, CambioEstado, RespuestaDelCliente


class Llamada:

    def __init__(self, descripcionOperador, detalleAccionRequerida, duracion, encuestaEnviada, observacionAuditor,respuestasDeEncuesta,
                 cliente, cambioEstado):
        self._descripcionOperador = descripcionOperador
        self._detalleAccionRequerida = detalleAccionRequerida
        self._duracion = duracion
        self._encuestaEnviada = encuestaEnviada
        self._observacionAuditor = observacionAuditor
        self._respuestasDeEncuesta = respuestasDeEncuesta
        self._cambioEstado = cambioEstado  # todo Recordar Agregar el Primer Cambio de Estado
        self._accionRequerida = []
        self._cliente = cliente
        self._operador = []
        self._auditor = []
        self._subOpcionSeleccionada = []
        self._opcionSeleccionada = []

    def verificarPeriodo(self, fechaInicio, fechaFin):  # todo
        return self._cambioEstado[0].esDelPeriodo(fechaInicio, fechaFin)

    def verificarExistenciaDeRespuestas(self):
        return len(self._respuestasDeEncuesta) > 0

    def mostrarDatos(self):
        nombre = self.getNombreCliente().getNombre()
        estado = self._cambioEstado[0].esActivo()
        duracion = self.getDuracion()
        datosRTA = []
        for i in self._respuestasDeEncuesta:
            rta = i.mostrarDatosRTA()
            pgunta = i.mostrarPregunta()
            encuesta = i.mostrarEncuesta()
            datosRTA.append((rta,pgunta,encuesta))
        return(nombre, estado, duracion, datosRTA)


    def getNombreCliente(self):
        return self._cliente

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
    for i in range(20):
        descripcionOperador = random.choice(desc)
        detalleAccionRequerida = random.choice(accionreq)
        duracion = random.randint(1, 20)
        encuestaEnviada = bool(random.getrandbits(1))
        observacionAuditor = random.choice(observaciones_auditor)
        cliente = random.choice(Cliente.crearCliente())
        cliente.getNombre()
        cambio = CambioEstado.obtenerFechaRandom()
        respuesta = RespuestaDelCliente.respuesEncuesta()
        individual = Llamada(descripcionOperador, detalleAccionRequerida, duracion, encuestaEnviada, observacionAuditor,respuesta,
                             cliente, cambio)
        llamada_totales.append(individual)
    return llamada_totales
