hin=int(input("enter the hin="))
eng=int(input("enter the eng="))
bio=int(input("enter the bio="))
mat=int(input("enter the mat="))
chemstry=int(input("enter the che="))
physic=int(input("enter the phy="))
total=hin+eng+bio+mat+chemstry+physic
percentage=total/600*100
if percentage>=90:
    print("a,grade")
elif percentage>=80:
    print("b,grade")
elif percentage>=70:
    print("c,grade")
elif percentage>=60:
    print("d,grade")
elif ppercentage>=50:
    print("e,grade")
else:
    print("f,grade")