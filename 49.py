compnum = 50
guess = int(input("Enter nmber: "))
count = 1
while guess != compnum:

	if guess < compnum:
		print("Too low")
	else:
		print("Too high")

	count+=1
	guess = int(input("Do you want to enter again: "))

print("Attempts were {}".format(count))