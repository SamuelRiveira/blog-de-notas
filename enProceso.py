class EnProceso:
    def __init__(self, en_proceso:str) -> None:
        self.en_proceso = en_proceso

    def __str__(self) -> str:
        return self.en_proceso
    
    def leer(self) -> str:
        return self.en_proceso