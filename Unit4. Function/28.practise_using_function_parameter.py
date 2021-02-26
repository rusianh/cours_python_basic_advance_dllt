def main():
    student_A_name = "Dung" #local variable
    student_A_math_score = 9
    student_A_literature_score = 7
    
    student_B_name = "Nguyen"
    student_B_math_score = 5
    student_B_literature_score = 8

    level_A_toan = "basic"
    print_student(student_A_name, student_A_math_score, student_A_literature_score)
    print_student(student_B_name, student_B_math_score, student_B_literature_score)

def print_student (name, math_score, literature_score):
    print("student name: "+ name)
    print("toan: "+ str(math_score))
    print("van: "+ str(literature_score))

main()