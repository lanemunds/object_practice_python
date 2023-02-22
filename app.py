class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student('Lane', 33, 95)
s2 = Student('Tim', 22, 75)
s3 = Student('Bill', 30, 90)

course = Course('science', 2)
course.add_student(s1)
course.add_student(s2)

print(Course.get_average_grade(course))


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print('I dont know what to say')


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(
            f'I am {self.name} and I am {self.age} years old I am {self.color}')


class Dog(Pet):
    def speak(self):
        print('Bark')


c = Cat('carl', 12, 'Brown')
c.show()


class Person:
    number_of_people = 0
    gravity = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person('Lane')
p2 = Person('Tim')

print(Person.number_of_people_())


class Math:
    @staticmethod
    def add5(x):
        return x + 5


print(Math.add5(5))
