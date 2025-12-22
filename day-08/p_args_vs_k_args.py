# Positional Arguments

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What's the weather like in {location}")

greet_with("Kay", "Buea")

# Keyword Arguments

def greet_again(name, location):
    print(f"Hello {name}")
    print(f"What's the weather like in {location}")

greet_with(name = "Lamar", location = "Yaounde")