#Inheritance: When one class(child/derived) derives the properties and methods of another class(parent/base).
class Car:
    @staticmethod
    def start():
        print("The car has started...");
    @staticmethod
    def stop():
        print("The car has stopped...");
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand;


class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type;
#C1 = ToyotaCar("mercedes");
C1 = Fortuner("Diesel");
print(C1.type);
C1.start();
C1.stop();
#Three types of inheritance
#Single inheritance
#Multi-level inheritance
#Multiple inheritance


#multiple inheritance
class A:
    varA = "Welcome to class A";
class B:
    varB = "Welcome to class B";
class C(A, B):
    varC = "Welcome to class C";
C1 = C();
print(C1.varC);
print(C1.varA);
print(C1.varB);