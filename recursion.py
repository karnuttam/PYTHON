#Recursion: When a function calls itself repeatedly.
def show(n):
     if(n == 0):#This is the base condition where program (recursion) will be terminated
        return #this is control return
     print(n);
     show(n-1);
     print("End!");

show(5);

def factorial(n):
    if(n == 0 or n == 1):
        return 1;
    else:
        n = n*factorial(n - 1);
        return n;

num = int(input("Enter the number to find the factorial: "));
fact_result = factorial(num);
print("The factorial of the given number: ", fact_result);
