#Punctuators: Punctuators are symbols to organize sentence structure in programming.
#(),{}, @, [], #, -=, +=, *= etc;
#Python is a implicit typed language.No need to declare type in python.
#C, C++ is a explicit typed language.We have to declare type before variable.int age = 23
#Expression Execution
#String and Numeric values can operate together with*
A, B = 2, 3;
Txt = "@";
print(2*Txt*3);#if any string multiplied with numeric value then it repeats
A, B = "2", 3;
Txt = "@";
print((A+Txt)*B);
#Concatenation
#Numeric values can operate with all arithmetic operators
#Arithmetic expression with integer and float will result in float
#Result of division operator with two integers will be float
#Integer division with float and int will give int displayed  as float(//);
A, B = 1.5, 3;
C = A//B; #integer division same result gives floor value
print(C, A/B);
#Result of (A//B) is same as floor(A/B);
#Reminder is negative when denominator is negative