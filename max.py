
a=int(input("enter the first number:-"))
b=int(input("enter the second number:-"))
c=int(input("enter the third number:-"))
if a>b:
    if a>c:
        print(a,"a is maximum")
    else:
        print("empety")
elif b>c:
    if b>a:
        print(b,"b is maximum")
    else:
        print("empety")
elif c>a:
    if c>b:
        print(c,"c is maximum")
    else:
        print("empety")
else:
    print("nothing")