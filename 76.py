nm1 = input("Enter name: ")
nm2 = input("Enter name: ")
nm3 = input("Enter name: ")

nm_list = [nm1,nm2,nm3]
print(nm_list)

out = True

while out == True:

	add = input("Do you want to add more names: ")

	if add == "yes":
		nm = input("Enter name: ")
		nm_list.append(nm)

	else:
		print(f"You invited {nm_list} for party and its count is {len(nm_list)}.")
		exit()