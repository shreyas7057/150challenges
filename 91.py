from array import *

num = array('i',[1,1,3,3,5])
print(num)

enter_num = int(input("Enter any number from array: "))

print(f"The {enter_num} appeared for {num.count(enter_num)} times in array.")