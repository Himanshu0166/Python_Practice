# Advance series
num=int(input("Enter the number:"))
print("Factorial")
sum=1
for i in range(1,num+1):
    sum=sum*i
print(f"The Factorial of {num} is {sum}")
print("Fibonacci Series")
a,b=0,1
print("Printing Fibonacci series")
for i in range(1,num+1):
    print(a,end=",")
    a,b=b,a+b



