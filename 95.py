from array import *


num = array('f',[11,22,33,44,55])

tryagain = True

while tryagain == True:
	n = int(input("Enter number between 2 and 5: "))

	if n<2 or n>5:
		print("Wrong input")
	else:
		tryagain = False


for i in range(0,5):
	ans = num[i]/n
	print(ans)