#  Write a program to generate electricity bill
# # Price
# # First 100 units= free
# Next 100 units Rs 5 per units
# After 200 units 10 Rs per unit
unit_used=int(input("Enter the number of unit used:"))
if unit_used<=100:
    print("No electricity Bill generated ")
elif 100<unit_used<=200:
    total_bill=(unit_used -100)*5
    print("Total Electricity Bill is",total_bill)
elif unit_used>200:
    total_bill=100*5 + (unit_used-200)*10
    print("Total Electricity Bill is",total_bill)

