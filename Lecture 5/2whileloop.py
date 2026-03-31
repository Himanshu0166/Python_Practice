#question 1
i=1
while i<=100:
    print(i)
    i+=1
print("Loop ended")

# Question 2
j=100
while j>=1:
    print(j)
    j-=1
print("Loop ended")

# Question 3
a=int(input("Enter number for to generate its table:"))
k=1
print("Printing Table of ",a)
while k<=10:
    print(f"{a} X {k} = {a*k}")
    k+=1
#Question 4
b=[1,4,9,16,25,36,49,64,81,100]
x=0
while x<len(b):
    print(b[x])
    x+=1
#question 5
c=(1,4,9,16,25,36,49,64,81,100)
y=36
z=0
while z<len(c):
    if c[z]==y:
        print("Found at index,",z)
        break
    else:
        print("Finding")
    z+=1

