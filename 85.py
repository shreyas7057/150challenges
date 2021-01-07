name = input("Enter your name: ")
vowels = 0

ls = ['a','e','i','o','u']

for i in ls:
	if i in name:
		vowels+=1
print(vowels)