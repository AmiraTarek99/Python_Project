import login
from validation import *
import usermenu as menu
from dealwithprojectdata import *

def createproject () :
    projectdata={}
    projectdata['email'] = login.loggedemail
   
    title=get_user_input("Enter project title: ")
    projectdata['title'] = title
  
    details=get_user_input("Enter project details: ")
    projectdata['details'] = details


    while True :
        target=input("Enter project target: ")
        if checktarget(target) :
            projectdata['target'] = target
            break   
        else:
           print("Invalid target,please enter it again")  

    while True :
        startdate=input("Enter project start date in the format YYYY-MM-DD: ")
        if checkdate(startdate) :
            projectdata['start date'] = startdate
            break   
        else:
           print("Invalid start date,please enter it again")       

    while True :
        enddate=input("Enter project End date in the format YYYY-MM-DD: ")
        if checkdate(enddate) :
            projectdata['end date'] = enddate
            break   
        else:
           print("Invalid End date,please enter it again") 

    data = load_data()
    projects = data.get(login.loggedemail, [])
    projects.append(projectdata)
    data[login.loggedemail] = projects
    save_data(data)
    print('Project created successfully.')
    menu.usermenu()
