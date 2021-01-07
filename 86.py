pswd = input("Enter password: ")
conf_pswd = input("Enter password: ")

if pswd == conf_pswd:
	print("Thank you")

elif pswd.lower() == conf_pswd.lower():
	print("Both password should be in same case")

else:
	print("Incorrect")