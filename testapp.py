#simple test file for python
from Student import Student

print("Start of the program\n\n")
student1 = Student("joe mamboi", 3.0, 24, False)

print("-\t---\t---\t-")
print("Name: \t\t", student1.name)
print("AGE: \t\t", student1.age)
print("GPA: \t\t", student1.gpa)
print("On_Probation: \t", student1.is_on_probation)
print("-\t-\t-\t-")
