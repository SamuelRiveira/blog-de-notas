class Terminado:
    def __init__(self, terminado:str) -> None:
        self.terminado = terminado

    def __str__(self) -> str:
        return self.terminado
    
    def leer(self) -> str:
        return self.terminado