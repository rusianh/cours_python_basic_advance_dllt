def ask_yes_no(promt):
    answer = input(promt)
    # using while loop to make sure users type in yes or no, wrong answers will be prompted to enter again
    while True:
        answer = input("Are you male (yes/no): ")
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            continue

def calculate_age(year_born, current_years):
    return current_years - year_born

def main():
    # constant variable (unchanged variable), written in all capital letter, this is the naming convention of constant variable
    CURRENT_YEAR = 2021
    METER_TO_FEET = 3.281

    # ask for details from users
    firstname = input("Your firstname: ")
    lastname = input("Your lastname: ")
    year_born = input("When you were born: ")
    height_meter = input("Your height (meter): ")
    is_male = ask_yes_no("Are you male (yes/no): ")

    # convert year_born from string to integer then calculate age by comparing the year the user was born and the current year
    year_born = int(year_born)
    age = CURRENT_YEAR - year_born(year_born, CURRENT_YEAR)

    # convert height from string to float then convert it from meter to feet and take 2 digits in the decimal place
    height_meter = float(height_meter)
    height_feet = height_meter * METER_TO_FEET
    height_feet = round(height_feet,1)

    # print the information of the user after processing using string format, \n is the newline character
    print("\n---")
    print("Your name is " + firstname + " " + lastname)
    print("{2} is {0} years old in {1}".format(age,CURRENT_YEAR,firstname))
    print("You are " + str(height_feet) + " feet tall")


    # check height of the user based on their gender
    if is_male == True:
        if height_feet > 6.5:
            print("You are", end=" ")

            # print "very" 10 times using for
            for i in range(10):
                print("very", end=" ")

            print("tall as a man")
        elif height_feet > 6.0:
            print("You are tall as a man")
        else:
            print("You are short as a man")
    else:
        if height_feet > 5.7:
            print("You are tall as a girl")
        elif height_feet < 5.0:
            print("You are", end=" ")

            # print "very" 10 times using while
            i=0
            while i<10:
                print("very ", end = "")
                i+=1

            print("short as a girl")
        else:
            print("You are short as a girl")

main()