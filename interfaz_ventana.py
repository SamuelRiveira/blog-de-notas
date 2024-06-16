from coleccionPendientes import ColeccionPendientes
from coleccionEnProceso import ColeccionEnProceso
from coleccionTerminado import ColeccionTerminados

from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Container
from textual.widgets import Label, Static, Footer
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


class PendientesScreen(Screen):

    CSS_PATH = "ventanaPendientes.tcss"

    BINDINGS = [
        Binding(key="Q", action="action_volver", description="Volver"),
        Binding(key="R", action="action_actualizar", description="Actualizar"),
        Binding(key="D", action="action_borrar", description="Borrar")
    ]

    def compose(self) -> ComposeResult:
        global current_title
        global current_description

        with Container(id="main_container"):
            yield Label(current_title, id="titulo")
            with Container(id="contenedor-descripcion"):
                yield Static(current_description, id="descripcion")
        yield Footer()

    def action_volver(self):
        pass

    def action_actualizar(self):
        pass

    def action_borrar(self):
        pass


class En_ProcesoScreen(Screen):

    CSS_PATH = "ventanaEnProceso.tcss"

    BINDINGS = [
        Binding(key="Q", action="action_volver", description="Volver"),
        Binding(key="R", action="action_actualizar", description="Actualizar"),
        Binding(key="D", action="action_borrar", description="Borrar")
    ]

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
        Binding(key="Q", action="action_volver", description="Volver"),
        Binding(key="R", action="action_actualizar", description="Actualizar"),
        Binding(key="D", action="action_borrar", description="Borrar")
    ]

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