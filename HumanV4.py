number=int(input("Enter your number:"))
def cube(number):
    return number*number*number
def by_three(number):
    if number %56 ==0:
        return cube(number)
    else:
        return False
print(by_three(9))
print(by_three(4))