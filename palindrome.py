def palin(text):
    if len(text) <= 1:
        return "palindrome"
    else:
        if text[0] == text[-1]:
            return palin(text[1:-1])
        else:
            return "not a palindrome"
            

print(palin("madam"))
print(palin("malayalam"))
print(palin("python"))

print(palin("018181"))

print(palin("abba"))



