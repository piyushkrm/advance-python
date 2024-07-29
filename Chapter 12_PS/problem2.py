# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.


myList = [10, 20, 56, 89, 23, 59, 22, 563]

for index, item in enumerate(myList) :
    if index == 2 or index == 4 or index == 6 :
        print(item)

