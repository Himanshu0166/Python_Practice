# Question 1
num=int(input("Enter the number:"))
if num%2==0:
    print("Even")
else:
    print("odd")
# Question 2
num2=int(input("Enter the number:"))
if num2%7==0:
    print("Multiple of 7")
else:
    print('Not Multiple of 7')

# Question 3

a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))
c=int(input("Enter the number3:"))
if a>b and a>c:
    print("Number 1 is greatest Number:")
elif b>a and b>c:
    print("Number 2 is greatest number")
else:
    print('Number 3 is greatest number:')