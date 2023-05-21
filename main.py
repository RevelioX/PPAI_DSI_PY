from Boundary import pantallaMain
from Controller import ControladorConsultarEncuesta
from Entity import Llamada, CambioEstado


def main():
    llamadas = Llamada.generarLlamada()
    CambioEstado.obtenerFechaRandom()
    pantalla = pantallaMain.PantallaConsultarEncuesta()
    gestor = ControladorConsultarEncuesta.ControladorConsultarEncuesta(2, 3, llamadas,pantalla)

    pantalla.opcionConsultarEncuesta(gestor)

if __name__ == "__main__":
    main()
