CURRENT_YEAR = 2021
Meter_to_feet = 3.281

print("Your firstname: ")
firstname = input()

print("Your lastname: ")
lastname = input()

print("Your name is " + firstname + " " + lastname)

print("When you were born: ")
year_born = input()
year_born = int(year_born)

age = CURRENT_YEAR - year_born

print("You are " + str(age) + " years old in " + str(CURRENT_YEAR))
print("You are {0} years old in {1}".format(age,CURRENT_YEAR))

print("your height (meter): ")
height_meter = input()
height_feet = float(height_meter) * Meter_to_feet

height_feet = round(height_feet,1)

print("You are "+ str(height_feet) + "feet tall")