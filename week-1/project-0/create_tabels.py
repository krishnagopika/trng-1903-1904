import sqlite3

con = sqlite3.connect('C:/TrainingMaterial/TRNG-00001903-1904/trng-1903-1904/week-1/project-0/src/revhire.db')

cursor = con.cursor()


cursor.execute(
    """CREATE TABLE USER(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20),
        email VARCHAR(20),
        password VARCHAR(20),
        role VARCHAR(20)
    )""")

con.commit()

con.close()


