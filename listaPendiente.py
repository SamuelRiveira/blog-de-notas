# listaPendiente.py

from coleccionPendientes import ColeccionPendientes
from pendientes import Pendiente

class ListaPendientes:
    def __init__(self):
        self.coleccion = ColeccionPendientes()

    def obtener_pendientes(self):
        return self.coleccion.leer()

    def agregar_pendiente(self, titulo, descripcion):
        pendiente = Pendiente(titulo, descripcion)
        self.coleccion.insertar(titulo, descripcion)
        print(f"Pendiente '{titulo}' agregado.")

    def actualizar_pendiente(self, id, new_titulo, new_descripcion):
        self.coleccion.actualizar(id, new_titulo, new_descripcion)
        print(f"Pendiente ID '{id}' actualizado a '{new_titulo}'.")

    def eliminar_pendiente(self, id):
        self.coleccion.borrar(id)
        print(f"Pendiente ID '{id}' eliminado.")
