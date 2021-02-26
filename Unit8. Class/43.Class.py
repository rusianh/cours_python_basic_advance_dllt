class Student:
    def __init__(self):
        self.name = None
        self.age = None
        self.math_score = None
        self.literature_score = None

    def average_score(self):
        ave_score = (self.math_score + self.literature_score)/2
        return ave_score

s1 = Student()
s1.math_score = 7
s1.literature_score = 4

s2 = Student()
s2.math_score = 6
s2.literature_score = 5


print(s1.average_score())
print(s2.average_score())