# Blaine Swieder
# Even Odd Checker (using Recursion)
# May 30th, 2025

def is_even(number): 
    if number == 0: 
        return True
    elif number == 1: 
        return False
    else: 
        return is_even(number - 2) 
    
num = int(input("Enter a number: "))

if is_even(num): 
    print(f"The number {num} is even.")
else: 
    print(f"The number {num} is odd.")
