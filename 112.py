import csv


file = open("Books.csv","a")

author = input("Enter name of author: ")
book = input("Enter name of book: ")
year = int(input("Enter year of book: "))

add = book+","+author+","+str(year)

file.write(add+"\n")
file.close()
