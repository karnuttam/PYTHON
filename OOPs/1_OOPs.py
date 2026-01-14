#OOP in Python
'''
To map with real world scenarios, we started using objects in code.
This is called Object Oriented Programming.
Class: Class is a blueprint for creating objects.

'''

class Student:
    name="Uttam Singh"
    age = 20
    semester= "Fourth"

s1 = Student();
#print(s1);
print(s1.name);
print(s1.semester);
print(s1.age);

class Car:
    color ="Blue"
    brand = "mercedes"
car1 = Car();
print(car1.color);
print(car1.brand);

#Constructor: All classes have a function called _init_(), which is always executed when the class is being initiated.

'''
Creating class
class Student:
      def __init__(self, fullname):
      self.name = fullname

Creating Object
s1 = Student("Karan")
print(s1.name)

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
'''

class Student:
    college_name = "Indian Institute of Information Technology..."
    name = "Anonymous"; #Class Attribute
    def __init__(self, fullname, marks):#Parameterized Constructor
        self.name = fullname; #Object Attribute > class Attribute
        self.marks = marks;
        print(self)
        print("Adding new student in Database..");
s1 = Student("Karan", 56);
print(s1.name, s1.marks);
s2 = Student('Arjun', 99);
print(s2.name, s2.marks);
print(s2.college_name);