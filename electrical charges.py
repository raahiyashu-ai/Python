Units =int(input("Enter your daily consumtion of elcticity in Unites:"))
if Units<50:
    amount= Units*2.60
    surcharge=25
elif Units<=100:
    amount= 130 +((Units-50)*3.25)
    surcharge=35
elif Units <=200:
    amount=130 +162.50+((Units-100)*5.26)
    surcharge=45
else:
    amount=130+162.50+526+((Units-200)*8.45)
    surcharge=75
    total=Units+amount
print("\n Electricity Bill= %.2f"%total)