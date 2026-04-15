#Find the greatest of 4 number entered by user
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))
d=int(input("Enter number 4:"))
if a>b and a>c and a>d:
    print("Number 1 is the greatest number among the entered number:",a)
elif b>a and b>c and b>d:
    print("Number 2 is the greatest number among the entered number:",b)
elif c>a and c>b and c>d:
    print("Number 3 is the greatest number among the entered number:",c)
else:
    print("Number 4 is the greatest number among the entered number:",d)
print("End of the program")
