import random

usr = input("Enter h/t for head or tails: ")


res = random.choice(['h','t'])

if res == usr:
	print("You win")

else:
	print("Bad luck")

print(f"Computer selected {res} side")
