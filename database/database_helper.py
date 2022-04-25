def citizen_helper(citizen) -> dict:
    return {
        "id": str(citizen['_id']),
        "fullname": citizen['fullname'],
        "email": citizen['email'],
        "course_of_study": citizen['course_of_study'],
        "year": citizen['year'],
        "GPA": citizen['gpa']
    }

def admin_helper(admin) -> dict:
    return {
        "id": str(admin['_id']),
        "fullname": admin['fullname'],
        "email": admin['email'],
    }
