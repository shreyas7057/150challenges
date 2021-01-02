food_dictionary = {}

food1 = input("ENter food: ")
food_dictionary[1] = food1

food2 = input("ENter food: ")
food_dictionary[2] = food2

food3 = input("ENter food: ")
food_dictionary[3] = food3

food4 = input("ENter food: ")
food_dictionary[4] = food4

print(food_dictionary)
rem = int(input("Enter food you want to remove"))
del food_dictionary[rem]
print(food_dictionary.values())

