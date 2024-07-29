#  5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

no = int(input("Enter the number for print table of a number : "))

i = 1
table = [no * i for i in range(1, 11)]
with open("F:/Advance Python/Chapter 12_PS/Tables.txt", "a") as f :
    f.write(f"Table of {no} : {str(table)}\n")
