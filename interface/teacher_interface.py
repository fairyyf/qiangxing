import os
from lib import common
from conf import setting
from db import modles
def get_all_course():
    path = os.path.join(setting.Base_DB,"course")
    return common.get_all_dir_obj(path)

def choose_teach_course_interface(teacher_name,course_name):
    teacher_obj=modles.Teacher.get_obj_by_name(teacher_name)
    if course_name in teacher_obj.course_list:
        return False,"课程已存在请勿重复提交"
    teacher_obj.add_course(course_name)
    return True,"课程选择成功"

def check_all_teacher_course(teacher_name):
    obj=modles.Teacher.get_obj_by_name(teacher_name)
    return obj.course_list
    
def check_student_in_course(course):
    course_obj=modles.Course.get_obj_by_name(course)
    return course_obj.student_list
    
def modify_score(teacher_name,course_name,student_name,score):
    teacher_obj=modles.Teacher.get_obj_by_name(teacher_name)
    score_obj=teacher_obj.modify_score(student_name,course_name,score)
    return "打分完毕"