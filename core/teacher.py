from interface import teacher_interface,common_interface
from lib import common
teacher_info={
    "name":None
          }
def teacher_login():
    """登入"""
    while True:
        name = input("请输入名字").strip()
        password = input('请输入密码：').strip()
        flag, msg = common_interface.login_interface(name, password, 'teacher')
        if flag:
            print(msg)
            teacher_info['name'] = name
            break
        else:
            print(msg)

@common.logn_auth('teacher')
def choose_teach_cpirse():
    """
    选择要教授的课程
    :return:
    """
    while True:
        course_list=teacher_interface.get_all_course()
        if not course_list:
            print("课程不存在,请联系管理员创建课程")
            break
        else:
            for i,course in enumerate(course_list):
                print("%s:%s" %(i,course))
            choice = input("请选择课程:").strip()
            if choice.isdigit():
                choice = int(choice)
                if choice<len(course_list):
                    flg,msg=teacher_interface.choose_teach_course_interface(teacher_info["name"],course_list[choice])
                    if flg:
                        print(msg)
                        break
                    else:
                        print(msg)
                else:
                    print("必须输入数字")


@common.logn_auth('teacher')
def check_cpirse():
    """
    查看教授课程
    :return:
    """
    course_list=teacher_interface.check_all_teacher_course(teacher_info["name"])
    if course_list:
        for course in course_list:
            print(course)
    else:
        print("请先选择课程")

@common.logn_auth('teacher')
def check_student():
    """
    查看学生
    :return:
    """
    course_list=teacher_interface.check_all_teacher_course(teacher_info["name"])
    if course_list:
        for i,course in enumerate(course_list):
            print("%s:%s" %(i,course))
        choice = input("请选择哪门课程下的学生:").strip()
        if choice.isdigit():
            choice=int(choice)
            if choice<len(course_list):
                student_list=teacher_interface.check_student_in_course(course_list[choice])
                for i,student in enumerate(student_list):
                    print("%s:%s" %(i,student))
            else:
                print('请选择存在的课程')
        else:
            print('请输入数字')
    else:
        print("请先选择课程")

@common.logn_auth('teacher')
def modify_score():
    """
    修改分数
    :return:
    """
    course_list=teacher_interface.check_all_teacher_course(teacher_info["name"])
    if course_list:
        for i,course in enumerate(course_list):
            print("%s:%s" %(i,course))
        choice = input("请选择哪门课程下的学生:").strip()
        if choice.isdigit():
            choice=int(choice)
            if choice<len(course_list):
                student_list=teacher_interface.check_student_in_course(course_list[choice])
                for i,student in enumerate(student_list):
                    print("%s:%s" %(i,student))
                choose = input("请选择学生").strip()
                if choose.isdigit():
                    choose=int(choose)
                    if choose < len(student_list):
                        score = input("请输入分数:").strip()
                        if score.isdigit():
                            score =int(score)
                            msg=teacher_interface.modify_score(teacher_info["name"],course_list[choice],student_list[choose],score)
                            print(msg)
                        else:
                            print('必须输入数字')
                    else:
                        print('必须选择存在的学生')
            else:
                print('请选择存在的课程')
        else:
            print('请输入数字')
    else:
        print("请先选择课程")


func_dic={
    "1":teacher_login,
    "2":choose_teach_cpirse,
    "3":check_cpirse,
    "4":check_student,
    "5":modify_score
}
def teacher_view():
    while True:
        print('''
        1 登陆
        2 选择课程
        3 查看课程
        4 查看学生
        5 修改学生成绩
        ''')
        choice = input('请选择功能:').strip()
        if choice == 'q': break
        if choice not in func_dic: continue
        func_dic[choice]()