#registeration function 
import json
import maskpass
from validation import *
from readdata import *



def register () :
    data= {}
    print("Welcom to our system, create your account") 
    
    while True :
        firstname=input("Enter your first name: ")
        if checkname(firstname) :
            data['first name'] = firstname 
            break   
        else:
           print("Invalid name,please enter it again")
 
    while True :
        lastname=input("Enter your last name: ")
        if checkname(lastname) :
            data['last name'] = lastname
            break
        else:
            print("Invalid name,please enter it again")
                 
           
    while True :
        myemail=input("Enter your email: ")
        
        if checkmail(myemail) :
            if checkifemailexist(myemail) :
                data['email'] = myemail
                break
        else:
            print("Invalid email,please enter it again") 

    while True :
        password= maskpass.askpass(prompt="Enter your password:", mask="*")
        if checkpassword(password) :
            data['password'] = password
            break
        else:
            print("Invalid password,please enter it again (hint: password must contain at least 8 characters of lower,upper case ,numbers and special characters)") 

    while True :
        confirm=maskpass.askpass(prompt="Confirm your password: ", mask="*")
        if confirm == password :
            break
        else:
            print("It is not the same password ,please enter it again")  

    while True :
        phone=input("Enter your phone number: ")
        if checkphone(phone) :
            data['phone'] = phone
            break
        else:
            print("Invalid phone number,please enter it again")
    olddata= readusersdata() 
         
    try :       
         
        with open('users.json','w') as fileobj :
            olddata.append(data)
            jsondata = json.dumps(olddata, indent=5)
            fileobj.write(jsondata)
            print("you have created a new account successfully !")
    except Exception as e:
        print(e) 
        