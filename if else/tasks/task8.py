a=int(input("give a number for a="))
b=int(input("give a number for b="))
c=input("Arithmetic expression=")
if(c=="add"):
    c=a+b
    print(c)
elif(c=="sub"):
    c=a-b
    print(c)
elif(c=="multi"):
    c=a*b
    print(c)
elif(c=="div"):
    c=a/b
    print(c)
else:
    print("invalid input")
