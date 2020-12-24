num = int(input("Enter number between 10 to 20: "))

while num<10 or num>20:
	if num<10:
		print("Too low")

	else:
		print("Too high")

	num = int(input("Try again..."))
print("Thank you")