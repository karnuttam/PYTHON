#loops are used for sequential traversal. For traversing list, string, tuples etc.
list_1 = [4, 5,36,96];
for value in list_1:
    print(value);

#for loop with else(optional)
for num in list_1:
    print(num);
else:
    print("END");

str_1= "Uttam Singh";
for char in str_1:
    print(char);
else:
    print("End");

for ch in str_1:
    if(ch == "U"):
        print("U found");
        break;
    print(ch);
else:
    print("END");

list_2 = [45, 25,89, 14,25,36, 78, 25];
x = 25;
idx = 0;
for el in list_2:
    if(el == x):
        print("Number found at index: ", idx);
    idx = idx + 1;
    
