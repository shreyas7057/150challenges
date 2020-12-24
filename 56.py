import random

usr = int(input("Enter number between 1 to 10: "))
choice = random.randint(1,10)

while choice != usr:
	usr = int(input("Enter number between 1 to 10: "))
print(choice)