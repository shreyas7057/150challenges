import random

score = 0

for i in range(1,6):
	num1 = random.randint(1,50)
	num2 = random.randint(1,50)

	correct = num1+num2
	ans = int(input("Enter your ans: "))
	if ans == correct:
		score = score+1
print("Your score is {0}".format(score))