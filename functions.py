#Functions in Python
#Block of statements that perform a specific task.
#def func_name(param1, param2..): function definition
#some work
#return value

#func_name(arg1, arg2..) Function call

def sum(a, b):
    s = a + b;
    return s;
print(sum(45, 63));
result = sum(78, 69);
print(result);

def hello():
    print("Hello, Python");

hello();
hello();
hello();
hello();
hello();

#functions type
#1. Built in function 2. User defined function
print("Uttam Singh,", end=" ");
print("A good learner.");

#Default parameters: Assigning a default value to parameter, which is used when no argument is passed.

def calc_product(a = 1, b = 5):# default parameter
    print(a * b);
    return a*b;

calc_product();

cities =["Delhi", "Patna", "Imphal", "Kolkata", "Guwahati", "Bengaluru"];
heroes =["Ironman", "Superman", "Krish","Captain America", "Thor", "Loky"];

def print_len(list):
    print(len(list));

print_len(cities);

def print_heroes(list):
    for item in list:
        print(item, end=" ");

print_heroes(heroes);

def find_fact(n):
    fact = 1;
    i = 1;
    while i <= n:
        fact = fact*i;
        i = i + 1;
    return fact;

result_fact = find_fact(6);
print("\nThe factorial of given number is", result_fact);