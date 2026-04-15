#Check whether  the student passed or failed if required total 40% and 33% in each subject given 3 subject  entered marks by the user
Marks1=int(input("Entered marks of first subject: "))
Marks2=int(input("Entered marks of second subject: "))
Marks3=int(input("Entered marks of third subject: "))
Total_Percentage=(Marks1+Marks2+Marks3)*100/300
if Total_Percentage>=40 and Marks1>=33 and Marks3>=33 and Marks2>=33:
    print("Passed the exam ",Total_Percentage, "%")
else:
    print("Failed,Better luck next time ",Total_Percentage, "%")