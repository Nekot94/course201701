import sqlite3
conn = sqlite3.connect('magic_shop.db')
curs = conn.cursor()

curs.execute("SELECT * FROM items")
rows = curs.fetchall()
# print(rows)
curs.execute("SELECT name, price FROM items WHERE price > 30") 
# rows = curs.fetchall()
# print(rows)
curs.execute("SELECT * FROM items WHERE count > 1 ORDER BY count DESC LIMIT 2") 
rows = curs.fetchall()
for row in rows:
	print("Имя: {0[0]}, Количество {0[1]}".format(row))

curs.execute("UPDATE items SET name='Посох Трусы', price=100000 WHERE name='Посох Исы'")
curs.execute("DELETE FROM items WHERE name='Молоко дракона'")
curs.execute("SELECT * FROM items")
rows = curs.fetchall()
print(rows)



curs.close()
conn.close()