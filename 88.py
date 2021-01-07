from array import *

num = []


for i in range(0,5):
	ip_num = int(input("Enter number: "))
	num.append(ip_num)
print(num)

num = sorted(num)
print(f"Sorted array {num}")
num.reverse()
print("Reverse sort array {0} ".format(num))