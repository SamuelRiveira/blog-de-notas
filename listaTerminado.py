# listaTerminado.py

from coleccionTerminado import ColeccionTerminados
from terminados import Terminado

class ListaTerminados:
    def __init__(self):
        self.coleccion = ColeccionTerminados()  # Corregido el nombre de la clase (mayúscula 'C')

    def obtener_terminados(self):
        return self.coleccion.leer()

    def agregar_terminado(self, descripcion):
        terminado = Terminado(descripcion)
        self.coleccion.insertar(terminado)
        print(f"Terminado '{descripcion}' agregado.")

    def actualizar_terminado(self, old_descripcion, new_descripcion):
        self.coleccion.actualizar(old_descripcion, new_descripcion)
        print(f"Terminado '{old_descripcion}' actualizado a '{new_descripcion}'.")

    def eliminar_terminado(self, descripcion):
        self.coleccion.borrar(Terminado(descripcion))
        print(f"Terminado '{descripcion}' eliminado.")
