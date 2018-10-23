def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y
print("write")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
while True:
    a=int(input("enter the operator number:-"))
    x=float(input("Enter the first value:-"))
    y=float(input("Enter the second value:-"))
    if (a==1):
        print(add(x,y))
    elif (a==2):
        print(sub(x,y))
    elif (a==3):
        print(multi(x,y))
    elif (a==4):
        print(div(x,y))
    else:
        print("unknown operator")
