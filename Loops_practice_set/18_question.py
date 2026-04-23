num=int(input("Enter the number:"))
print("Reversing the number")
reverse=0
temp=num
for i in range(1,len(str(num))+1):
    last_digit= temp%10
    reverse= reverse*10 + last_digit
    temp=temp//10
print(f"Reverse of the num {num} is {reverse}")
print("Checking the number is Palindrome or not")
print("Checking")
if num==reverse:
    print("Number  is Palindrome")
else:
    print("Number is not palindrome")
