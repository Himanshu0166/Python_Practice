a=int(input("Enter the number:"))
for i in range(1,a+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

b=1
while b<=a:
    if b % 3 == 0 and b % 5 == 0:
        print(b)
    b +=1