import csv


def add():
	file = open("Salaries.csv","a")
	name = input("Enter name: ")
	salary = int(input("Enter salary: "))
	new_rec = name+ " "+str(salary)+"\n"
	file.write(str(new_rec))
	file.close()


def view():
	file = open("Salaries.csv","r")
	for row in file:
		print(row)
	file.close()


again = True

while again == True:
	print("1) Add to file")
	print("2) View records")
	print("3) Quit")
	select = int(input("Enter choice: "))

	if select == 1:
		add()

	elif select == 2:
		view()

	elif select == 3:
		again = False

	else:
		print("Incorrect option")