from array import *

num = array('i',[])

for i in range(0,5):
	n = int(input("Enter number: "))
	num.append(n)
print(num)

sort_num = sorted(num)
print(sort_num)

rem_num = int(input("Enter any number from array to delete: "))

if rem_num in sort_num:
	sort_num.remove(rem_num)
	print(sort_num)

else:
	print("Not Found ")