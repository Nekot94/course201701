import json
menu = {
	'breakfast': {
		'time': 7.33,
		'items': ['Хлеб с сыром', 'Чай']
	},
	'lunch': {
		'time': 13.50,
		'items': ['Хинкал','Салат Московский','Сок']
	}
}
# print(menu)
# menu_json = json.dumps(menu)
# with open("menu_json.json", "wt", encoding="utf-8") as f:
# 	f.write(menu_json)

with open("menu_json.json", "rt", encoding="utf-8") as f:
	menu2_json = f.read()

print(menu2_json)
menu2 = json.loads(menu2_json)
print(menu2)
print("\u0421")