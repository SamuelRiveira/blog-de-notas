# coleccionEnProceso.py

from db import Db

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS en_proceso (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        pendiente TEXT NOT NULL
    )
'''

SQLDDLSELECT = '''
    SELECT id, titulo, pendiente FROM en_proceso
'''

SQLDDLINSERT = '''INSERT INTO en_proceso (titulo, pendiente) VALUES '''
# Hay que concatenar ('titulo', 'pendiente')

SQLDDLUPDATEPART1 = '''UPDATE en_proceso SET titulo = "'''
SQLDDLUPDATEPART2 = '''", pendiente = "'''
SQLDDLUPDATEPART3 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM en_proceso WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM en_proceso WHERE pendiente LIKE '''
# Hay que concatenar

class ColeccionEnProceso:
    DBNAME = 'notas.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)
        self.con.execute(SQLMDLCREATE)

    def leer(self) -> list:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, titulo, pendiente):
        if self.buscar(pendiente) == 0:
            elstr = f"('{titulo}', '{pendiente}')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, id, new_titulo, new_pendiente):
        elstr = f'{SQLDDLUPDATEPART1}{new_titulo}{SQLDDLUPDATEPART2}{new_pendiente}{SQLDDLUPDATEPART3}{id}'
        self.con.execute(elstr)

    def borrar(self, id):
        self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, pendiente:str) -> int:
        resultado = 0
        elstr = '"' + str(pendiente) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado
