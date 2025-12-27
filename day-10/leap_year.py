def is_leap_year(year):

    if (year % 4) == 0:
        if (year % 100) == 0:

            if (year % 400) == 0:
                return "a Leap Year."
            
            else:
                return "not a Leap Year."
    
        else:
            return "a Leap Year."
        
    else:
        return "not a Leap Year."
    
x = int(input("Enter a year: "))

print(f"{x} is {is_leap_year(x)}")