import random

usr = int(input("Enter number between 1 to 10: "))
choice = random.randint(1,10)

while choice != usr:

	if choice>usr:
		print("Computer was too high")

	else:
		print("Computer was low")
		
	usr = int(input("Enter number between 1 to 10: "))
print(choice)