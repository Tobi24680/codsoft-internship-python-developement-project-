def add(a,b):
    print("\nans:",a+b)

def sub(a,b):
    print("\nans:",a-b)

def multiply(a,b):
    print("\nans:",a*b)

def divide(a,b):
    print("\nans:",a/b)

def  exp(a,b):
    print('\nansS:',a**b)


def values():
   global a
   a=int(input("ENTER A VALUE FOR a:"))
   global b
   b=int(input("ENTER A VALE FOR b:"))

if __name__=="__main__":
    print("....calculator....\n")
    values()
    while True:
        print("\n")
        print("1.Add")
        print("2.Sub")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exponential")
        print("6.Exit")

        c=int(input("ENTER THE CHOICE FOR CALCLATE:"))
        if c==1:
            add(a,b)
        elif c==2:
            sub(a,b)
        elif c==3:
            multiply(a,b)
        elif c==4:
            divide(a,b)
        elif c==5:
            exp(a,b)
        elif c==6:
            break
        else:
            print("INVALIDE INPUT TRY AGAIN")

print("visit again...")
