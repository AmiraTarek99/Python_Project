
def select_project(projects):
    if projects:
        try:
            project_index = int(input('Enter the project number you want to select: ')) - 1
            if project_index < 0 or project_index >= len(projects):
                raise ValueError
        except (ValueError, IndexError):
            print('Invalid project number.')
            return None
        return project_index
    else:
        return None