from PIL import Image

im = Image.open("gopher.jpg")
pixels = im.load()

x, y = im.size

# print(x, y)
# print(im)
for i in range(x):
	for j in range(y):
		r, g, b = pixels[i, j]
		pixels[i, j] = 0, g, 0

im.save("gopher2.jpg")
im.show()