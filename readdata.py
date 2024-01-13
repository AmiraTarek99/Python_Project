import json

#read data from users json file 
def readusersdata():
    try:
        with open('users.json','r') as fileobj :
            jsonContent = fileobj.read()
            jsondata = json.loads(jsonContent)
            return jsondata
    except Exception as e:
        print(e)


#check if email exists
def checkifemailexist (email)  :
    jsondata=readusersdata()
    for i in range(0,len(jsondata)):
        if email == jsondata[i]['email']:
            print("This email already exists") 
            return False
        else :
            return True