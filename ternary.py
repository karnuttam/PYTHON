#Single line if / Ternary Operator
#<var> = <value1>if<condition>else<value2>

food = input("food: ");
result = "yes" if food=="cake" else "No";
print(result);

#<string1> if <condition> else <string2>
print("sweet") if food =="cake" or food == "apple" else print("fruit");

#clever if / Ternary Operator
#<var> = (false_value, true_value)[<condition>]

age = int(input("Age: "));
vote = ("Yes", "No")[age >= 18]
print(vote);

salary = float(input("Salary: "))
tax = salary*(0.1, 0.2) [salary <= 50000]
print(tax);

#Best practices
#Simple instructions
#One instruction per task
#Short and meaningful variable names
#Use appropriate comments
#Avoid complex expressions

#type conversion(automatically convert by python)

a = int("2");
b = 4.25;
print(type(a));
c = int(a);#type casting (manually)
print(c + b);

input("Enter your name: ");