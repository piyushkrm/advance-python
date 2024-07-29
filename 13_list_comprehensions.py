# list square 

myList = [2, 4, 6, 8, 10]
print(f"Before square {myList}")

squareList = []

# for item in myList :
#     squareList.append(item * item)

# do same word using list comprehension
squareList = [i * i for i in myList]


print(f"After square {squareList}")

