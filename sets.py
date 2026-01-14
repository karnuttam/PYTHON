#Set in Python
'''
Set is the collection of the unordered items.
Each element in the set must be unique and immutable.
Sets are mutable.
'''

collection={1,2,2,2,3,6, "Hello", "World", 4,5};
print(collection);
print(type(collection));
print(len(collection));

print("This is a empty set");
null_set = set();
print(null_set);

#set methods
null_set.add(1);
print(null_set);
null_set.add(2);
print(null_set);
null_set.add(3);
print(null_set);
#In sets all values are immutable(hashable)
new_set = collection.union(null_set);
print(new_set);
new_set_2 = collection.intersection(null_set);
print(new_set_2);

classroom = {"python", "java", "C++", "python", "javascript", "dart", "C", "javascript", "C++", "PHP"};
print(classroom);
print("Total classroom needed: ",len(classroom));

values = {
    ("float",9.0),
    ("int", 9)
}
print(values);