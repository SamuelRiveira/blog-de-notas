# main.py

from coleccionPendientes import ColeccionPendientes
from coleccionEnProceso import ColeccionEnProceso
from coleccionTerminado import ColeccionTerminados

def main():
    # Crear una instancia de ColeccionPendientes
    cp = ColeccionPendientes()

    # Insertar los pendientes con títulos y descripciones
    cp.insertar("Título Pendiente 1", "Descripción del pendiente 1")
    cp.insertar("Título Pendiente 2", "Descripción del pendiente 2")
    cp.insertar("Título Pendiente 3", "Descripción del pendiente 3")

    # Crear una instancia de ColeccionEnProceso
    cep = ColeccionEnProceso()

    # Insertar los en proceso con títulos y descripciones
    cep.insertar("Título En Proceso 1", "Descripción del en proceso 1")
    cep.insertar("Título En Proceso 2", "Descripción del en proceso 2")
    cep.insertar("Título En Proceso 3", "Descripción del en proceso 3")

    # Crear una instancia de ColeccionTerminados
    ct = ColeccionTerminados()

    # Insertar los terminados con títulos y descripciones
    ct.insertar("Título Terminado 1", "Descripción del terminado 1")
    ct.insertar("Título Terminado 2", "Descripción del terminado 2")
    ct.insertar("Título Terminado 3", "Descripción del terminado 3")

    # Mostrar que los títulos y descripciones han sido insertados
    print("Títulos y descripciones insertados exitosamente.")

if __name__ == "__main__":
    main()
