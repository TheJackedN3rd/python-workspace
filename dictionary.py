#dictionary
#dictionary has no indexing, but it has keys and values
#dicitonary is mutable, it can be changed
#keys must be immutable, but values can be mutable
#dictionary can have mixed data types for keys and values
#dictionary can have duplicate values, but keys must be unique
#dictionary is unordered, it does not maintain the order of elements

#mutable data types: list, set, dictionary
#immutable data types: int, float, str, tuple, frozenset




D = {}
D = {    "name": "John",
     "age": 30,}
print(D)  # {'name': 'John', 'age': 30}

D1 = {(1, 2): "tuple_key", "name": "Alice"}
print(D1)  # {(1, 2): 'tuple_key', 'name': 'Alice'}

D3 = {"name" : "Safty", "name" : "Bob"}  # duplicate keys, the last one will be kept
print(D3)  # {'name': 'Bob'}

D4 = {"name" : "Safty", "Name" : "Bob"}
print(D4)  # {'name': 'Safty', 'Name': 'Bob'}  # keys are case-sensitive


D2 = {"name": "Bob", "age": 25, "city": "New York"}

D5 = {"name": "Alice", "age": 30, "city": "Los Angeles", "hobbies": ["reading", "traveling"], "Marks": {"math": 90, "science": 85}}
print(D5)  # {'name': 'Alice', 'age': 30, 'city': 'Los Angeles', 'hobbies': ['reading', 'traveling'], 'Marks': {'math': 90, 'science': 85}}

print(D5['name'])

D5['age'] = 31  # modify the value of a key
print(D5)  # {'name': 'Alice', 'age': 31, 'city': 'Los Angeles', 'hobbies': ['reading', 'traveling'], 'Marks': {'math': 90, 'science': 85}}

D5["Marks"]["math"] = 95  # modify a nested value
print(D5)  # {'name': 'Alice', 'age': 31, 'city': 'Los Angeles', 'hobbies': ['reading', 'traveling'], 'Marks': {'math': 95, 'science': 85}}
D5["hobbies"].append("cooking")  # add a new hobby
print(D5)  # {'name': 'Alice', 'age': 31, 'city': 'Los Angeles', 'hobbies': ['reading', 'traveling', 'cooking'], 'Marks': {'math': 95, 'science': 85}}

D.get("name")  # get the value of a key
print(D.get("name"))  # Alice

D5['Gender'] = 'Male'  # add a new key-value pair
print(D5)  # {'name': 'Alice', 'age': 31, 'city': 'Los Angeles', 'hobbies': ['reading', 'traveling', 'cooking'], 'Marks': {'math': 95, 'science

D5["Marks"]["history"] = 88  # add a new subject to Marks
print(D5)  # {'name': 'Alice', 'age': 31, ' city': 'Los Angeles', 'hobbies': ['reading', 'traveling', 'cooking'], 'Marks': {'math': 95, 'science': 85, 'history': 88}}}

del D

del D2["age"]  # delete a key-value pair
print(D2)  # {'name': 'Bob', 'city': 'New York'}

D2.clear()  # clear the dictionary
print(D2)  # {}

D5.pop("city")  # remove a key-value pair and return the value
print(D5)  # {'name': 'Alice', 'age': 31, 'hobbies': ['reading', 'traveling', 'cooking'], 'Marks': {'math': 95, 'science': 85, 'history': 88},

for i in D5:
    print(i)  # iterate over keys
    
for i in D5:
    print(i,D5[i])  # iterate over values
    
'Alice' in D5  # check if a key exists
print('Alice' in D5)  # False, 'Alice' is a value, not a key
print('name' in D5)  # True, 'name' is a key

print(len(D5))  # length of the dictionary
print(D5.keys())  # get all keys   
print(D5.values())  # get all values
print(D5.items())  # get all key-value pairs
print(min(D5))  # get the minimum key (alphabetically)
print(max(D5))  # get the maximum key (alphabetically)
sorted(D5)  # sort the keys of the dictionary
print(sorted(D5))  # ['age', 'hobbies', 'Marks', 'name']
