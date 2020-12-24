n = int(input("Enter the number: "))
total = n
again = "y"

while again == "y":
	n2 = int(input("Enter another number: "))
	total = total + n2
	again = input("Do you want to add another number: ")
print(f"The total is {total}")