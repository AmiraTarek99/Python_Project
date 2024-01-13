from createproject import *
from deleteproject import *
from editproject import *
from listproject import *
from main import main

def usermenu():
    print("------Welcom to your account------")
    print("1-Create a new project")
    print("2-Edit a project")
    print("3-Delete a project")
    print("4-list all projects")
    print("5-log out")
    print("6-Exit")


    
    while True :
        choice=input("choose an option: ")
        if choice.isdigit():
            choice=int(choice)   
            if choice == 1 :
                createproject()
                break
            elif choice==2  :
                editproject()
                usermenu()    
                break
            elif choice==3  :
                deleteproject()
                usermenu() 
                break
            elif choice==4  :
                listprojects()
                usermenu()
                break
            elif choice==5  :
                print("you have logged out successfully !")
                main()
                break
            elif choice==6  :
                exit
                break
            else :
                print("please enter a valid option")
                
                      
        else:
            print("please enter a valid option")
