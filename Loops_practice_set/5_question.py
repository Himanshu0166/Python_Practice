# Sum of first n natural number
a=int(input("Enter the number:"))
i=1
sum=0
summ=0
while i<=a:
    sum +=i
    i +=1
print(sum)

for i in range(1,a+1):
    summ +=i
print(summ)