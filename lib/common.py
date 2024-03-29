import os

def logn_auth(user_type):
    from core import admin,student,teacher
    def atut(func):
        def wrapper(*args,**kwargs):
            if user_type == "admin":
                if not admin.admin_info["name"]:
                    admin.admin_login()
                return func(*args,**kwargs)
            elif user_type == "student":
                if not student.student_info["name"]:
                    student.student_login()
                return func(*args,**kwargs)
            elif user_type == "teacher":
                if not teacher.teacher_info["name"]:
                    teacher.teacher_login()
                return func(*args,**kwargs)
        return wrapper
    return atut

def get_all_dir_obj(path):
    if os.path.exists(path):
        obj_list=os.listdir(path)
        return obj_list
    else:
        return None