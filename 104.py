l = {}

for i in range(0,4):
	name = input("Enter name: ")
	age = int(input("Enter age: "))
	shoe_size = int(input("Enter shoe size: "))
	l[name] = {"Age":age,"Shoe Size":shoe_size}

rmv = input("Enter name to remove: ")
del l[rmv]

for name in l:
	print((name),list[name]["Age"],list[name]['Shoe Size'])