#lists in Python
#A built-in data type that stores set of values
#It can store elements of different types (integer, float, string, etc.)
marks1  = 95.36;
marks2 = 87.36;
marks3 = 96.25;
marks4 = 66.24;
marks = 48.25;
marks = [96.36, 56.25, 48.63, 25.63];
print(marks);
print(type(marks));
print(marks[0])
print(marks[1])

student=["Karan", 96.25, 17, "Delhi"];
print(student);

#Strings are immutable in python and lists are mutable in python;
student[0]= "Uttam";
print(student);

#list slicing
#list_name[starting_index: ending_index] #ending_index is not included
print(marks[1: 4]);

#list methods
list = [2, 1, 3];
print(list);
list.append(4);# adds one element at the end;
print(list);
list.sort(); #Sorts in ascending order;
print(list);
list.sort(reverse = True); #sorts in descending order;
print(list);
list.reverse()#reverses list
print(list);
list.insert(2, 56);
print(list);
list.remove(56);
print(list);
list.pop(2);
print(list);
