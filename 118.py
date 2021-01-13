def number():
	num = int(input("Enter number: "))
	return num


def count():
	x = 1
	for i in range(1,number()):
		print(i)
		x+=1


count()