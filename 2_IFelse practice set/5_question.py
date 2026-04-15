# Write a program for grading the student score
student_marks=int(input("Enter your marks:"))
if student_marks<=100:

    if student_marks>=90:
        print("Congratulation on scoring Ex grade")
    elif 80 <= student_marks < 90:
        print("Congratulation on scoring A grade")
    elif 70 <= student_marks < 80:
        print("Congratulation on scoring B grade")
    elif 60 <= student_marks < 70:
        print("Congratulation on scoring C grade")
    elif 50 <= student_marks < 60:
        print("Congratulation on scoring D grade")
    else:
        print("Your grade is F")
else:
    print("Enter the marks between 100")