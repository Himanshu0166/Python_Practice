num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
if num2 > num1 > num3 or num3 > num1 > num2:
    print("The second Largest number is Number 1:",num1)
if num1 > num2 > num3 or num3 > num2 > num1:
    print("The second Largest number is Number 2:",num2)
if num1 > num3 > num2 or num2 > num3 > num1:
    print("The second Largest number is Number 3:",num3)