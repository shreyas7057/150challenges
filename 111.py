import csv

file = open("Books.csv","w")
add = "To Kill the mocking bird,Harper Lee,1960\n"
file.write(str(add))

add = "A Brief History of Time,Stephen Hawking,1988\n"
file.write(str(add))

add = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(add))

add = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(add))

add = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(add))

file.close()