import login
import usermenu as menu
from dealwithprojectdata import *

def listprojects () :
    data = load_data()
    projects = data.get(login.loggedemail, [])
    if not projects:
        print('No projects found for the logged-in user.')
    else:
        for index, project in enumerate(projects):
            print(f"Project {index + 1}:")
            print(f"Title: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Target: {project['target']}")
            print(f"Start Date: {project['start date']}")
            print(f"End Date: {project['end date']}")
            print()

