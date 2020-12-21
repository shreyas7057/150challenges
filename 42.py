total = 0

for i in range(0,5):
    num = int(input("Enter number: "))
    ans = input("Want to add this num: ")
    if ans == "y":
        total = total + num

print(total)
    