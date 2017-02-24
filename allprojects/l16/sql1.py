import sqlite3
conn = sqlite3.connect('magic_shop.db')
curs = conn.cursor()
curs.execute("DROP TABLE items")
curs.execute("""CREATE TABLE items
(name VARCHAR(50) PRIMARY KEY,
count INT,
price REAL,
country VARCHAR(50))
""")

curs.execute("INSERT INTO items VALUES('Молоко дракона',5,5000,'Китай')")
curs.execute("INSERT INTO items VALUES('Посох Исы',1,20.5,'Махачкала')")
name, count, price, country = 'Укус Шмеля', 5, 777.777, 'Махачкала'
curs.execute("INSERT INTO items VALUES(?, ?, ?, ?)", (name, count, price, country))
ins = "INSERT INTO items VALUES(?, ?, ?, ?)"
name, count, price, country = 'Бес', 10, 30, 'Преисподняя'
curs.execute(ins, (name, count, price, country))
conn.commit()

curs.close()
conn.close()


