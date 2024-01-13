from selectproject import *
from dealwithprojectdata import *
import login
import usermenu as menu
import listproject as list

def deleteproject():
    data = load_data()
    projects = data.get(login.loggedemail, [])
    if not projects:
        print('No projects found for the logged-in user.')
        return
    list.listprojects()
    project_index = select_project(projects)
    if project_index is not None:
        del projects[project_index]
        data[login.loggedemail] = projects
        save_data(data)
        print('Project deleted successfully.')


if __name__ == '__main__':
    menu.usermenu()   
