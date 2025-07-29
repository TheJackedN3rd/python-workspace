#map works for all items
#filter for only specific items

l = [1,2,3,4,5,6,7,8]
print(list(filter(lambda x:x>4,l)))

fruits = ["apple", "banana", "mango", "orange", "grape", "pineapple", "kiwi"]
print(list(filter(lambda fruit:'e' in fruit,fruits)))
