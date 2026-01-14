#Dictionary in Python
#Dictionary are used to store data values in key:value pairs.
#They are unordered, mutable(changeable) & don't allow duplicate keys
dict = {
    "name": "Uttam Singh",
    "Age": 20,
    "marks": [99, 98, 100, 97],
}
print(dict);
info ={
    "key": "value",
    "learning": "python",
    "marks": 96.99,
    "subject":["Python", "C", "C++"],#list
    "topics":("dictionary", "set"),#tuple
    "is_adult": True
}
print(info);
print(type(info));
print(info["topics"]);
print(info["marks"]);
print(info["learning"]);
info["name"]="Uttam";
info["surname"]="Singh";
print(info);

null_dict = {}#Empty dictionary
print(null_dict);
null_dict["name"] = "Apna College";
print(null_dict);

result={
    "name": "Uttam",
    "subject":{
        "Physics": 99.36,
        "Chemistry": 98.26,
        "Biology": 96.25,
    },
    "status":"Pass"
}
print(result);
print(result["subject"]);
print(result["subject"]["Chemistry"]);

#Dictionary methods
print(result.keys());
print(len(result));
print(result.values())
print(result.items())
print(list(result.items()))
print(result["name"]);
#print(result["name2"]);#It will give error
print(result.get("name"));
print(result.get("name2"));#It will not give error
result.update({"city":"Delhi"});
print(list(result.keys()));#typecasting
new_dict ={"fruits": "Apple","Veg":"Cabbage"};
result.update(new_dict);
print(result);
print(result);
