# listapendiente.py

from coleccionPendientes import ColeccionPendientes
from pendientes import Pendiente

class ListaPendientes:
    def __init__(self):
        self.coleccion = ColeccionPendientes()

    def obtener_pendientes(self):
        return self.coleccion.leer()

    def agregar_pendiente(self, descripcion):
        pendiente = Pendiente(descripcion)
        self.coleccion.insertar(pendiente)
        print(f"Pendiente '{descripcion}' agregado.")

    def actualizar_pendiente(self, old_descripcion, new_descripcion):
        self.coleccion.actualizar(old_descripcion, new_descripcion)
        print(f"Pendiente '{old_descripcion}' actualizado a '{new_descripcion}'.")

    def eliminar_pendiente(self, descripcion):
        self.coleccion.borrar(Pendiente(descripcion))
        print(f"Pendiente '{descripcion}' eliminado.")
