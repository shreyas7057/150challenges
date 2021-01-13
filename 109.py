print("1) Create new file")
print("2) Display the file")
print("3) Add new item to file")
print("Select any option from above 1/2/3")

ch = int(input("Select option: "))

if ch == 1:
	with open("Subject.txt","w") as fp:
		sub = input("Enter subject: ")
		fp.write(sub+"\n")
		fp.close()

elif ch == 2:
	with open("Subject.txt","r") as fp:
		print(fp.read())
		fp.close()

elif ch == 3:
	with open("Subject.txt","a") as fp:
		sub = input("Enter subject: ")
		fp.write(sub)
		fp.close()

	with open("Subject.txt","r") as fp:
		print(fp.read())
		fp.close()

else:
	print("Wrong Option")
