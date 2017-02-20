import json

menu = {
	"breakfast":{
		"time":"7:00",
		"items":["Хлеб с маслом","Чай"]
	},
	'lunch':{
		'time':'12:30',
		'items':['Суп','Вода']
	}	
}

print(menu)

# json_menu = json.dumps(menu)
# with open("menu.json","wt", encoding="utf-8") as f:
# 	f.write(json_menu)


with open("menu.json","rt", encoding="utf-8") as f:
	json_menu2 = f.read()

print(json_menu2)

menu2 = json.loads(json_menu2)

print(menu2)