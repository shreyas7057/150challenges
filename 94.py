from array import *

num = array('i',[1,2,3,4,5])
print(num)

sel_num = int(input("Enter number from array: "))

choice = True

while choice == True:

	if sel_num in num:
		pos = num.index(sel_num)
		print(f"The position of {sel_num} in array is {pos}")
		choice = False

	else:
		print("Wrong input")
		sel_num = int(input("Enter number from array: "))