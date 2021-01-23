import csv

def add():
	file = open("Salaries.csv","a")
	name = input("Enter name: ")
	salary = int(input("Enter salary: "))
	new_rec = name+', '+str(salary)+'\n'
	file.write(new_rec)
	file.close()


def view():
	file = open("Salaries.csv","r")
	for row in file:
		print(row)
	file.close()


def delete():
	file = open("Salaries.csv","r")
	x = 0
	tmplist = []
	for row in file:
		tmplist.append(row)
	file.close()
	for row in tmplist:
		print(x,row)
		x+=1
	rowdel = int(input("Enter row number: "))
	del tmplist[rowdel]
	file = open("Salaries.csv","w")
	for row in tmplist:
		file.write(row)
	file.close()

tryagain = True

while tryagain == True:
	print("1) Add to file")
	print("2) View records")
	print("3) Delete record")
	print("4) Quit")
	selection = input("Enter number to select: ")
	if selection == "1":
		add()
	elif selection == "2":
		view()
	elif selection == "3":
		delete()
	elif selection == "4":
		tryagain = False
	else:
		print("Incorrect option")