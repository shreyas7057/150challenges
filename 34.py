print("1) Square")
print("2) Triangle")

choice = int(input("Enter choice 1 or 2: "))

if choice == 1:
	side = int(input("Enter side of square: "))
	area = side**2
	print("Area is {}".format(area))

elif choice == 2:
	height = int(input("Enter height of triangle: "))
	base = int(input("Enter base of triangle: "))
	area = (base*height)/2
	print(f"The area of triangle is {area}")

else:
	print("Wrong choice")