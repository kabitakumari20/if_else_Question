# a=int(input("enter the num="))
# b=int(input("enter the num="))
# c=a%b
# d=a-c
# if d%b==0:
# 	print(d)
# else:
# 	print("not dividiable")


# num=int(input("enter the num="))
# a=int(input("enter the a="))
# b=int(input("enter the b="))
# if num%a==0 and num%b==0:
# 	print("true")
# else:
# 	print("false")

# a=int(input("enter the a="))
# b=int(input("enter the b="))
# c=int(input("enter the c="))
# if a>b:
#     if a>c:
#         print(a,"grater")
# elif b>a:
#     if b>c:
#         print(b,"grater")
# elif c>a:
#     if c>b:
#         print(c,"grater")
#     else:
#         print("nothing")
# else:
#     print("all equal")


num=input("enter the num=")
i=0
sum=0
while i<len(num):
	sum=sum+(num[i])
	i=i+1
print(sum)