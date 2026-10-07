class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)

student1 = Student("Dalton", 21)

student1.introduce()