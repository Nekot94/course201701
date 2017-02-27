from PIL import Image

im = Image.open("gopher.jpg")
pixels = im.load()

x, y = im.size

# print(x, y)
# print(im)
br = int(input("На сколько изменить яркость: "))
for i in range(x):
	for j in range(y):
		r, g, b = pixels[i, j]
		pixels[i, j] = r + br, g + br, b + br

im.save("gopher2.jpg")
im.show()