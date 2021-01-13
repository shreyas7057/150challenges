
names = []

def add():

	name = input("Enter name: ")
	names.append(name)
	return names


def change():
	num = 0
	for x in names:
		print(num,x)
		num+=1

	select_num = int(input("Enter num of name you want to change: "))
	name = input("Enter new name: ")
	names[select_num] = name
	return names

def delete():
	num = 0
	for x in names:
		print(num,x)
		num+=1
	select_num = int(input("Enter number of name you want to delete: "))
	del names[select_num]
	return names


def view():
	for x in names:
		print(x)
	print()


def main():
	again = 'y'
	while again == "y":
		print("1) Add name")
		print("2) Change name")
		print("3) Delete name")
		print("4) View name")
		print("5) Quit")

		selection = int(input("Enter your choice: "))
		if selection == 1:
			names = add()

		elif selection == 2:
			names = change()

		elif selection == 3:
			names = delete()

		elif selection == 4:
			names = view()

		elif selection == 5:
			again = "n"

		else:
			print("incorrect option")
		data = (names,again)

names = []
main()
