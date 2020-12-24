num = 10
while num>0:
	print("There are {0} green bottles on wall".format(num))
	print(f"{num} green bottle hanging on wall")
	print("And if 1 green bottle accidently fall")
	num = num -1
	ans = int(input("How many bottles on wall"))

	if ans == num:
		print(f"There will be {num} bottles on the wall")

	else:
		while ans!=num:
			ans = int(input("No try again"))

print("There are no more green bottles on walls.")