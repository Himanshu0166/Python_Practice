age=int(input("Enter your age:"))
sex=input("Enter your gender M or F:")
working_days=int(input("Enter your number of working days:"))
if sex=="M" or sex=="m":
    if 18<=age<30:
        wages=700*working_days
        print("Your total wages is:",wages)
    elif 30<=age<=40:
        wages=800*working_days
        print("Your total wages is:",wages)
    else:
        print("Enter appropriate age")

if sex=="F" or sex=="f":
    if 18<=age<30:
        wages=750*working_days
        print("Your total wages is:",wages)
    elif 30<=age<=40:
        wages=850*working_days
        print("Your total wages is:",wages)
    else:
        print("Enter appropriate age")
