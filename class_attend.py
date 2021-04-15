class_attend=int(input("enter class_attend="))
class_held=int(input("enter class_held="))
attendance=class_attend/class_held*100
if attendance>75:
    print("you give exam")
else:
    print("not give exam")    