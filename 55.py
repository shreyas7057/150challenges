import random

choice = random.randint(0,5)

usr = int(input('Enter number between 0 to 5: '))

if choice == usr:
	print("Well done")

else:
	
	if choice < usr:
		print("Too high")

	else:
		print("Too low")

	usr = int(input('Enter number between 0 to 5: '))

	if choice == usr:
		print("Correct")
	else:
		print("You loose")
print(choice)