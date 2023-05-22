import PySimpleGUI as sg


class PantallaConsultarEncuesta:
    def __init__(self, controladorConsultas=None, botonConsultarEn=sg.Button('Consultar Encuesta'),
                 botonConsultar=sg.Button('Consultar'), botonCerrar=sg.Button('Cerrar'),
                 textoPeriodo=sg.Text('Selecciona un periodo de fechas'),
                 botonDesde=sg.CalendarButton('Desde', target='date_from', key='cal_from'),
                 botonHasta=sg.CalendarButton('Hasta', target='date_to', key='cal_to')):
        self.controlador = controladorConsultas
        self._botonConsultarEncuesta = botonConsultarEn
        self._botonConsultar = botonConsultar,
        self._botonCerrar = botonCerrar,
        self._textPeriodo = textoPeriodo,
        self._botonDesde = botonDesde,
        self._botonHasta = botonHasta

    def opcionConsultarEncuesta(self, controladorConsultas):
        self.controlador = controladorConsultas
        self.habilitar()

    def habilitar(self):
        layout_consulta = [[sg.Button('Consultar Encuesta', size=(18, 1), pad=((70, 3), 20))]]
        window_consulta = sg.Window('Consultar Encuesta''', layout_consulta, size=(300, 100))

        while True:
            event_consulta, values_consulta = window_consulta.read()
            if event_consulta == sg.WINDOW_CLOSED:
                break
            elif event_consulta == "Consultar Encuesta":
                window_consulta.close()
                self.controlador.newEncuesta()

    def seleccionarPeriodo(self):
        layout_periodo = [[self._textPeriodo],
                          [self._botonDesde,
                           sg.Input(key='date_from', enable_events=True, visible=False)],
                          [self._botonHasta,
                           sg.Input(key='date_to', enable_events=True, visible=False)],
                          [self._botonConsultar, self._botonCerrar]]

        window_periodo = sg.Window('Seleccionar Periodo''', layout_periodo)
        while True:
            event_periodo, values_periodo = window_periodo.read()
            if event_periodo == sg.WINDOW_CLOSED or event_periodo == "Cerrar":
                window_periodo.close()
                break
            elif event_periodo == 'cal_from':
                window_periodo['date_from'].update(values_periodo['cal_from'].strftime('%Y-%m-%d'), visible=True)
            elif event_periodo == 'cal_to':
                window_periodo['date_to'].update(values_periodo['cal_to'].strftime('%Y-%m-%d'), visible=True)
            elif event_periodo == 'Consultar':
                date_from = (values_periodo['date_from'].split(" ")[0])
                date_to = (values_periodo['date_to'].split(" ")[0])
                self.controlador.tomarPeriodo(date_from, date_to)

    def mostrarLlamadas(self, llamadasFiltradas):
        if len(llamadasFiltradas) > 0:
            layout_llamada = [
                [sg.Table(
                    values=[["Llamada de " + llamada.getNombreCliente().getNombre()] for llamada in llamadasFiltradas],
                    headings=['Cliente'],
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='-TABLE-',
                    enable_events=True,
                    select_mode=sg.TABLE_SELECT_MODE_BROWSE)],

                [sg.Button('Cerrar')]
            ]
            window_llamadas = sg.Window('Lista Llamada''', layout_llamada)
            while True:
                event, values = window_llamadas.read()
                if event == sg.WINDOW_CLOSED or event == 'Cerrar':
                    window_llamadas.close()
                    break
                elif event == '-TABLE-':
                    row_index = values['-TABLE-'][0]
                    llamada_seleccionada = llamadasFiltradas[row_index]
                    mensaje = (f"Llamada seleccionado de: {llamada_seleccionada.getNombreCliente().getNombre()}")
                    sg.popup(mensaje, title='Selección exitosa')
                    self.tomarSeleccion(llamada_seleccionada)
        else:
            layout = [[sg.Text('¡No se encontraron llamadas para esas fechas!', size=(40, 1), justification='center')],
            [sg.Button('Cerrar')]]
            window_error = sg.Window('ERROR!', layout,size=(300, 100))

            while True:
                event, _ = window_error.read()
                if event == sg.WINDOW_CLOSED or event == 'Cerrar':
                    break
            window_error.close()

    def tomarSeleccion(self, llamada):
        self.controlador.llamadaSeleccion(llamada)

    def mostrarLlamadaConEncuesta(self, datos):
        respuesta = datos[3][0][0]
        pregunta = datos [3][0][1]
        encuesta = datos[3][0][2]
        layout_llamada = [
            [sg.Table(
                values=[[datos[0], datos[1], datos[2], respuesta, pregunta, encuesta]],
                headings=['Cliente', 'Estado', 'Duracion', "Respuesta", "Pregunta", "Encuesta"],
                auto_size_columns=True,
                display_row_numbers=True,
                justification='left',
                num_rows=10,
                key='-TABLE-',
                enable_events=True,
                select_mode=sg.TABLE_SELECT_MODE_BROWSE)],

            [sg.Button('Cerrar')],
        ]
        window_llamadas_seleccionada = sg.Window('Llamada Seleccionada''', layout_llamada)
        while True:
            event, values = window_llamadas_seleccionada.read()
            if event == sg.WINDOW_CLOSED or event == 'Cerrar':
                window_llamadas_seleccionada.close()
                break
            elif event == '-TABLE-':
                row_index = values['-TABLE-'][0]
                sg.popup("¿Desea Generar un CSV?")
                self.opcionGenerarCSV(datos)

    def opcionGenerarCSV(self, datos):
         self.controlador.generarCSVSeleccionado(datos)
