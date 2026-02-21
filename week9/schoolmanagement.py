class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduction(self):
        return f"Hello, I am {self.name}, and I am {self.age} years old"

class student(person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduction(self):
        return f"Hello, I am a student called {self.name}, my student id is {self.student_id} and I am {self.age} years old"

class teacher(person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduction(self):
        return f"Hello, I am a teacher called {self.name}, I teach {self.subject} and I am {self.age} years old"

alice = person('alice', 23)
bob = student('bob', 19, 1)
joe = teacher('joe', 32, 'history')

print("=== School Management System ===")
print(bob.introduction())
print(joe.introduction())
print(f"\nStudent age: {bob.age}")
print(f"Teacher subject: {joe.subject}")