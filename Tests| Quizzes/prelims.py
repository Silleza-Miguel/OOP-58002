class Student:
    def __init__(self, name, student_no, age, school, course):
        self.name = name
        self.student_no = student_no
        self.age = age
        self.school = school
        self.course = course

    def self(self):
        print("\nName        : " + self.name +
              "\nStudent No. : " + self.student_no +
              "\nAge         : " + self.age +
              "\nSchool      : " + self.school +
              "\nCourse      : " + self.course)

print("Example:")
myself = Student("Miguel Silleza", "202116376", "19", "Adamson", "Computer Engineering")
myself.self()

while True:
    id = []
    attributes = ["Name", "Student No.", "Age", "School", "Course"]

    print("\nWhat about you?\n")

    for i in range(len(attributes)):
        value = str(input(attributes[i] + "? ")).title()
        id.append(value)

    myself = Student(id[0], id[1], id[2], id[3], id[4])
    myself.self()

    while True:
        accept = ["y", "n"]

        ans = input("\nAgain [y/n]? ").lower()

        if any(value in ans for value in accept):
            break

    if ans == "n":
        break

print("Bye!")
