#factorial
#using while
num=int(input("enter number:"))
fac=1
i=1
while i<=num:
    fac*=i
    i+=1
print(f"Factorial of {num} is {fac}")

#using for loop

num1=int(input("enter number:"))
fac1=1
for j in range(1,num1+1):
    fac1*=j
print(f"Factorial of {num1} is {fac1}")
