import sqlite3
conn = sqlite3.connect("weapon_shop.db")
curs = conn.cursor()

curs.execute("SELECT * FROM weapons")
rows = curs.fetchall()
# print(rows)

curs.execute("SELECT name, cost FROM weapons WHERE cost < 4000 ORDER BY cost DESC LIMIT 2")
rows = curs.fetchall()
for row in rows:
	print("Название оружия: {0[0]}, Цена оружия: {0[1]}".format(row))

curs.execute("UPDATE weapons SET name = 'АминоСтвол', cost = 30000 WHERE name = 'P90'")
curs.execute("DELETE FROM weapons WHERE name = 'Desert Eagle'")
conn.commit()

curs.execute("SELECT * FROM weapons")
rows = curs.fetchall()
print(rows)


curs.close()
conn.close()