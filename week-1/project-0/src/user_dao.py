import sqlite3

from user import User




# cursor.execute(
#     """CREATE TABLE USER(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(20),
#         email VARCHAR(20),
#         password VARCHAR(20)
#     )"""
# )

class UserDAO:
    con = sqlite3.connect("sample.db", check_same_thread=False)
    cursor = con.cursor()
    # def __init__(self):
    #     self.cursor.execute(
    # """CREATE TABLE USER(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name VARCHAR(20),
    #     email VARCHAR(20),
    #     password VARCHAR(20)
    # )""")
    #     self.con.commit()

    def create_user(self, user:User):
        self.cursor.execute(
            """INSERT INTO USER(name, email, password) VALUES(?, ?, ?)""",
            (user.name, user.email, user.password),
        )
        

        self.con.commit()
        return "created"
    
    def get_users(self):
        res = self.cursor.execute(
            """SELECT * from USER"""
        )
        self.con.commit()
        return res.fetchall()
    
