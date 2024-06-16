# listaTerminados.py

from coleccionTerminado import ColeccionTerminados
from pendientes import Pendiente

class ListaTerminados:
    def __init__(self):
        self.coleccion = ColeccionTerminados()

    def obtener_terminados(self):
        return self.coleccion.leer()

    def agregar_terminado(self, titulo, descripcion):
        terminado = Pendiente(titulo, descripcion)
        self.coleccion.insertar(titulo, descripcion)
        print(f"Terminado '{titulo}' agregado.")

    def actualizar_terminado(self, id, new_titulo, new_descripcion):
        self.coleccion.actualizar(id, new_titulo, new_descripcion)
        print(f"Terminado ID '{id}' actualizado a '{new_titulo}'.")

    def eliminar_terminado(self, id):
        self.coleccion.borrar(id)
        print(f"Terminado ID '{id}' eliminado.")
