l = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

print(l)

row = int(input("Which row you want to display: "))
print(l[row])

num = int(input("Enter number to add to list: "))

l[row].append(num)
print(l[row])