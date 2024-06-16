# interfaz_ventana.py

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Grid
from textual.widgets import Button

global current_description

class ObtenerDescripcion():

    def __init__ (self, descripcion):
        self.descripcion = descripcion
        global current_description
        current_description = str(self.descripcion)

    def mostrar_descripcion(self):
        return self.descripcion


class PendientesScreen(Screen):

    def compose(self) -> ComposeResult:
        global current_description
        yield Grid(
            Button(current_description, variant="error", id="quit"),  # Mostrar descripción en el botón
            Button("Pendientes", variant="primary", id="cancel"),
            id="dialog",
        )

class En_ProcesoScreen(Screen):

    def compose(self) -> ComposeResult:
        global current_description
        yield Grid(
            Button(current_description, variant="error", id="quit"),  # Mostrar descripción en el botón
            Button("En proceso", variant="primary", id="cancel"),
            id="dialog",
        )

class TerminadosScreen(Screen):

    def compose(self) -> ComposeResult:
        global current_description
        yield Grid(
            Button(current_description, variant="error", id="quit"),  # Mostrar descripción en el botón
            Button("Terminados", variant="primary", id="cancel"),
            id="dialog",
        )