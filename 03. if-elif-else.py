'''
>= 90, grade A
80 to 89, grade B
70 to 79, grade C
60 to 69, grade D
< 60 , grade Fail
'''

# if - elif - else
marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Your grade is A")
elif marks >=80 and marks < 90:  # 80 <= marks < 90
    print("Your grade is B")
elif 70 <= marks <80:
    print("Your grade is C")
elif marks >=60 and marks < 70:
    print("Your grade is D")
else:
    print("You failed the exam.")