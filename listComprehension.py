l = [1,2,3,4,5,6,7,8,9]
L = [i * 2 for i in l]
print(L)

L2 = [i**2 for i in range(9)]
print(L2)

L3 = [i**2 for i in range(9) if i%2!=0]
print(L3)

fruits = ["apple", "banana", "mango", "orange", "grape", "pineapple", "kiwi"]
l1 = [fruit for fruit in fruits if 'o' in fruit]
print(l1)

D = {
    "name": "Safty",
    "gender": "Male",
    "age": 22
}

print(D.items())
#{key_expression: value_expression for item in iterable if condition}

D1 = {key:value for key,value in D.items() if len(key) > 3}
print(D1)

l2 = {item:item**2 for item in l if item%2 ==0}
print(l2)