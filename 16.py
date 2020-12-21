rain = input("Is it raining: ")

rain = rain.lower()

if rain == "yes":

	wind = input("Was it windy? ")
	wind = wind.lower()

	if wind == "yes":
		print("It is too windy for an umbrella")

	else:
		print("Take umbrella")

else:
	print("Enjoy your day")