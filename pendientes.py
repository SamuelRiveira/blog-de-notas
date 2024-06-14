class Pendiente:
    def __init__(self, pendiente:str) -> None:
        self.pendiente = pendiente

    def __str__(self) -> str:
        return self.pendiente
    
    def leer(self) -> str:
        return self.pendiente