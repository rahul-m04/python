score=int(input("Your score out of 100="))
if(score<35):
    print("Poor student")
elif(score>35 and score<70):
    print("average student")
elif(score>70 and score<100):
    print("Good student")
else:
    print("Invalid score")
