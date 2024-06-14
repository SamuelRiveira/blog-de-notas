# import os
# class ObtenerID:

#     def escribir(self, id):
#         f = open("mostrarlaid.txt", 'wt')
#         with f:
#             f.write(id)
#             return True
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Grid
from textual.widgets import Button, Static

global index

class ObtenerID():

    def __init__ (self, id):
        self.id = id
        global index
        index = str(self.id)

    def mostrarid(self):
        return self.id


class PendientesScreen(Screen):

    def compose(self) -> ComposeResult:
        global index
        yield Grid(
            Button(index , variant="error", id="quit"),
            Button("Pendientes", variant="primary", id="cancel"),
            id="dialog",
        )

class En_ProcesoScreen(Screen):

    def compose(self) -> ComposeResult:
        global index
        yield Grid(
            Button(index , variant="error", id="quit"),
            Button("En proceso", variant="primary", id="cancel"),
            id="dialog",
        )

class TerminadosScreen(Screen):

    def compose(self) -> ComposeResult:
        global index
        yield Grid(
            Button(index , variant="error", id="quit"),
            Button("Terminados", variant="primary", id="cancel"),
            id="dialog",
        )