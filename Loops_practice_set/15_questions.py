num=int(input("Enter the number:"))
print("Hollow pyramid")
for i in range(1,num+1):
    if i==1 or i==num:
        print(" "*(num-i)+"*"*(2*i-1),end="")
    else:
        print(" "*(num-i)+"*"+" "*(2*(i-1)-1)+"*",end="")
    print()