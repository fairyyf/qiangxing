from db import modles

def admin_register_interface(name,password):
    """管理员注册"""
    damin_obj=modles.Admin.get_obj_by_name(name) #读取管理员文档是否有管理员名字
    if damin_obj:
        return False,"账户已存在"
    else:
        modles.Admin(name,password)
        return True,"注册成功"

def create_school_interface(admin_name,school_name,addr):
    school_obj = modles.School.get_obj_by_name(school_name)
    if school_obj:
        return False,"学校已经存在"
    admin_obj=modles.Admin.get_obj_by_name(admin_name)
    admin_obj.create_school(school_name,addr)
    return True,"学校创建成功"

def create_teacher_interface(admin_name,teacher_name,password="456"):
    teacher_obj = modles.Teacher.get_obj_by_name(teacher_name)
    if teacher_obj:
        return False,"老师已经存在"
    admin_obj=modles.Admin.get_obj_by_name(admin_name)
    admin_obj.create_tercher(teacher_name,password)
    return True,"老师创建成功"

def create_course_interface(admin_name,course_name,school_name):
    course_obj = modles.Course.get_obj_by_name(course_name)
    if course_obj:
        return False,"课程已经存在"
    admin_obj=modles.Admin.get_obj_by_name(admin_name)
    admin_obj.create_course(course_name)
    school_obj=modles.School.get_obj_by_name(school_name)
    school_obj.add_course(course_name)
    return True,"课程创建成功"
