#User Registrations signin signup
from database import *
from bank import bank
from customer import *
import random

def SignUp():
    username=input("Create Username: " )
    temp=db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print("User Already Exists")
        SignUp()
    else:
        print("User is Available Please Proceed: ")
        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        city = input("Enter Your City: ")
        while True:
            account_no = int(random.randint(10000000,99999999))
            temp = db_query(f"SELECT account_no FROM customers WHERE account_no = '{account_no}';")
            if temp:
                continue
            else:
                print("Your Account Number",account_no)
                break
    cobj = customer(username,password,name,age,city,account_no)
    cobj.createuser()
    bobj=bank(username,account_no)
    bobj.craete_transaction_table()
    
def SignIn():
    username=input("Enter Username: " )
    temp=db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} Enter Your Password: ")
            temp=db_query(f"SELECT password FROM customers where username = '{username}';")
            #print(temp[0][0])
            if temp[0][0] == password:
                print("Signed In succesfully")
                return username
            else:
                print("Wrong Password Try Again")
                continue
    else:
        print("Enter Correct Username")
        SignIn()