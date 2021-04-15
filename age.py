age_1=int(input("enter the age="))
age_2=int(input("enter the number="))
age_3=int(input("enter the number="))
if age_1>age_2 and age_1>age_3:
    print("age_1 is grater than age_2 and age_3")
elif age_2>age_1 and age_2>age_3:
    print("age_2 isgrater tha age_1 and age_3")
elif age_3>age_1 and age_3>age_2:
    print("age_3 is grater than age_1 and age_2")
else:
    print("all  age equal")         