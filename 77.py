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
		one_name = input("Enter any name: ")

		if one_name in nm_list:
			print("Position of searched name in list is: ",nm_list.index(one_name))
			invite = input("Do you want to invite this person.")
			if invite == "yes":
				print("All invited")

			else:
				nm_list.remove(one_name)
				print(nm_list)
		else:
			print("Name not found")

		exit()