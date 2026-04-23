a=int(input("Enter the number:"))
for i in range(2,a):
    if (a%i) == 0:
        print("Number is not a Prime Number:")
        break
else:
    print("Number is prime number:")
