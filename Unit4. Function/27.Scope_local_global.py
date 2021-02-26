def main():
    student_A_name = "Dung" #local variable
    student_B_name = "Nguyen"
    level_A_toan = "basic"
    print_student_A(student_A_name, level_A_toan)
    print_student_B(student_B_name)

def print_student_A(name, level):
    print("Student A:" + name)
    print("Toan: 9 " + level)
    print("Van: 6")

def print_student_B(name):
    print("Student B: "+ name)
    print("Toan: 5")
    print("van: 7")


main()