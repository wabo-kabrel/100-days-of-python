my_dict = {
    "name": "Lamar",
    "age": 20,
    "grade": 'A',
    "language": "Python"
}

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f"{key} -> {value}")