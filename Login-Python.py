


userName=input("Enter your user name:")
password=input("Enter your password:")

if userName == "admin":
    if password=="123":
        print("correct usarname & password, Login Successful")
    else:
        print("Wrong Password")
elif password=="123":
    print("Wrong username")
else:
    print("Wrong usarname & password, Login Fail")  
