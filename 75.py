num_l = [123,456,789,412]


for i in num_l:
	print(i)

guess = int(input("GUess the number: "))

if guess in i:
	print(num_l.index(guess))
	
else:
	print("Num not in list")
	
