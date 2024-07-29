# finally keyword are used in the function  when value are return but finally block are executed


def main() :
    try :
        a = int(input("Enter a number : "))
        return

    except Exception as e :
        print(e)
        return

    finally : 
        print("I am inside the finally")


main()