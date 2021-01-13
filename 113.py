import csv

rec = int(input("Enter how many records you want: "))

file = open("Books.csv","a")

for i in range(0,rec):
	author = input("Enter author name: ")
	book = input("Enter book name: ")
	year = input("Enter year: ")

	newrec = book+','+author+','+str(year)
	file.write(newrec+"\n")
file.close()


searchauth = input("Enter author name to search: ")

file = open("Books.csv","r")
count = 0
for row in file:
	if searchauth in str(row):
		print(row)
		count+=1

if count == 0:
	print("No books for this author")

file.close()