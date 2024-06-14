# main.py

from coleccionTerminado import ColeccionTerminados
from coleccionEnProceso import ColeccionEnProceso
from coleccionPendientes import ColeccionPendientes

def main():
    # Crear una instancia de ColeccionTerminados
    
    ct = ColeccionPendientes()

    # Insertar los tres descripciones
    ct.insertar("Pendiente 1")
    ct.insertar("Pendiente 2")
    ct.insertar("Pendiente 3")

    ct = ColeccionEnProceso()

    # Insertar los tres descripciones
    ct.insertar("En proceso 1")
    ct.insertar("En proceso 2")
    ct.insertar("En proceso 3")

    ct = ColeccionTerminados()

    # Insertar los tres descripciones
    ct.insertar("Terminados 1")
    ct.insertar("Terminados 2")
    ct.insertar("Terminados 3")

    # Mostrar que los descripciones han sido insertados
    print("descripciones insertados exitosamente.")

if __name__ == "__main__":
    main()
