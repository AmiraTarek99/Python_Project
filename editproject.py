from selectproject import *
from dealwithprojectdata import *
import login
import listproject as list
from validation import *

def editproject():
    data = load_data()
    list.listprojects()
    projects = data.get(login.loggedemail, [])
    if not projects:
        print('No projects found for the logged-in user.')
        return

    project_index = select_project(projects)
    if project_index is not None:
        project = projects[project_index]
        print(f"Selected Project: {project['title']}")
        print("Enter new values (leave blank to keep current value):")

        title = input(f"Title [{project['title']}]: ") or project['title']
        details = input(f"Details [{project['details']}]: ") or project['details']
        target = input(f"Details [{project['target']}]: ") or project['target']
        start_date = input(f"Start Date [{project['start date']}]: ") or project['start date']
        end_date = input(f"End Date [{project['end date']}]: ") or project['end date']

        projects[project_index] = {
            'email': login.loggedemail,
            'title': title,
            'details': details,
            'target': target,
            'start date': start_date,
            'end date': end_date
        }

     

        data[login.loggedemail] = projects
        save_data(data)
        print('Project modified successfully.')

 

