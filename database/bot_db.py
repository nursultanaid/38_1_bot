import sqlite3
from database import sql_queries

class BotDB:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_table(self):
        if self.connection:
            print("Database connected successfully!")

        self.connection.execute(sql_queries.CREATE_USER_QUERY)
        self.connection.commit()

    def sql_insert_user(self, tg_id, username, lastname, firstname):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY
            (None, tg_id, username, lastname, firstname)
        )
        self.connection.commit()