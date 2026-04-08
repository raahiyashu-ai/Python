print("Select your Ride:")
print("1.Bike")
print("2.Car")
choice=int(input("Enetr your choice:"))
if choice==1:
    print("What type bike you want?")
    print("1.BMW/n")
    print("2.Duke/n")
    choice2=int(input("Enter your choice2:"))
    if choice2==1:
      print("You have selected BMW")
    else:
      print("You have selected Duke")
elif(choice==2):
    print("What type bike Car you want?")
    print("1.Bugatti/n")
    print("2.Lambourgine/n")
    choice=int(input("Enter your choice2:"))
    if choice==1:
      print("You have selected Bugatti")
    else:
      print("You have selected Lambourgine")