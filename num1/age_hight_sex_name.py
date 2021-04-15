age=int(input("enter the age="))
sex=input('enter the sex=')
name=input("enter the post name=")
hight=int(input("enter the hight="))
if age>=18 and age<=40:
    if sex=="male":
        if hight>=160:
            print("your selected for police")
    elif sex=="female":
        if hight>=150:
            print("your selected for police")
        else:
            print("not selected for this post")
    else:
        print("hight is not aviliable")
else:
    print("nothing")

