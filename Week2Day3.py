class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
print("Person 1:")
print("Name:", person1.name)
print("Age:", person1.age)
print("\nPerson 2:")
print("Name:", person2.name)
print("Age:", person2.age)

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
student1 = Student("John", 20, "Computer Science")
student2 = Student("Emma", 21, "Business")
print("\nStudent Profiles")
print("\nStudent 1")
print("Name:", student1.name)
print("Age:", student1.age)
print("Major:", student1.major)
print("\nStudent 2")
print("Name:", student2.name)
print("Age:", student2.age)
print("Major:", student2.major)