from login import *
from register import register as reg


def main(): 
    print("------Welcome to our crowd funding app------")
    print("1-login to your account")
    print("2-create new account")
    print("3-Exit")

    try:
        while True :
            choice=input("choose an option: ")
            if choice.isdigit():
                choice=int(choice)   
                if choice == 1 :
                    login()
                    main()
                    break
                elif choice==2  :
                    reg()
                    main()
                    break
                elif choice==3  :
                    exit
                    break
                else :
                    print("please enter a valid option")
                    
                      
            else:
                print("please enter a valid option")
    except Exception as e :         
        print(e) 

if __name__ == '__main__':
    main()