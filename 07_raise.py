x = int(input("Enter the 1st number : "))
y = int(input("Enter the 2nd number : "))

if x / y == 0:
    raise ZeroDivisionError
else:
    print(f"The division of the number {x} and {y} is {x / y } : ")