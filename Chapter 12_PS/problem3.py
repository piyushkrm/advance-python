# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.

no = int(input("Enter the number for print table of a number : "))

i = 1
table = [no * i for i in range(1, 11)]

print(table)