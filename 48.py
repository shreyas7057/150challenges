again = "y"
count = 0
while again == "y":
	name = input("Enter name to invite: ")
	print(f"{name} has been invited.")
	count+=1
	again = input("Do you want to invite any other..")
print(f"Total {count} number of people are coming for party")