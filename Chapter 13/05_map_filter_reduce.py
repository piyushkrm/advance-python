#  Map Example

ls = [6, 2, 3, 4, 5]

square = lambda x : x*x

sprList = map(square, ls)

for i in sprList:
    print(i)



#  Filter Example
lis = [10, 15, 20, 18, 13, 28]

def even(n) :
    if n % 2 == 0:
        return True
    return False

onlyEven = filter(even, lis)
print(list(onlyEven))