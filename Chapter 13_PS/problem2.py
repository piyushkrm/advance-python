"""
2. Write a program to input name, marks and phone number of a student and format it using the format function like below:

"The name of the student is Pihu, his marks are 92 and phone number is 7488241964"
"""

name = input("Enter your name : ")

marks = int(input("Enter your marks : "))

phnNo = int(input("Enter your phone number : "))

sentence = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phnNo)
print(sentence)