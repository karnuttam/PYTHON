'''
Class Method: A class method is bound to the class and receives the class as an implicit first argument.
Note - static method can't access or modify class state and generally for utility.
'''
class Person:
    name = "Anonymous";

    @classmethod
    def changeName(cls, name):
        cls.name = name;

P1= Person();
print(P1.name);
P1.changeName("Rahul Kumar");
print(Person.name);