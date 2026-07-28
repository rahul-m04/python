age=int(input("your age:"))
salary=int(input("your salary:"))
if(salary>=20000 or age<=25):
    amount=int(input("Required loan amount="))
    if(amount>=50000):
        print("maximum loan amount is 50000")
    else:
        print("you are eligible")
else:
    print("your are not eligible")
