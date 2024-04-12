import sqlite3

con = sqlite3.connect("sample.db")

cursor = con.cursor()

# cursor.execute(
#     """CREATE TABLE USER(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(20),
#         email VARCHAR(20),
#         password VARCHAR(20)
#     )"""
# )

cursor.execute(
    """INSERT INTO USER(name, email, password) VALUES("Jane Doe", "jane.doe@example.com", "John@123")"""
)

res = cursor.execute(
    """SELECT * FROM USER"""
).fetchall()

print(res)


con.commit()

con.close()
