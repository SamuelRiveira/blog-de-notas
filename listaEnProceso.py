# listaEnProceso.py

from coleccionEnProceso import ColeccionEnProceso
from pendientes import Pendiente

class ListaEnProceso:
    def __init__(self):
        self.coleccion = ColeccionEnProceso()

    def obtener_en_proceso(self):
        return self.coleccion.leer()

    def agregar_en_proceso(self, titulo, descripcion):
        en_proceso = Pendiente(titulo, descripcion)
        self.coleccion.insertar(titulo, descripcion)
        print(f"En proceso '{titulo}' agregado.")

    def actualizar_en_proceso(self, id, new_titulo, new_descripcion):
        self.coleccion.actualizar(id, new_titulo, new_descripcion)
        print(f"En proceso ID '{id}' actualizado a '{new_titulo}'.")

    def eliminar_en_proceso(self, id):
        self.coleccion.borrar(id)
        print(f"En proceso ID '{id}' eliminado.")
