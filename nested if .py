medical_cause=input("Did you have a medical cause? (Y/N):").strip().upper()
if medical_cause =='Y':
    print("YOU ARE ALLOWED")
else:
    atten=int(input("Enter the attendence of line student "))
    if atten>=75:
        print("Allowed")
    else:
        print("Not Alowed")