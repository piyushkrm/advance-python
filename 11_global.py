a = 10      #Global variable

def glo() :
    a = 40      # Local variable
    global n
    n = 45      # Global variable
    print(a)

glo()

print(a)