# Sum of first n natural number
a=int(input("Enter the number:"))
i=1
product=1
productt=1
while i<=a:
    product*=i
    i +=1
print(f"Factorial of {a} is {product}")
for i in range(1,a+1):
    productt *= i
print(f"Factorial of {a} is {productt}")
