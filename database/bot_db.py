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
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_user(self, tg_id, username, lastname, firstname):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY
            (None, tg_id, username, lastname, firstname)
        )
        self.connection.commit()

    def sql_insert_ban_user(self, tg_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY
            (None, tg_id, 1,)
        )
        self.connection.commit()

    def sql_select_ban_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": [0],
            "telegram_id": row[1],
            "count": row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY
            (tg_id,)
        ).fetchone()

    def sql_update_ban_count(self, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_COUNT_QUERY
            (tg_id,)
        )
        self.connection.commit()