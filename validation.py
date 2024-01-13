import re

#validation function for name
def checkname (name)  :
    if name.isalpha():
        return True
    else:
        return False

#validation function for email
def checkmail (mail)  :
    reg= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(reg,mail):
       return True
    else:
        return False



#validation function for password
def checkpassword (password)  :
    if len(password) < 8 or len(password)>20 :  
        return False  
    if not re.search("[a-z]", password):  
        return False  
    if not re.search("[A-Z]", password):  
        return False  
    if not re.search("[0-9]", password):  
        return False  
    if not re.search("['$', '@', '#', '%']", password):  
        return False  
    return True  


#validation function for phone number

def checkphone (phone)  :
    reg= r'\b^01[0125][0-9]{8}$\b'

    if re.match(reg,phone):
       return True
    else:
        return False
    
def checktarget (target)  :
    if target.isdigit() :
        target=float(target)
        return True
    else:
        return False


def checkdate (date):
    reg= r'^\d{2}-\d{2}-\d{4}$'
    if re.match(reg,date):
       return True
    else:
        return False

def get_user_input(prompt):
    user_input = input(prompt)
    while not user_input:
        print("Input is required. Please try again.")
        user_input = input(prompt)
    return user_input


