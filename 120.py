import random

def add_sum(n1,n2):
	rand_n1 = random.randint(5,20)
	rand_n2 = random.randint(5,20)
	rand_res = rand_n1+rand_n2
	res = n1+n2
	print(f"User result {res}")
	print(f"Random result {rand_res}")

	if rand_res == res:
		print("Correct")

	else:
		print("Incorrect")


def sub_num(n1,n2):
	rand_n1 = random.randint(25,50)
	rand_n2 = random.randint(1,25)
	rand_res = rand_n1-rand_n2
	res = n1-n2
	print(f"User result {res}")
	print(f"Random result {rand_res}")

	if rand_res == res:
		print("Correct")

	else:
		print("Incorrect")


def result():
	n1 = int(input("Enter number 1: "))
	n2 = int(input("Enter number 2: "))
	choice = int(input("Enter choice(1 for add 2 for sub) : "))

	if choice == 1:
		add_sum(n1,n2)

	elif choice == 2:
		sub_num(n1,n2)

	else:
		print("Enter proper option")


result()