# interfaz.py

# Importaciones necesarias
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from listaTerminado import ListaTerminados
from listaPendiente import ListaPendientes
from listaEnProceso import ListaEnProceso

from textual.app import App, ComposeResult
from textual.widgets import Footer, Label, ListItem, ListView, Header
from textual.binding import Binding
from textual.screen import Screen
from textual.message import Message
from textual.containers import Container
from interfaz_ventana import PendientesScreen, En_ProcesoScreen, TerminadosScreen, ObtenerDetalles

class ListItemSelected(Message):
    def __init__(self, list_view: ListView, item: ListItem, index: int):
        super().__init__()
        self.list_view = list_view
        self.item = item
        self.index = index

class ExampleScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(Header).update("Nueva Pantalla")
        self.query_one(Footer).update("Presiona Q para salir.")

class TableApp(App):

    CSS_PATH = "interfaz.tcss"

    BINDINGS = [
        Binding(key="Q", action="quit", description="Salir")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        
        with Container(id="main_container"):

            with Container(id="left_container"):
                yield Label("Lista Pendientes")
                yield ListView(id="list_pendientes")
            
            with Container(id="center_container"):
                yield Label("Lista En Proceso")
                yield ListView(id="list_enProceso")

            with Container(id="right_container"):
                yield Label("Lista Terminados")
                yield ListView(id="list_terminados")
        
        yield Footer()

    def on_mount(self) -> None:
        self.cargar_pendientes()
        self.cargar_enProceso()
        self.cargar_terminados()

    def cargar_pendientes(self) -> None:
        pendientes = ListaPendientes().obtener_pendientes()
        list_pendientes = self.query_one("#list_pendientes", ListView)

        for id, titulo, descripcion in pendientes:
            list_pendientes.append(ListItem(Label(titulo)))  # Mostrar título en la lista

    def cargar_enProceso(self) -> None:
        enProceso = ListaEnProceso().obtener_en_proceso()
        list_enProceso = self.query_one("#list_enProceso", ListView)

        for id, titulo, descripcion in enProceso:
            list_enProceso.append(ListItem(Label(titulo)))  # Mostrar título en la lista

    def cargar_terminados(self) -> None:
        terminados = ListaTerminados().obtener_terminados()
        list_terminados = self.query_one("#list_terminados", ListView)

        for id, titulo, descripcion in terminados:
            list_terminados.append(ListItem(Label(titulo)))  # Mostrar título en la lista

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        list_view = event.control
        item = event.item
        index = -1

        for i, child in enumerate(list_view.children):
            if child == item:
                index = i
                break

        # Obtener el título y la descripción del item seleccionado
        titulo = item.query_one(Label).renderable
        descripcion = ""

        # Buscar el título y la descripción correspondientes en la base de datos
        if list_view.id == "list_pendientes":
            pendientes = ListaPendientes().obtener_pendientes()
            titulo, descripcion = pendientes[index][1], pendientes[index][2]  # Obtener título y descripción usando el índice
            ObtenerDetalles(titulo, descripcion)
            self.push_screen(PendientesScreen())
        elif list_view.id == "list_enProceso":
            enProceso = ListaEnProceso().obtener_en_proceso()
            titulo, descripcion = enProceso[index][1], enProceso[index][2]  # Obtener título y descripción usando el índice
            ObtenerDetalles(titulo, descripcion)
            self.push_screen(En_ProcesoScreen())
        elif list_view.id == "list_terminados":
            terminados = ListaTerminados().obtener_terminados()
            titulo, descripcion = terminados[index][1], terminados[index][2]  # Obtener título y descripción usando el índice
            ObtenerDetalles(titulo, descripcion)
            self.push_screen(TerminadosScreen())

if __name__ == "__main__":
    app = TableApp()
    app.run()