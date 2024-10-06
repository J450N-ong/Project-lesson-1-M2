age=input("Are you between the age of 10-20? Y or N: ")
real_age=int(input("ENTER YOUR REAL AGE: "))
if age=="Y":
    print("You are allowed to class")
else:
    if real_age>20:
        print("You are not allowed to this class")
    elif real_age<10:
        print("You are not allowed to this class")
    else:
        print("You are allowed to this class")