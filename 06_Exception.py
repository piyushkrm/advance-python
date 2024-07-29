try :
    a = int(input("Enter a number : "))

except Exception as e :
    print(e)

# Different types of error
except ValueError as v:
    print(v)

except TypeError as t:
    print(t)

except ZeroDivisionError as z:
    print(z)

