import random

colors = ['black','green','blue','red','yellow']
rand_color = random.choice(colors)
print(rand_color)



while True:
	
	usr_color = input("Enter color: ")

	if rand_color == usr_color:
		print("Well done")
		break

	else:
		if rand_color == "black":
			print("Its black color")
			
		elif rand_color == "green":
			print("Its green color")
			
		elif rand_color == "blue":
			print("Its blue color")
			
		elif rand_color == "red":
			print("Its red color")
			
		elif rand_color == "yellow":
			print("Its yellow color")
			