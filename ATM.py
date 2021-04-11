from datetime import datetime
from auth import *

name = input("what is your name?\n")
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

if (name in allowedUsers):
    password = input("your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):

        now = datetime.now()
        print(f"welcome {name}")
        print(f"Time is: {now}")
        print("these are the available options:")
        print("1. withdrawal")
        print("2. cash deposit")
        print("3. complaint")
        selectedOption = int(input("please select an option:"))
        if (selectedOption == 1 ):

            amount = int(input("How much would you like to withdraw? \n"))
            print("Take your cash")

        elif (selectedOption == 2):
            amount = int(input("How much would you like to deposit? \n"))
            print(f"Your current balance is {amount}")


        elif (selectedOption == 3):
            complaint = input("What issue will you like to report? \n")
            print("Thank you for contacting us")

        else:

            print("invalid option, please try again")



    else:
        print("password incorrect. please try again")    
else:
    print("Name not found, please try again")


init()