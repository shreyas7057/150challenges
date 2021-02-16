import sqlite3

with sqlite3.connect("Phonebook.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(id integer PRIMARY KEY, firstname text, surname text, phonenumber text); """)

cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)VALUES("1","def","uvw","5678")""")
db.commit()

cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)VALUES("2","ghi","klm","454545")""")
db.commit()

cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)VALUES("3","abc","xyz","1234")""")
db.commit()

cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)VALUES("4","abc","xyz","1234")""")
db.commit()

cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)VALUES("5","abc","xyz","1234")""")
db.commit()

db.close()