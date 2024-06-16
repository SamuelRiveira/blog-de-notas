# interfaz_ventana.py

from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Grid
from textual.widgets import Label, Static

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

    def compose(self) -> ComposeResult:
        global current_title
        global current_description
        yield Grid(
            Label(current_title, id="titulo"),  # Mostrar título arriba
            Static(current_description, id="descripcion"),  # Mostrar descripción centrada y más grande
            id="dialog",
        )

class En_ProcesoScreen(Screen):

    def compose(self) -> ComposeResult:
        global current_title
        global current_description
        yield Grid(
            Label(current_title, id="titulo"),  # Mostrar título arriba
            Static(current_description, id="descripcion"),  # Mostrar descripción centrada y más grande
            id="dialog",
        )

class TerminadosScreen(Screen):

    def compose(self) -> ComposeResult:
        global current_title
        global current_description
        yield Grid(
            Label(current_title, id="titulo"),  # Mostrar título arriba
            Static(current_description, id="descripcion"),  # Mostrar descripción centrada y más grande
            id="dialog",
        )
