class Person:
    def __init__(self, std):
        self.std = std
        self.__pre = 0
        self.__mid = 0
        self.__fin = 0


class Student(Person):
    def preGrade(self, classStanding, exam):
        self.__pre = (classStanding * 0.6) + (exam * 0.4)
        return self

    def midGrade(self, classStanding, exam):
        self.__mid = (classStanding * 0.6) + (exam * 0.4)
        return self

    def finGrade(self, classStanding, exam):
        self.__fin = (classStanding * 0.6) + (exam * 0.4)
        return self

    def display(self):
        print(f'Name: {self.std}\n'
              f'Prelim Grade: {round(self.__pre, 2)}\n'
              f'Midterm Grade: {round(self.__mid, 2)}\n'
              f'Finals Grade: {round(self.__fin, 2)}\n')
        return self


std1 = Student("Jeremiah Harland").preGrade(69, 80).midGrade(57, 81).finGrade(79, 69).display()
std2 = Student("Naomi Ethel").preGrade(52, 64).midGrade(97, 53).finGrade(62, 65).display()
std3 = Student("Vivienne Audrey").preGrade(88, 78).midGrade(85, 73).finGrade(70, 85).display()