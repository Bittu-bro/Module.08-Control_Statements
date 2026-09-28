# ==, !=, <, >, <=, >=
# Syntax of if
# Indentation

# #if condition:   # If the program's "condition" is true, it will run; otherwise, it will not.
#     statement1 
#     statement2
#     statement3
#     statement........N
#print(rest of the program) # There is no condition attached to this, so it will always be just one run.


age = float(input("Enter your age: "))
if age >= 18:
    print("Congrats! you are an adult, you can now cast vote.!!!!")
print("Rest of the program")