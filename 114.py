import csv



start = int(input("Enter year to see books: "))
end = int(input("Enter year to see books: "))

file = list(csv.reader(open("Books.csv","r")))
tmp = []
for row in file:
	tmp.append(row)

x = 0
for row in tmp:
	if int(tmp[x][2]) >= start and int(tmp[x][2])<=end:
		print(tmp[x])
	x+=1