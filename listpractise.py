l = "how are you?"
print(l.split())  # Splitting the string into a list of words
L =[]
for i in l.split():
    print(i.capitalize())  # Printing each word in the list
    L.append(i.capitalize())  # Appending capitalized words to a new list
print("Capitalized List:", L)
print(" ".join(L))  # Joining the capitalized words into a single string

mail = "safty5@gmail.com"
print(mail[:mail.find('@')])  # Extracting the username from the email
    

l = [10, 20, 20, 30, 40, 40, 50]  # Initializing a list with integers
print("Original List:", l)

L = []

for i in l:  # Iterating through the list
    if i not in L:  # Checking for duplicates
        L.append(i)  # Appending unique elements to a new list
        print(i, end=' ')  # Printing each element in the list