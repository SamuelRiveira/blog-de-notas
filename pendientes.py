# pendientes.py

class Pendiente:
    def __init__(self, titulo: str, descripcion: str) -> None:
        self.titulo = titulo
        self.descripcion = descripcion

    def __str__(self) -> str:
        return f"{self.titulo} - {self.descripcion}"
    
    def leer_titulo(self) -> str:
        return self.titulo
    
    def leer_descripcion(self) -> str:
        return self.descripcion
