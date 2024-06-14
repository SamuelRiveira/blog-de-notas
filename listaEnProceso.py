# listaenProceso.py

from coleccionEnProceso import ColeccionEnProceso
from enProceso import EnProceso

class ListaEnProceso:
    def __init__(self):
        self.coleccion = ColeccionEnProceso()  # Corregido el nombre de la clase (mayúscula 'C')

    def obtener_en_proceso(self):
        return self.coleccion.leer()

    def agregar_enProceso(self, descripcion):
        enProceso = EnProceso(descripcion)
        self.coleccion.insertar(enProceso)
        print(f"EnProceso '{descripcion}' agregado.")

    def actualizar_enProceso(self, old_descripcion, new_descripcion):
        self.coleccion.actualizar(old_descripcion, new_descripcion)
        print(f"EnProceso '{old_descripcion}' actualizado a '{new_descripcion}'.")

    def eliminar_enProceso(self, descripcion):
        self.coleccion.borrar(EnProceso(descripcion))
        print(f"EnProceso '{descripcion}' eliminado.")
