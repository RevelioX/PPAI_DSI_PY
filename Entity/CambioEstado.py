import datetime
import random
from Entity import Estado
from datetime import datetime

class CambioEstado:

    def __init__(self,fechaInicio, estado):
        self._fechaInicio = fechaInicio
        self._estado = estado

    def esDelPeriodo(self,fechaInicio,fechaFin):
        fechaInicio = datetime.strptime(fechaInicio, "%Y-%m-%d")
        fechaFin = datetime.strptime(fechaFin, "%Y-%m-%d")
        if fechaInicio < self._fechaInicio < fechaFin:
            return True
        else:
            return False

    def esActivo(self):
        return self._estado.getNombreEstado()

    def getNombre(self):
        return self._estado.getNombre()

def obtenerFechaRandom():
    cambioV = []
    anio_aleatorio = random.randint(2015, 2023)
    mes_aleatorio = random.randint(1, 12)
    dia_aleatorio = random.randint(1, 29)
    estado = Estado.obtenerEstado()
    fechaRandom = datetime(anio_aleatorio, mes_aleatorio, dia_aleatorio)
    cambioV.append(CambioEstado(fechaRandom, estado))

    return cambioV
