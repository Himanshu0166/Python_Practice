salary=int(input("Enter your total salary:"))
year_of_service=int(input("Enter the number of year of service"))
if year_of_service>10:
    bonus=10*salary/100
    print("Thank you for your",year_of_service,"year's of service")
    print("Your Net Bonus is ",bonus)
elif 6<=year_of_service<=10:
    bonus=8*salary/100
    print("Thank you for your", year_of_service, "year's of service")
    print("Your Net Bonus is ",bonus)
else:
    bonus=5*salary/100
    print("Thank you for your",year_of_service,"year's of service")
    print("Your Net Bonus is ",bonus)
