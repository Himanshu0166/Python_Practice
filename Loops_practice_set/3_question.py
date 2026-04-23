a=int(input("Enter the number whose table you want to print:"))
print("Printing the table of",a)
i=1
while i<11:
    print(f"{a} X {i} = {a * i}")
    i += 1