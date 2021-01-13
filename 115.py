import csv

file = open("Books.csv","r")
x = 0

for row in file:
	disp = "Row: "+str(x)+"-"+row
	print(disp)
	x+=1