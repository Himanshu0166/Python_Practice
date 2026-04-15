side1=int(input("Enter side1 of triangle:"))
side2=int(input("Enter side2 of triangle:"))
side3=int(input("Enter side3 of triangle:"))
if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
    print("Triangle of given side is possible")
else:
    print("Triangle of given side is not possible")
