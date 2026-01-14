#We use @property decorator on any method in the class to ust the method as a property.

class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy;
        self.chem = chem;
        self.maths = maths;

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths) / 3) + "%";

S1 = Student(89, 99, 97);
print(S1.percentage);
        