# 11. Print this pattern using nested for loop:
# .
# 1
# 12
# 123
# 1234
# 12345
num=int(input("Enter the number"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()