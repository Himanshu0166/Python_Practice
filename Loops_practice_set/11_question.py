# 8. Reverse a number using a while loop.
num=int(input("Enter the Number:"))
rev=0
while num>0:
    last_digit=num%10
    rev = rev*10 + last_digit
    num = num//10
print("Reverse digit is :",rev)