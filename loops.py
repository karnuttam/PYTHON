#Loops are used to repeat instructions
#while loops
#num = int(input("Enter the value: "));
num = 0;#known as iterator which helps in iteration
while(num <= 10 ):
    num = num+1;
    print(num);

print("The updated value of num: ");
print(num);

n = int(input("Enter the value of n: "));
i = 1;
while i <= 10:
   print(n*i);
   i = i+1;
#Traversing the list
list_1 = [1, 4,9, 16,25, 36, 49, 64, 81, 100];
print(list_1[0]);
i = 0;
while i <= len(list_1)-1:
    print( list_1[i]);
    i = i+1;


tuple =(0, 1, 2, 3, 4);
print(tuple);
'''
x = int(input("Enter the value provided in tuple: "));
idx = 0;
while idx <= len(tuple)-1:
    if(x == tuple[idx]):
        print("Found at index: ",idx);
   
    break;
       
else:
    print("No, matching");
    idx = idx + 1; 
   ''' 


   