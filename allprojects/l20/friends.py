from json import loads
from urllib.request import urlopen
from time import sleep

friends = []

data = urlopen("https://api.vk.com/method/friends.get?user_id=381462099").read().decode("utf-8")
data = loads(data)
friends_id = data["response"]
# print(friends_id)

for f_id in friends_id:
	data = urlopen("https://api.vk.com/method/friends.get?user_id="+str(f_id)).read().decode("utf-8")
	data = loads(data)
	# print(data)
	try:
		friends_friends_id = data["response"]
	except:
		continue
	friends.append([f_id,len(set(friends_friends_id) & set(friends_id))])
	sleep(0.2)
	print(".",end="")

print()
friends.sort(key=lambda x: -x[1])
print(friends)
