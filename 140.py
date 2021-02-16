import sqlite3

def viewphonebook():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

def addtophonebook():
    newid = int(input("Enter ID: "))
    newfname = input("Enter first name: ")
    newsname = input("Enter surname: ")
    newpnum = input("ENter phone number: ")
    cursor.execute(""" INSERT INTO Names (id,firstname,surname,phonenumber) VALUES (?,?,?,?) """,(newid,newfname,newsname,newpnum))
    db.commit()


def selectname():
    selectsurname = input("Enter surname: ")
    cursor.execute("SELECT * FROM Names WHERE surname = ?",[selectsurname])
    for x in cursor.fetchall():
        print(x)

def deletedata():
    selecid = int(input("Enter id: "))
    cursor.execute("DELETE FROM Names WHERE id = ?",[selecid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()


with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()


def main():
    again = "y"

    while again == 'y':
        print()
        print("Main Menu")
        print()
        print("1) View phone book")
        print("2) Add to phone book")
        print("3) Search for surname")
        print("4) Delete person from phonebook")
        print("5) Quit")
        print()
        selection = int(input("Enter your selection: "))
        print()

        if selection == 1:
            viewphonebook()
        elif selection == 2:
            addtophonebook()
        elif selection == 3:
            selectname()
        elif selection == 4:
            deletedata()
        elif selection == 5:
            again = 'n'
        else:
            print("Incorrect option")

main()
db.close()