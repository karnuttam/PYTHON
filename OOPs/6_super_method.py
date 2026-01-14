#Super Method: super() method is used to access methods of the parent class.
class Car:
    def __init__(self, type):
        self.type = type;
    @staticmethod
    def start():
        print("The car has started...");
    @staticmethod
    def stop():
        print("The car has stopped...");

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name;
        super().__init__(type);
        super().start();
        super().stop();

C1 = ToyotaCar("Prius","Electric");
print(C1.name);
print(C1.type)
