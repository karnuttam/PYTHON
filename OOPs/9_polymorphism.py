#Polymorphism: Operator Overloading
#When the same operator is allowed to have different meaning according to the context.
#Operators and Dunder Functions

print(1+2);#Addition
print(type(1));
print("Uttam" + "Singh");#Concatenation
print(type("Uttam"));
print([1, 2, 3] + [4, 5, 6]);#Merging
print(type([1, 2,3]))

class Complex:
    def __init__(self, real, imag):
        self.real = real;
        self.imag = imag;
    def showNumber(self):
        print(self.real,"+ i",self.imag);

   # def add(self, obj2):
    def __add__(self, obj2): #After using dunder function
        newReal = self.real + obj2.real;
        newImag = self.imag + obj2.imag;
        return Complex(newReal, newImag);

    def __sub__(self, obj2): #After using dunder function
        newReal = self.real - obj2.real;
        newImag = self.imag - obj2.imag;
        return Complex(newReal, newImag);

C1 = Complex(5, 6);
C1.showNumber();
C2 = Complex(6, 9);
C2.showNumber();

C3 = C1 +C2;#After using dunder function (we can direct add)
C3.showNumber();
C4 = C1 - C2;
C4.showNumber();
#result = C1.add(C2);
#result.showNumber();