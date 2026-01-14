#Methods are functions that belong to objects.
#Functions used in class known as methods

class Student:
    college = "IIITM";
    def __init__(self, name, marks, semester):
        self.name = name;
        self.marks = marks;
        self.semester = semester;
    def hello(self):#methods
        print("I am learning Python...");

    def get(self):
        print(self.marks);
    @staticmethod
    def python():
        print("Hello,world");

s1 = Student("Karan", 99, "Fourth");
print(s1.name, s1.marks, s1.semester);
s1.hello();
s1.get();
s1.python();

#Static Method
'''
Methods that don't use the self parameter (work at class level)

class Student:
@staticmethod #decorator
def college():
    print("ABC College");

    
Decorator: Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it..
'''