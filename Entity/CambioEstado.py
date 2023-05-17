import datetime

class CambioEstado:

    def __init__(self,estado):
        self._fechaInicio = datetime.datetime.now()
        self._estado = estado

    def esDelPeriodo(self,fechaInicio,fechaFin):
        if fechaInicio < self._fechaInicio < fechaFin:
            return True
        else:
            return False

    def esActivo(self):
        return "" #todo No se como implementarlo

