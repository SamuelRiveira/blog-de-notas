from coleccionPendientes import ColeccionPendientes
from coleccionEnProceso import ColeccionEnProceso
from coleccionTerminado import ColeccionTerminados

from textual.app import ComposeResult, App
from textual.screen import Screen
from textual.containers import Container, Grid
from textual.widgets import Label, Static, Footer, Input, Button
from textual.binding import Binding

global current_id
global current_title
global current_description

class ObtenerDetalles:

    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        global current_id
        global current_title
        global current_description
        current_id = id
        current_title = str(self.title)
        current_description = str(self.description)

    def mostrar_detalles(self):
        return self.id, self.title, self.description

# Pantalla para insertar nuevos pendientes
class InsertarPendientes(Screen):
    CSS_PATH = "confirmacion.tcss"

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
            self.app.push_screen(ConfirmarInsertarPendiente(self.titulo_input.value, self.contenido_input.value))

# Confirmación para insertar nuevos pendientes
class ConfirmarInsertarPendiente(Screen):
    def __init__(self, titulo_input_value, contenido_input_value):
        super().__init__()
        self.titulo_input_value = titulo_input_value
        self.contenido_input_value = contenido_input_value

    def compose(self) -> ComposeResult:
        return [
            Grid(
                Label("¿Estás seguro de que quieres insertar la nota?", id="question"),
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
            self.app.pop_screen()  # Para volver a la pantalla anterior
        elif event.button.id == "cancel":
            self.app.pop_screen()

# Pantalla para actualizar pendientes
class ActualizarPendientes(Screen):
    CSS_PATH = "confirmacion.tcss"

    def compose(self) -> ComposeResult:
        global current_id
        global current_title
        global current_description

        self.titulo_input = Input(placeholder="Título", id="titulo_input", value=current_title)
        self.contenido_input = Input(placeholder="Contenido", id="contenido_input", value=current_description)
        self.actualizar_button = Button("Actualizar", variant="error", id="actualizar")
        self.cancelar_button = Button("Cancelar", variant="primary", id="cancelar")

        yield self.titulo_input
        yield self.contenido_input
        yield self.actualizar_button
        yield self.cancelar_button

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cancelar":
            self.app.pop_screen()
        elif event.button.id == "actualizar":
            self.app.push_screen(ConfirmarActualizarPendiente(current_id, self.titulo_input.value, self.contenido_input.value))

# Confirmación para actualizar pendientes
class ConfirmarActualizarPendiente(Screen):
    def __init__(self, nota_id, titulo_input_value, contenido_input_value):
        super().__init__()
        self.nota_id = nota_id  # Usamos nota_id en lugar de id
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
            cp.actualizar(self.nota_id, self.titulo_input_value, self.contenido_input_value)
            self.app.pop_screen()
            self.app.pop_screen()  # Para volver a la pantalla anterior
        elif event.button.id == "cancel":
            self.app.pop_screen()

# Pantalla para mostrar detalles de pendientes
class PendientesScreen(Screen):

    CSS_PATH = "ventanaPendientes.tcss"

    BINDINGS = [
        Binding(key="q", action="volver", description="Volver", key_display="Q"),
        Binding(key="e", action="actualizar", description="Actualizar", key_display="R"),
        Binding(key="d", action="borrar", description="Borrar", key_display="D"),
        Binding(key="h", action="insertar", description="Insertar", key_display="H")
    ]

    def compose(self) -> ComposeResult:
        global current_title
        global current_description

        with Container(id="main_container"):
            yield Label(current_title, id="titulo")
            with Container(id="contenedor-descripcion"):
                yield Static(current_description, id="descripcion")
        yield Footer()

    def action_insertar(self):
        self.app.push_screen(InsertarPendientes())

    def action_volver(self):
        self.app.pop_screen()

    def action_actualizar(self):
        self.app.push_screen(ActualizarPendientes())

    def action_borrar(self):
        pass

# Pantalla para insertar nuevas tareas en proceso
class InsertarEnProceso(Screen):
    CSS_PATH = "confirmacion.tcss"

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
            self.app.push_screen(ConfirmarInsertarEnProceso(self.titulo_input.value, self.contenido_input.value))

# Confirmación para insertar nuevas tareas en proceso
class ConfirmarInsertarEnProceso(Screen):
    def __init__(self, titulo_input_value, contenido_input_value):
        super().__init__()
        self.titulo_input_value = titulo_input_value
        self.contenido_input_value = contenido_input_value

    def compose(self) -> ComposeResult:
        return [
            Grid(
                Label("¿Estás seguro de que quieres insertar la nota?", id="question"),
                Button("Confirmar", variant="error", id="confirmar"),
                Button("Cancelar", variant="primary", id="cancel"),
                id="dialog",
            )
        ]

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "confirmar":
            cep = ColeccionEnProceso()
            cep.insertar(self.titulo_input_value, self.contenido_input_value)
            self.app.pop_screen()
            self.app.pop_screen()  # Para volver a la pantalla anterior
        elif event.button.id == "cancel":
            self.app.pop_screen()

# Pantalla para actualizar tareas en proceso
class ActualizarEnProceso(Screen):
    CSS_PATH = "confirmacion.tcss"

    def compose(self) -> ComposeResult:
        global current_id
        global current_title
        global current_description

        self.titulo_input = Input(placeholder="Título", id="titulo_input", value=current_title)
        self.contenido_input = Input(placeholder="Contenido", id="contenido_input", value=current_description)
        self.actualizar_button = Button("Actualizar", variant="error", id="actualizar")
        self.cancelar_button = Button("Cancelar", variant="primary", id="cancelar")

        yield self.titulo_input
        yield self.contenido_input
        yield self.actualizar_button
        yield self.cancelar_button

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cancelar":
            self.app.pop_screen()
        elif event.button.id == "actualizar":
            self.app.push_screen(ConfirmarActualizarEnProceso(current_id, self.titulo_input.value, self.contenido_input.value))

# Confirmación para actualizar tareas en proceso
class ConfirmarActualizarEnProceso(Screen):
    def __init__(self, nota_id, titulo_input_value, contenido_input_value):
        super().__init__()
        self.nota_id = nota_id  # Usamos nota_id en lugar de id
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
            cep = ColeccionEnProceso()
            cep.actualizar(self.nota_id, self.titulo_input_value, self.contenido_input_value)
            self.app.pop_screen()
            self.app.pop_screen()  # Para volver a la pantalla anterior
        elif event.button.id == "cancel":
            self.app.pop_screen()

# Pantalla para mostrar detalles de tareas en proceso
class En_ProcesoScreen(Screen):

    CSS_PATH = "ventanaEnProceso.tcss"

    BINDINGS = [
        Binding(key="q", action="volver", description="Volver", key_display="Q"),
        Binding(key="e", action="actualizar", description="Actualizar", key_display="R"),
        Binding(key="d", action="borrar", description="Borrar", key_display="D"),
        Binding(key="h", action="insertar", description="Insertar", key_display="H")
    ]

    def compose(self) -> ComposeResult:
        global current_title
        global current_description

        with Container(id="main_container"):
            yield Label(current_title, id="titulo")
            with Container(id="contenedor-descripcion"):
                yield Static(current_description, id="descripcion")
        yield Footer()

    def action_insertar(self):
        self.app.push_screen(InsertarEnProceso())

    def action_volver(self):
        self.app.pop_screen()

    def action_actualizar(self):
        self.app.push_screen(ActualizarEnProceso())

    def action_borrar(self):
        pass

# Pantalla para insertar nuevas tareas terminadas
class InsertarTerminado(Screen):
    CSS_PATH = "confirmacion.tcss"

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
            self.app.push_screen(ConfirmarInsertarTerminado(self.titulo_input.value, self.contenido_input.value))

# Confirmación para insertar nuevas tareas terminadas
class ConfirmarInsertarTerminado(Screen):
    def __init__(self, titulo_input_value, contenido_input_value):
        super().__init__()
        self.titulo_input_value = titulo_input_value
        self.contenido_input_value = contenido_input_value

    def compose(self) -> ComposeResult:
        return [
            Grid(
                Label("¿Estás seguro de que quieres insertar la nota?", id="question"),
                Button("Confirmar", variant="error", id="confirmar"),
                Button("Cancelar", variant="primary", id="cancel"),
                id="dialog",
            )
        ]

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "confirmar":
            ct = ColeccionTerminados()
            ct.insertar(self.titulo_input_value, self.contenido_input_value)
            self.app.pop_screen()
            self.app.pop_screen()  # Para volver a la pantalla anterior
        elif event.button.id == "cancel":
            self.app.pop_screen()

# Pantalla para actualizar tareas terminadas
class ActualizarTerminados(Screen):
    CSS_PATH = "confirmacion.tcss"

    def compose(self) -> ComposeResult:
        global current_id
        global current_title
        global current_description

        self.titulo_input = Input(placeholder="Título", id="titulo_input", value=current_title)
        self.contenido_input = Input(placeholder="Contenido", id="contenido_input", value=current_description)
        self.actualizar_button = Button("Actualizar", variant="error", id="actualizar")
        self.cancelar_button = Button("Cancelar", variant="primary", id="cancelar")

        yield self.titulo_input
        yield self.contenido_input
        yield self.actualizar_button
        yield self.cancelar_button

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cancelar":
            self.app.pop_screen()
        elif event.button.id == "actualizar":
            self.app.push_screen(ConfirmarActualizarTerminado(current_id, self.titulo_input.value, self.contenido_input.value))

# Confirmación para actualizar tareas terminadas
class ConfirmarActualizarTerminado(Screen):
    def __init__(self, nota_id, titulo_input_value, contenido_input_value):
        super().__init__()
        self.nota_id = nota_id  # Usamos nota_id en lugar de id
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
            ct = ColeccionTerminados()
            ct.actualizar(self.nota_id, self.titulo_input_value, self.contenido_input_value)
            self.app.pop_screen()
            self.app.pop_screen()  # Para volver a la pantalla anterior
        elif event.button.id == "cancel":
            self.app.pop_screen()

# Pantalla para mostrar detalles de tareas terminadas
class TerminadosScreen(Screen):

    CSS_PATH = "ventanaTerminados.tcss"

    BINDINGS = [
        Binding(key="q", action="volver", description="Volver", key_display="Q"),
        Binding(key="e", action="actualizar", description="Actualizar", key_display="R"),
        Binding(key="d", action="borrar", description="Borrar", key_display="D"),
        Binding(key="h", action="insertar", description="Insertar", key_display="H")
    ]

    def compose(self) -> ComposeResult:
        global current_title
        global current_description

        with Container(id="main_container"):
            yield Label(current_title, id="titulo")
            with Container(id="contenedor-descripcion"):
                yield Static(current_description, id="descripcion")
        yield Footer()

    def action_insertar(self):
        self.app.push_screen(InsertarTerminado())

    def action_volver(self):
        self.app.pop_screen()

    def action_actualizar(self):
        self.app.push_screen(ActualizarTerminados())

    def action_borrar(self):
        pass