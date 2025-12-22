age = int(input("Enter your age: "))

def life_left(age):
    max_age = 90
    years_left = 90 - age
    weeks_left = years_left * 54
    print(f"You have {weeks_left} weeks left")
    
life_left(age)

