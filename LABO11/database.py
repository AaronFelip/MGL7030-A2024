import sqlite3
from livre import Livre


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/livre.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()