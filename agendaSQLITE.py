import sqlite3


class AgendaDB:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def insert(self, name, phone):
        command = 'INSERT OR IGNORE INTO AGENDA(name, phone) VALUES(?, ?)'
        self.cursor.execute(command, (name, phone))
        self.conn.commit()

    def edit(self, name, phone, id):
        command = 'UPDATE OR IGNORE AGENDA SET name=?, phone=? WHERE id=?'
        self.cursor.execute(command, (name, phone, id))
        self.conn.commit()

    def delete(self, id):
        command = 'DELETE FROM AGENDA WHERE id=?'
        self.cursor.execute(command, (id,))
        self.conn.commit()

    def list(self):
        command = 'SELECT * FROM AGENDA'
        self.cursor.execute(command)
        for line in self.cursor.fetchall():
            print(line)

    def search(self, value):
        command = 'SELECT * FROM AGENDA WHERE name LIKE ?'
        self.cursor.execute(command, (f'%{value}%',))
        for line in self.cursor.fetchall():
            print(line)

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.search('Brasil')

    agenda.close()