# interfaz.py

import sys
import os

# Añade el directorio actual al sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importaciones de los módulos de las listas
from listaTerminado import ListaTerminados
from listaPendiente import ListaPendientes
from listaEnProceso import ListaEnProceso

# Importaciones de Textual
from textual.app import App, ComposeResult
from textual.widgets import Footer, Label, ListItem, ListView, Header
from textual.binding import Binding
from textual.screen import Screen
from textual.message import Message
from textual.containers import Container
from interfaz_ventana import PendientesScreen, En_ProcesoScreen, TerminadosScreen, ObtenerID

# Definición del evento personalizado para la selección de un ListItem
class ListItemSelected(Message):
    def __init__(self, list_view: ListView, item: ListItem, index: int):
        super().__init__()
        self.list_view = list_view
        self.item = item
        self.index = index

# Ejemplo de una pantalla personalizada
class ExampleScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(Header).update("Nueva Pantalla")
        self.query_one(Footer).update("Presiona Q para salir.")

# Aplicación principal
class TableApp(App):

    CSS_PATH = "interfaz.tcss"

    BINDINGS = [
        Binding(key="Q", action="quit", description="Salir")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        
        # Contenedor principal para las tres listas
        with Container(id="main_container"):

            with Container(id="left_container"):
                yield Label("Lista Pendientes")
                yield ListView(id="list_pendientes")
            
            with Container(id="center_container"):
                yield Label("Lista En Proceso")
                yield ListView(id="list_enProceso")

            with Container(id="right_container"):  # Usaremos sólo terminados por ahora
                yield Label("Lista Terminados")
                yield ListView(id="list_terminados")  # Asignar un ID único al ListView
        
        yield Footer()

    def on_mount(self) -> None:
        self.cargar_pendientes()
        self.cargar_enProceso()
        self.cargar_terminados()

    def cargar_pendientes(self) -> None:
        # Obtener los datos de la lista de terminados desde la base de datos
        pendientes = ListaPendientes().obtener_pendientes()

        # Referenciar el ListView por su ID
        list_pendientes = self.query_one("#list_pendientes", ListView)

        # Rellenar el ListView con los datos obtenidos
        for id, descripcion in pendientes:
            list_pendientes.append(ListItem(Label(descripcion)))

    def cargar_enProceso(self) -> None:
        # Obtener los datos de la lista de terminados desde la base de datos
        enProceso = ListaEnProceso().obtener_en_proceso()

        # Referenciar el ListView por su ID
        list_enProceso = self.query_one("#list_enProceso", ListView)

        # Rellenar el ListView con los datos obtenidos
        for id, descripcion in enProceso:
            list_enProceso.append(ListItem(Label(descripcion)))

    def cargar_terminados(self) -> None:
        # Obtener los datos de la lista de terminados desde la base de datos
        terminados = ListaTerminados().obtener_terminados()

        # Referenciar el ListView por su ID
        list_terminados = self.query_one("#list_terminados", ListView)

        # Rellenar el ListView con los datos obtenidos
        for id, descripcion in terminados:
            list_terminados.append(ListItem(Label(descripcion)))

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        list_view = event.control
        item = event.item
        
        # Buscar el índice del ListItem en el ListView
        index = -1
        for i, child in enumerate(list_view.children):
            if child == item:
                index = i
                break

        obtener = ObtenerID(index + 1)  # Esto parece ser una acción necesaria, aunque no esté muy claro su propósito aquí

        # Cambiando a una pantalla basada en el id del ListView
        if list_view.id == "list_pendientes":
            self.push_screen(PendientesScreen())
        elif list_view.id == "list_enProceso":
            self.push_screen(En_ProcesoScreen())
        elif list_view.id == "list_terminados":
            self.push_screen(TerminadosScreen())

# Ejecutar la aplicación
if __name__ == "__main__":
    app = TableApp()
    app.run()
