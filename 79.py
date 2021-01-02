nums = []
cnt = 0

while cnt<3:
	num = int(input("Enter number: "))
	nums.append(num)
	print(nums)
	cnt+=1
keep_num = input("DO you want to keep last number(yes/no): ")
if keep_num == "yes":
	print(nums)
else:
	nums.remove(num)
	print(nums)