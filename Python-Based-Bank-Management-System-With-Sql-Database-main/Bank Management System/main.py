from register import *
from bank import *

status=False

print("Welcomr to DBMS Banking Project")
while True:
    try:
        register = int(input("1. SignUp\n"
                             "2. SignbIn\n"))
        if register == 1 or register == 2:
            if register==1:
                SignUp()
            if register==2:
                user=SignIn()
                status=True
                break
        else:
            print("Please Enter Valid Input From Options")
    except ValueError:
        print("Invalid Input Try Again With Numbers")
        

account_number = db_query(f"SELECT account_no FROM customers WHERE username='{user}';")


while status:
    print(f"Welcome {user.capitalize()} choose your banking service\n")
    try:
        facility = int(input("1. Balance Enquiry\n"
                             "2. Cash Deposit\n"
                             "3. Cash Withdraw\n"
                             "4. Fund Transfer\n"))
        if facility >= 1 and facility <= 4:
            if facility==1:
                bobj=bank(user,account_number[0][0])
                bobj.balanceenquiry()
                
            elif facility==2:
                while True:
                    try:
                        amount=int(input("Enter Amount to Deposit"))
                        bobj=bank(user,account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
                    
            elif facility==3:
                while True:
                    try:
                        amount=int(input("Enter Amount to Withdraw"))
                        bobj=bank(user,account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
                    
            elif facility==4:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number"))
                        amount = int(input("Enter Money to Transfer"))
                        bobj=bank(user,account_number[0][0])
                        bobj.fundtransfer(receive,amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
        else:
            print("Please Enter Valid Input From Options")
            continue
        
    except ValueError:
        print("Invalid Input Try Again With Numbers")
        continue