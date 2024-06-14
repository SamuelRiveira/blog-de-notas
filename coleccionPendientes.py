# coleccionTerminado.py

from db import Db
from pendientes import Pendiente

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS pendientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pendiente TEXT NOT NULL
    )
'''

SQLDDLSELECT = '''
    SELECT * FROM pendientes
'''

SQLDDLINSERT = '''INSERT INTO pendientes (pendiente) VALUES '''
# Hay que concatenar ('pendiente')

SQLDDLUPDATEPART1 = '''UPDATE pendientes SET pendiente = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM pendientes WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM pendientes WHERE pendiente LIKE '''
# Hay que concatenar

class ColeccionPendientes:
    DBNAME = 'notas.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)
        self.con.execute(SQLMDLCREATE)

    def leer(self) -> list:
        """
        Lee todas las notas terminadas desde la base de datos.
        Retorna una lista de tuplas (id, pendiente).
        """
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, pendiente):
        if self.buscar(pendiente) == 0:
            elstr = "('" + str(pendiente) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldpendiente:str, newpendiente:str):
        id = self.buscar(oldpendiente)
        if id != 0 and self.buscar(newpendiente) == 0:
            elstr = SQLDDLUPDATEPART1 + newpendiente 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, pendiente):
        id = self.buscar(pendiente) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, pendiente:Pendiente) -> int:
        resultado = 0
        elstr = '"' + str(pendiente) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado
