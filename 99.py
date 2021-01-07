l = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

print(l)

row = int(input("Which row you want to display: "))
print(l[row])

col = int(input("Enter which col you want to display: "))
print(l[row][col])

c = input("DO you want ot change the value: ")

if c == 'y' or c == 'Y':
	num = int(input("Enter new num to change: "))
	l[row][col] = num
	print(l[row])
else:
	print(l[row])