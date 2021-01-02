sub = ['maths','eng','sci','ss','pd','history']

usr_ip = input("Enter subject which you dont like: ")
subid = sub.index(usr_ip)
del sub[subid]
print(sub)