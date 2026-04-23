# Number Pattern
num=int(input("Enter the number:"))
print("Increasing number Pattern")
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("Same number repeated")
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print("Decreasing number Triangle")
for i in range(num,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print("Reverse number Triangle")
for i in range(num):
    for j in range(num,i,-1):
        print(j,end=" ")
    print()
print("Pyramid of numbers")
for i in range(1,num+1):
    print(" " * (num - i), end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()

