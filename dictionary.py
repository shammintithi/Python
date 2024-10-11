#1. Dictionary
dict = {
    "Key" : "value",
    "name" : "tithi",
    "age" : 30,
    "info" : ("tithi", 21, "SEU"),
    "is_valid" : True,
}

print(dict)
print(dict["age"]) #for diffferent values
print(dict["is_valid"])

#another

dict["name"] = "Shammin"
dict["surname"] = "Akter"
print(dict["name"])
#print(dict)

#2. Null dictionary
null_dict = {}

#Also we can add some values in null dictionary

null_dict["name"] = "Shammin"
print(null_dict)
