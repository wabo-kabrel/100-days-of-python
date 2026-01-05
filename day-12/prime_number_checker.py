def is_prime(num):
    if num <= 1:
        return "Not a prime number"

    elif num == 2:
        return "Prime number"
    
    else:
        for i in range (2, num):
            if num % i == 0:
                return "Not a prime number"
            else:
                return "Prime number"
    
print(is_prime(int(input("Enter a number: "))))