#Conditional Statements
#if-elif-else (SYNTAX)

age = int(input("Enter the valid age: "));
if(age >= 18 and age <= 100):
    print("Can vote and apply for driving license.");
else:
    print("You are not eligible.");

light = input("Enter the traffic light: ");
print("Red, Green, Yellow");

if(light == "Red"):
    print("Stop");
elif(light == "Yellow"):
    print("Look");
elif(light == "Green"):
    print("go");
else:
    print("Enter the valid light.");

#giving proper spacing known as indentation
# nesting  
if(age <= 18):
    if(age >= 60):
        print("Cannot drive.");
    else:
        print("drive");
else:
    print("Cannot Drive...");