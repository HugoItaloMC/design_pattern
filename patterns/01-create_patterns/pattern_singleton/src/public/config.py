from metasingle import Singleton
import sqlite3


class DataBase(metaclass=Singleton):

    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db.first')
            self.cursor = self.connection.cursor()
        return self.cursor
