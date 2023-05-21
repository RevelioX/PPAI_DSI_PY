from Boundary import pantallaMain
from Controller import ControladorConsultarEncuesta
from Entity import Llamada, CambioEstado, Pregunta


def main():
    llamadas = Llamada.generarLlamada()
    CambioEstado.obtenerFechaRandom()
    pantalla = pantallaMain.PantallaConsultarEncuesta()
    gestor = ControladorConsultarEncuesta.ControladorConsultarEncuesta(2, 3, llamadas,pantalla)
    pantalla.opcionConsultarEncuesta(gestor)
    #print((Pregunta.generarPreguntasAleatorias(3)[0]).getDescripcion())


if __name__ == "__main__":
    main()
