pasword=input("enter the num,upper case,lower case,symbol=")
if pasword>="0" and pasword<="9":
    if pasword>="A" or pasword<="Z" and pasword>="a" or pasword<="z":
        if pasword>="#" and pasword>="@":
            print("it is stron pasword")
        else:
            print("it is not strong")


# pasword=input("enter the num,alphabet,symbol=")
#  if pasword>="0" or pasword<="9":
#      if pasword>="A" or pasword<="Z" :
#          if pasword>="#" or pasword>="@":
#              print("it is stron pasword")
#          else:
#              print("it is not strong")