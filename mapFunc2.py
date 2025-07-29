students = [
    {
        "name": "Ayaan Khan",
        "father's name": "Rahim Khan",
        "address": "Dhaka, Bangladesh"
    },
    {
        "name": "Meherun Nisa",
        "father's name": "Jalal Uddin",
        "address": "Chittagong, Bangladesh"
    },
    {
        "name": "Shovon Das",
        "father's name": "Bikash Das",
        "address": "Khulna, Bangladesh"
    }
]

print(list(map(lambda student:student['name'],students))) #can use i instead of student

print(list(map(lambda i:i["father's name"],students)))