working_days=int(input("Enter total number of working days:"))
absent_days=int(input("Enter total number of absent days:"))
percentage_class_attend=(100-absent_days)/working_days*100
if percentage_class_attend>=75:
    print("Eligible to appear in exam:")
    print("Attendance percentage :",percentage_class_attend)
else:
    print("Not Eligible to Appear in exam:")
    print("Attendance Percentage is less than 75 :",percentage_class_attend)

