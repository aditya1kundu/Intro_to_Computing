# creating class
class Student:
    pass
class Marks:
    pass
# instance
student1 = Student()
marks1 = Marks()
#Checking whether the instance or not.
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nChecking whether the said classes are subclasses of the built-in object class or not....")
print(issubclass(Student, object))
print(issubclass(Marks, object))
