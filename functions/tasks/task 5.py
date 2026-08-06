s_username="rahul"
s_password="endure"

username=input("Enter your username=")
password=input("enter your password=")

def validate():
    if(s_username==username and s_password==password):
        return True
    else:
        return False
a=validate()
print(a)
