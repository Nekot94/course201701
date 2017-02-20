import xml.etree.ElementTree as et
tree = et.parse("menu.xml")
root = tree.getroot()
print(root.tag)
for child in root:
	print("тэг:",child.tag,'атрибут:',child.attrib)
	for grandchild in child:
		print("\tтэг:",grandchild.tag,'атрибут:',grandchild.attrib)
		print("\t\t", grandchild.text)