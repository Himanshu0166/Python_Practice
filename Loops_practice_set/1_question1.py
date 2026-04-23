a=int(input("Enter the number whose table you want to print:"))
print("Printing the table of",a)
for i in range(1,11):
    print(a," X ",i," = ",a*i)
for i in range(1,11):
    print(f"{a} X {i} = {a*i}")