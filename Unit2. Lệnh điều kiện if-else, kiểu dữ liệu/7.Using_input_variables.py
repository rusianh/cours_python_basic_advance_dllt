curren_year = 2021

print("your first name: ")
first_name = input() #function #buil in function

print("you last name ")
lastname = input()

print("your name is " + first_name + '' + lastname)

print("when you were born: ")
year_born = input()
year_born = int(year_born) #over write

age = curren_year - year_born

print("You are "+ str(age) + ' ' + "year old")