fname = input("Enter first name: ")

if len(fname)<5:
	lname = input("Enter last name: ")
	full_name = fname+""+lname
	print(full_name.upper())


else:
	print(fname.lower())