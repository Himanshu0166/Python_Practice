# Basic star patterns
num=int(input("Enter the number:"))
print("Right angle triangle")
for i in range(1,num+1):
    print("*"*i)

print("Right angle triangle align to right")

for i in range(1,num+1):
    print(" "*(num-i)+ "*"*i)
print("Inverted Right angle triangle")
for i in range(num,0,-1):
    print("*" * i)
print("Inverted Right angle triangle align to right")
for i in range(num,0,-1):
    print(" "*(num-i)+"*" * i)
print("Pyramid pattern")
for i in range(1,num+1):
    print(" "*(num-i)+ "*"*(2*i-1))
print("Inverted Pyramid pattern")
for i in range(num,0,-1):
    print(" "*(num-i)+ "*"*(2*i-1))
print("Diamond pattern")
for i in range(1,num+1):
    print(" "*(num-i)+ "*"*(2*i-1))
for i in range(num-1,0,-1):
    print(" "*(num-i)+ "*"*(2*i-1))
print("Hollow Star Pattern")
for i in range(1,num+1):
    if i==1 or i==num:
        print("*"*num)
    else:
        print("*"+" "*(num-2)+"*")