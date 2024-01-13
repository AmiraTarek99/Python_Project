import maskpass
from readdata import readusersdata
from usermenu import *

#login function
def login ():
    
    emailfound=0
    data=readusersdata()
    passflag=0
    email=input("Enter your email: ")
    for i in range(0,len(data)):
        if email == data[i]['email']:
            location=i
            emailfound=1
            passflag=1
            break       
            
    if emailfound==0 :
        print("This email is not found ")
        
    else:                 
        while passflag==1 :  
            password= maskpass.askpass(prompt="Enter your password:", mask="*")
            if password == data[location]['password'] :
                global loggedemail
                loggedemail=email
                print("you have logged successfully !")
                usermenu()
            
                break
            else :
                print("Incorrect password, try to enter it again")    