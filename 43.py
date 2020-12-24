direction = input("Which direction you want to go (up/down): ")

if direction == "up":

	num = int(input("Enter number: "))
	for n in range(0,num):
		print(n+1)

elif direction == "down":
	num = int(input("Enter number below 20: "))

	for n in range(20,num-1,-1):
		print(n)

else:
	print("Wrong input")