a=int(input("Enter your age:"))
# We can also add separate if statement in program
# If statement no 1:
if a%2==0:
    print("You are eligible to get discount,Only if you are above legal age")
# If statement no 2:ladder
if a>=18:
    print("You are eligible to enter")
    if a % 2 == 0:
        print("Even age Special discount")
    else:
        print("NO discount,Try next year")
elif a==0:
    print("You entered your age as Zero")
elif a<0:
    print("Are you joking by entering negative age")
else:
    print("You are under age,Not eligible")
print("This is the end of the program")