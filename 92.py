from array import *
import random

nums = array('i',[])

for i in range(0,3):
	num = int(input("Enter number: "))
	nums.append(num)
print(nums)


rand_num = array('i',[])

for i in range(0,5):
	num = random.randint(1,100)
	rand_num.append(num)
print(rand_num)

rand_num.extend(nums)

rand_num = sorted(rand_num)

for i in rand_num:
	print(i)
