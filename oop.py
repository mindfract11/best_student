students = []
class Student:
    def __init__(self, name , age, grade):
        self.name = name 
        self.age = age
        self.grade = grade
    def  info(self):
        print("Name: {} Age: {} Grade: {}".format(self.name, self.age, self.grade))
student1 = Student("Alex","22","60")
student2 = Student("Illia", "31", "90")
student3 = Student("Kiril", "28", "88")

students.append(student1)
students.append(student2)
students.append(student3)

for student in students:
    student.info()

best_student = max(students,key=lambda x: x.grade)

print("/nBest student")
best_student.info()