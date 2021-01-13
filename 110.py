with open("Names.txt",'r') as fp:
	print(fp.read())
	fp.close()

with open("Names.txt","r") as fp:
	name = input("Enter name: ")
	name = name +'\n'

	for row in fp:
		if row !=name:
			with open("Names2.txt",'a') as fp:
				newname = row
				fp.write(newname)
				fp.close()

fp.close()