num=int(input("Enter the number:"))
for i in range(1,num+1):
    print(2*i-1,end=" ,")
print()
print("Even number")
for i in range(1,num+1):
    print(2*i,end=" ,")
print()
print("First n odd number")
count=0
sum=1
while count<num:
    print(sum,end=" ")
    sum +=2
    count +=1
print()
print("First n even number")
count=0
sum=2
while count<num:
    print(sum,end=" ")
    sum +=2
    count +=1
print()
print("Square of n  number")
for i in range(1,num+1):
    print(i*i,end=" ")
print()
print("Sum of first n natural number")
countt=1
summ=0
while countt<=num:
    summ =summ+countt
    countt +=1
print(summ)
print("Power of 2")
for i in range(1,num+1):
    print(2**i,end=",")
# Print a custom series: 1, 3, 6, 10, 15, 21... (triangular numbers)
# Formula: sum = sum + i
print(summ)
print("Print Custom series")
suum=0
for i in range(1,num+1):
    suum=suum+i
    print(suum,end=",")


