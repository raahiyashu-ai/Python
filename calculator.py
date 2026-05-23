def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

try:
    print("Pick any operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice=input("Enter you choice (1/2/3/4):")
    num1=float(input("Enter first number:"))
    num2=float(input("Enter you second number:"))
    if choice=='1':
        print("result:",add(num1,num2))
    elif choice=='2':
        print("result:",subtract(num1,num2))
    elif choice=='3':
        print("result:",multiply(num1,num2))
    elif choice=='4':
        print("result:",divide(num1,num2))
    else:
        print("Invalid")
except ZeroDivisionError:
    print("Error:Cannot be divided with zero/0")