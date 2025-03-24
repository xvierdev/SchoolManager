import sqlite3
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class DataBase:
    def __init__(self, db_name):
        with self.conn as sqlite3.connect(db_name):
            self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                            id INTEGER PRIMARY KEY,
                            nome TEXT NOT NULL,
                            idade INTEGER NOT NULL
                            )        
        ''')
    
    def insert_student(self, student):
        self.cursor.execute('INSERT INTO alunos (nome, idade) VALUES (?, ?)', (student.name, student.idade))
        self.conn.commit()