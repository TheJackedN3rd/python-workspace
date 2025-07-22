#Array homogenous List Heterogeneous
#Arrays are much faster than lists
#Lists are more flexible than arrays
#Lists can contain different data types, arrays cannot

l = [1, 2, 3, 4, 5]  # List of integers
print("List:", l)

a = [1, 2.5, "Hello", True]  # List with mixed data types
print("List with mixed types:", a)

MultiDimensionalList = [[1, 2, 3], [4, 5, 6], [7, 8, 9],10,11]  # List of lists
print("Multi-dimensional List:", MultiDimensionalList)

threeDList = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]  # Three-dimensional list
print("Three-dimensional List:", threeDList)

l1 = list("Hello")  # Convert string to list of characters
print("List from string:", l1)

l2 = list()  # Empty list
print("Empty List:", l2)

print(l[0])  # Accessing first element of the list
print(l[1:3])  # Slicing the list to get elements from index 1 to 2
print(l[-1])  # Accessing the last element of the list
print(l[::-1])  # Slicing the list to get all elements

print(MultiDimensionalList[1][0])
print(MultiDimensionalList[1])

print(threeDList[1][1][0])  # Accessing an element in a three-dimensional list
print(threeDList[0][1])  # Accessing a sub-list in a

l[0] = 10  # Modifying the first element of the list list
print("Modified List:", l)

l[1:4] = [20, 30, 40]  # Modifying a slice of the list
print("Modified slice of List:", l)

l.append(60)  # Appending an element to the end of the list
print("List after appending:", l)

l.append("New Element")  # Appending a string to the list
print("List after appending a string:", l)

l.extend("Hello")  # Extending the list with a string
print("List after extending with a string:", l)

l.extend([70, 80])  # Extending the list with another list
print("List after extending:", l)

l.append([90, 100])  # Appending a list to the list
print("List after appending a list:", l)

l.insert(1,"world")  # Inserting an element at index 1
print("List after inserting an element:", l)

del a  # Deleting the list with mixed types
print("Deleted list with mixed types.")
#print(a)  # This will raise an error since 'a' is deleted

del l[1]  # Deleting the first element of the list
print("List after deleting the second element:", l)

del l[-1]  # Deleting the last element of the list
print("List after deleting the last element:", l)

del l[-7:-2]  # Deleting a slice of the list
print("List after deleting a slice:", l)

l.remove(10)  # Removing the first occurrence of 10 from the list
print("List after removing 10:", l)

l.pop()  # Removing the last element of the list
print("List after popping the last element:", l)

l1.clear()  # Clearing the list
print("List after clearing:", l1)

l7 = [1, 2, 3, 4, 5]
l8 = [6, 7, 8, 9, 10]

l9 = l7 + l8  # Concatenating two lists
print("Concatenated List:", l9)

l10 = l7 * 2  # Repeating the list
print("Repeated List:", l10)

for i in l7:  # Iterating through the list
    print(i, end=' ')
    
for i in l:
    print(i,end = ' ')

for i in threeDList:  # Iterating through a three-dimensional list
            print(i, end=' ')
            

print([1,2] in threeDList) # Checking if a sub-list exists in the three-dimensional list

len(l)  # Getting the length of the list
print("Length of the list:", len(l))

# Getting the minimum value in the list
print("Minimum value in the list:", min(l7))

print("Maximum value in the list:", max(l7))  # Getting the maximum value in the list

sorted_list = sorted(l7)  # Sorting the list
print("Sorted List:", sorted_list)

sorted(l7, reverse=True)  # Sorting the list in descending order
print("Sorted List in descending order:", sorted(l7, reverse=True))

l7.sort()  # Sorting the list in place
print("List after in-place sort:", l7)

l7.index(3)  # Getting the index of the first occurrence of 3
print("Index of 3 in the list:", l7.index(3))

