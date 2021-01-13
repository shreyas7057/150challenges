with open("Names.txt","a") as fp:
	name = input("Enter name: ")
	fp.write("\n"+name)
	fp.close()

with open("Names.txt","r") as fp:
	print(fp.read())
	fp.close()