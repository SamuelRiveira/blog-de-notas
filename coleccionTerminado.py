# coleccionTerminado.py

from db import Db
from terminados import Terminado

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS terminados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        terminado TEXT NOT NULL
    )
'''

SQLDDLSELECT = '''
    SELECT * FROM terminados
'''

SQLDDLINSERT = '''INSERT INTO terminados (terminado) VALUES '''
# Hay que concatenar ('terminado')

SQLDDLUPDATEPART1 = '''UPDATE terminados SET terminado = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM terminados WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM terminados WHERE terminado LIKE '''
# Hay que concatenar

class ColeccionTerminados:
    DBNAME = 'notas.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)
        self.con.execute(SQLMDLCREATE)

    def leer(self) -> list:
        """
        Lee todas las notas terminadas desde la base de datos.
        Retorna una lista de tuplas (id, terminado).
        """
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, terminado):
        if self.buscar(terminado) == 0:
            elstr = "('" + str(terminado) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldterminado:str, newterminado:str):
        id = self.buscar(oldterminado)
        if id != 0 and self.buscar(newterminado) == 0:
            elstr = SQLDDLUPDATEPART1 + newterminado 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, terminado):
        id = self.buscar(terminado) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, terminado:Terminado) -> int:
        resultado = 0
        elstr = '"' + str(terminado) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado
