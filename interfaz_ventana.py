from coleccionPendientes import ColeccionPendientes
from coleccionEnProceso import ColeccionEnProceso
from coleccionTerminado import ColeccionTerminados

from textual.app import ComposeResult, App
from textual.screen import Screen
from textual.containers import Container, Grid
from textual.widgets import Label, Static, Footer, Input, Button
from textual.binding import Binding

global current_title
global current_description

class ObtenerDetalles:

    def __init__ (self, title, description):
        self.title = title
        self.description = description
        global current_title
        global current_description
        current_title = str(self.title)
        current_description = str(self.description)

    def mostrar_detalles(self):
        return self.title, self.description

class InsertarScreen(Screen):
    CSS_PATH = "insertar.tcss"

    def compose(self) -> ComposeResult:
        self.titulo_input = Input(placeholder="Título", id="titulo_input", value="")
        self.contenido_input = Input(placeholder="Contenido", id="contenido_input", value="")
        self.confirmacion_button = Button("Crear", variant="error", id="confirmacion")
        self.cancelar_button = Button("Cancelar", variant="primary", id="cancelar")

        yield self.titulo_input
        yield self.contenido_input
        yield self.confirmacion_button
        yield self.cancelar_button

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cancelar":
            self.app.pop_screen()
        elif event.button.id == "confirmacion":
            self.app.push_screen(QuitScreen(self.titulo_input.value, self.contenido_input.value))
                

class QuitScreen(Screen):
    def __init__(self, titulo_input_value, contenido_input_value):
        super().__init__()
        self.titulo_input_value = titulo_input_value
        self.contenido_input_value = contenido_input_value

    def compose(self) -> ComposeResult:
        return [
            Grid(
                Label("¿Estás seguro de que quieres actualizar la nota?", id="question"),
                Button("Confirmar", variant="error", id="confirmar"),
                Button("Cancelar", variant="primary", id="cancel"),
                id="dialog",
            )
        ]

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "confirmar":
            cp = ColeccionPendientes()
            cp.insertar(self.titulo_input_value, self.contenido_input_value)
            self.app.pop_screen()
        elif event.button.id == "cancel":
            self.app.pop_screen()


class PendientesScreen(Screen):

    CSS_PATH = "ventanaPendientes.tcss"

    BINDINGS = [
        Binding(key="q", action="volver", description="Volver", key_display="Q"),
        Binding(key="e", action="actualizar", description="Actualizar", key_display="R"),
        Binding(key="d", action="borrar", description="Borrar", key_display="D"),
        Binding(key="h", action="insertar", description="Insertar", key_display="H")
    ]

    def action_insertar(self):

        self.app.push_screen(InsertarScreen())
        

    def compose(self) -> ComposeResult:
        global current_title
        global current_description

        with Container(id="main_container"):
            yield Label(current_title, id="titulo")
            with Container(id="contenedor-descripcion"):
                yield Static(current_description, id="descripcion")
        yield Footer()

    def action_volver(self):
        self.app.pop_screen()

    def action_actualizar(self):
        pass

    def action_borrar(self):
        pass


class En_ProcesoScreen(Screen):

    CSS_PATH = "ventanaEnProceso.tcss"

    BINDINGS = [
        Binding(key="q", action="volver", description="Volver", key_display="Q"),
        Binding(key="e", action="actualizar", description="Actualizar", key_display="R"),
        Binding(key="d", action="borrar", description="Borrar", key_display="D"),
        Binding(key="h", action="insertar", description="Insertar", key_display="H")
    ]

    def action_insertar(self):
        pass

    def compose(self) -> ComposeResult:
        global current_title
        global current_description
        with Container(id="main_container"):
            yield Label(current_title, id="titulo")
            with Container(id="contenedor-EnProceso"):
                yield Static(current_description, id="EnProceso")
        yield Footer()

    def action_volver(self):
        pass

    def action_actualizar(self):
        pass

    def action_borrar(self):
        pass

class TerminadosScreen(Screen):

    CSS_PATH = "ventanaTerminados.tcss"

    BINDINGS = [
        Binding(key="q", action="volver", description="Volver", key_display="Q"),
        Binding(key="e", action="actualizar", description="Actualizar", key_display="R"),
        Binding(key="d", action="borrar", description="Borrar", key_display="D"),
        Binding(key="h", action="insertar", description="Insertar", key_display="H")
    ]

    def action_insertar(self):
        pass

    def compose(self) -> ComposeResult:
        global current_title
        global current_description
        with Container(id="main_container"):
            yield Label(current_title, id="titulo")
            with Container(id="contenedor-Terminado"):
                yield Static(current_description, id="Terminado")
        yield Footer()

    def action_volver(self):
        pass

    def action_actualizar(self):
        pass

    def action_borrar(self):
        pass