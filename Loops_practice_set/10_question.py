# . Count the number of digits in a given number using a while loop.
num=int(input("Enter the number:"))
count=0
if num==0:
    count=1
else:
    while num>0:
        num = num//10
        count +=1
print("The number of digit present in given number is:",count)

