try:
    number=int(input("Enter you number :"))
    print("The number entered is ",number)
except ValueError as ex:
    print("Exception:",ex)
