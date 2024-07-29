def myFunc() :
    print("Hello world !")



if __name__ == "__main__":
    # if the code is directly executed by running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__)
else :
    print("This code is executed by other programmer not the own programmer")