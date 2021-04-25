#Register
# - First_name, Last_name and Email
# Generate user account

#login
#accountnumber, 
# - password

#Bank_operations
#Initializing the system

import random 
import datetime as dt
import database
import validation
from getpass import getpass 



def init():
    print('welcome to Zuri bank')
    Haveaccount = int(input('Do you have an account with us: 1(YES) 2(NO) \n'))
    if(Haveaccount == 1):
        login()
        current_datetime = dt.datetime.now()
        print(current_datetime)

    elif(Haveaccount == 2):
        register()
        

    else:
        print('You have selected invalid Option')
        init()

def login():
    print("######## log in your details into the banking system ########")

    accountnumberfromuser = input("What is your account number?\n")

    is_valid_accountnumber = validation.accountnumber_validation(accountnumberfromuser)

    if is_valid_accountnumber:

        password = getpass("What is your password?\n")
        
        user = database.authenticated_user(accountnumberfromuser, password);

        if user:
            bankoperation(user)


        print ("Invalid account or password")
        login()
   
    else:
        init()


def register():
    print("###### register with Zuri bank #####")
    email = input("What is your email address?\n")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    password = input("Create a password for yourself\n")
    
    accountnumber = generateaccountnumber()

    is_user_created = database.create(accountnumber, first_name, last_name, email, password)
    
    if is_user_created:

        print("Your account has been created")
        print("###### system initializing in progress ######")
        print("Your accountnumber is: %d" % accountnumber)
        print("Make sure you keep it safe and do not share it with anyone")
        print("###### thank you for registering with Zuri bank ####")
        
        current_datetime = dt.datetime.now()
        
        print(current_datetime)
        
        login()
    
    else:
        print("something went wrong, try again later")
        
        register()


def bankoperation(user):
    print("Welcome %s  %s" %(user[0], user[1]))

    selectedoption = int(input("What would you like to do? (1) deposit (2) Withdrawal (3) complaint (4)logout (5) exit\n"))
    
    if(selectedoption == 1):
        
        depositoperation()
    elif(selectedoption == 2):
        
        withdrawaloperation()
   
    elif(selectedoption == 3):
        
        complaintoperation()
    
    elif(selectedoption == 4):
        
        logout()
    elif(selectedoption == 5):
        
        exit()
    else:
       
        print("Invalid operation selected")
        bankoperation(user) 

def generateaccountnumber():
    print("Generating account number")
    return random.randrange(1111111111,9999999999)

def logout():
    
    print("You have successfully log out of the system")
    login()

def withdrawaloperation():
    print("Welcome to withdrawal operation on zuri bank")
    print('Withdrawal Amount')
    print('1, NGN200')
    print('2, NGN300')
    print('3, NGN400')
    selectedOption = int(input('please select an option:'))
    if(selectedOption == 1):
        print('Insufficient cash in your Zuri account')
        print('You have 0.00 naira in your Zuri account')
        print('Thank you for banking with us')
    if(selectedOption == 2):
        print('Insufficient cash in your Zuri account')
        print('You have 0.00 naira in your Zuri account')
        print('Thank you for banking with us')
    if(selectedOption == 3):
        print('Insufficient cash in your Zuri account')
        print('You have 0.00 naira in your Zuri account')
        print('Thank you for banking with us')
        
    selectedoption = int(input("Will you like to perform another operation? (1) Yes (2) No? \n"))
    
    if(selectedoption == 1):
        return bankoperation()
   
    if(selectedoption == 2):
        
        logout()


def depositoperation():
    
    print("welcome to deposit operation on zuri bank")
    print('select Deposit amount')
    print('1, NGN200')
    print('2, NGN300')
    print('3, NGN400')
    selectedOption = int(input('please select an option:'))
    if(selectedOption == 1):
        print('NGN200')
        print('Balance; NGN1200')
        print('Thaank you for banking with us')
    if(selectedOption == 2):
        print('NGN300')
        print('Balance; NGN1300')
        print('Thank you for banking with us')
    if(selectedOption == 3):
        print('NGN400')
        print('NGN1400')
        print('Thank you for banking with us')

    logout()




def get_current_balance(user_data):
    return user_data[4]
    print("Your account balance with Zuri bank is 0.00 naira")

def complaintoperation():
    print('you are to log a complaint')
    print ('Report issue\n')
    print ('1, Inaccurate Balance')
    print ('2, Wrongful debit')
    
    selectedOption = int(input('please select an option:'))
    if(selectedOption == 1):
        print('Complaint Noted')
        print('Error will be corrected')
        print('Thank you for contacting us')
    
    if(selectedOption == 2):
        print('Complaint Noted')
        print('Debit will be rectified')
        print('Thank you for contacting with us')
    
init()
    


