# 4. Write a program to filter a list of numbers which are divisible by 5.

def divisible5(n) :
    if n % 5 == 0:
        return True
    return False


n = [1, 22, 36, 56, 78957521, 15690, 985, 6955, 27120, 5555, 225110]

filte = list(filter(divisible5, n))
print(filte)