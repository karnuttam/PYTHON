#Abstraction: Hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.clutch = False;
        self.accelator = False;
        self.brk = True;
    def start(self):
        self.clutch = True;
        self.accelator = True;
        self.brk = False;
        print("The car has started...");

C1 = Car();
C1.start();

#Encapsulation: Wrapping data and functions into a single unit (object).

         