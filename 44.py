num = int(input("How many persons you want to invite for party: "))

if num >=10:
	print("Too many peoples")

else:

	for nm in range(0,num):
		names = input("Name of people: ")
		print(f"{names} has been invited")