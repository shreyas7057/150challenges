tv_programs = ['tmkoc','cid','yrkkh','ng']

for i in tv_programs:
	print(i)

new_program = input("Enter new program: ")
new_position = int(input("Enter position from 0 to 3: "))

tv_programs.insert(new_position,new_program)

for i in tv_programs:
	print(i)