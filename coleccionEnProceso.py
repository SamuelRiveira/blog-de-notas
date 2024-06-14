# coleccionTerminado.py

from db import Db
from enProceso import EnProceso

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS enProcesos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        enProceso TEXT NOT NULL
    )
'''

SQLDDLSELECT = '''
    SELECT * FROM enProcesos
'''

SQLDDLINSERT = '''INSERT INTO enProcesos (enProceso) VALUES '''
# Hay que concatenar ('enProceso')

SQLDDLUPDATEPART1 = '''UPDATE enProcesos SET enProceso = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM enProcesos WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM enProcesos WHERE enProceso LIKE '''
# Hay que concatenar

class ColeccionEnProceso:
    DBNAME = 'notas.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)
        self.con.execute(SQLMDLCREATE)

    def leer(self) -> list:
        """
        Lee todas las notas terminadas desde la base de datos.
        Retorna una lista de tuplas (id, enProceso).
        """
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, enProceso):
        if self.buscar(enProceso) == 0:
            elstr = "('" + str(enProceso) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldenProceso:str, newenProceso:str):
        id = self.buscar(oldenProceso)
        if id != 0 and self.buscar(newenProceso) == 0:
            elstr = SQLDDLUPDATEPART1 + newenProceso 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, enProceso):
        id = self.buscar(enProceso) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, enProceso:EnProceso) -> int:
        resultado = 0
        elstr = '"' + str(enProceso) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado
