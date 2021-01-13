import random

def rand_num():
	low_num = int(input("Enter low end: "))
	high_num = int(input("Enter high end: "))
	comp_num = random.randint(low_num,high_num)
	print(comp_num)


def guess_num():
	print("I am thinking of a number...")
	num = int(input("Guess the number: "))
	return num


def check_num():
	trying = True
	
	rand_value = rand_num()
	usr_value = guess_num()
	
	while trying==True:

		if rand_value == usr_value:
			print("Correct you win")
			
			trying = False

		else:
			print('Try again')
			rand_num()
			guess_num()
			

check_num()