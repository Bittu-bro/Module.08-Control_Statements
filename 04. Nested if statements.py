'''

if marks >= 60, student is pass else student fail
and the student is pass, then we print grade
>= 90, grade A
80 to 89, grade B
70 to 79, grade C
60 to 69, grade D
< 60 , grade Fail

'''


marks = float(input("Enter your marks: "))
if marks >= 60:
    print("Congrats, You passed the Exam.")
    if marks >= 90:
        print("Your grade is A")
    elif marks >=80 and marks < 90:
        print("Your grade is B")
    elif 70 <= marks <80:
        print("Your grade is C")
    else:
        print("Your grade is D")
else:
    print("You have failed, Study hard next time.")