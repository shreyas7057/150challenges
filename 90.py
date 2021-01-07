from array import *

num = array('i',[])

while len(num)<5:

	ip_array = int(input("Enter number: "))

	if ip_array >=10 and ip_array<=20:
		num.append(ip_array)

	else:
		print('Out of range')
print(num)


