l = {}

for i in range(0,4):
	name = input("Enter name: ")
	age = int(input("Enter age: "))
	shoe_size = int(input("Enter shoe size: "))

	l[name] = {"Age":age,"Shoe Size":shoe_size}

usr_nm = input("Enter name to display: ")
print(l[usr_nm])


