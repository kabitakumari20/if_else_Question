print("welcome")
print("enter the your atm card")
language=input("enter the language=")
if language=="english" and language=="hindi":
    print("english")
    saving_ac=input("enter the saving_ac")
    pin=int(input("enter the pin="))
    if pin>=0 and pin<=9:
        if pin>=0 and pin<=4:
            print("pin is creact")
            amount=int(input("enter the amount"))
            if amount>=10000 and amount<=10000:
                print("total amount")