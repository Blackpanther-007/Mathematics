def add(a,b):
    return a+b
def multi(a,b):
    return a*b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b

a =int(input("Enter 1st num: "))
b= int(input("Enter 2nd num: "))

c= int(input("Enter\n1 for addition \n2 for substraction \n3 for multiplication\n4 for divding:"))
if c==1:
    print("Sum:",add(a,b))
if c==2:
    print("Subs:",sub(a,b))
if c==3:
    print("Mutli:",multi(a,b))    
if c==4:
    print("dividation:",div(a,b))
if c>4 or c<1:
    print("Invalid input for function. Enter correct value")